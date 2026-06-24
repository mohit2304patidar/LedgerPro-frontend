from app.models.purchase import Purchase
from app.models.purchase_item import PurchaseItem
from app.models.stock_movement import StockMovement
from app.models.transaction import Transaction
from app.models.transaction_entry import TransactionEntry
from app.models.supplier import Supplier
from app.utils.gst import calculate_gst
from app.repositories.ledger_repository import get_system_ledger
from app.utils.voucher import generate_purchase_voucher_no
from app.repositories.financial_year_repository import get_active_financial_year

def create_purchase(db, purchase_data):
    total_amount = sum(
        item.quantity * item.rate
        for item in purchase_data.items
    )

    financial_year = (get_active_financial_year(db))

    if not financial_year:
        raise Exception(
            "Active Financial Year not found"
        )
    
    voucher_no = (
        generate_purchase_voucher_no(db, financial_year)
    )

    gst_data = calculate_gst(
        total_amount,
        purchase_data.gst_rate,
        purchase_data.intra_state
    )

    purchase = Purchase(
        voucher_no = voucher_no,
        purchase_date = purchase_data.purchase_date,
        supplier_id = purchase_data.supplier_id,
        total_amount = gst_data["invoice_value"],
        taxable_amount = gst_data["taxable_value"],
        cgst_amount = gst_data["cgst"],
        sgst_amount = gst_data["sgst"],
        igst_amount = gst_data["igst"],
        total_tax = gst_data["total_tax"],
        financial_year_id = financial_year.id
    )

    db.add(purchase)
    db.flush()

    for item in purchase_data.items:

        purchase_item = PurchaseItem(
            purchase_id = purchase.id,
            product_id = item.product_id,
            quantity = item.quantity,
            rate = item.rate,
            amount = item.quantity * item.rate
        )

        db.add(purchase_item)

        stock = StockMovement(
            product_id = item.product_id,
            movement_type = "PURCHASE",
            quantity = item.quantity,
            rate = item.rate,
            reference_type = "PURCHASE",
            reference_id = purchase.id
        )

        db.add(stock)

    supplier = (
        db.query(Supplier)
        .filter(Supplier.id == purchase_data.supplier_id)
        .first()
    )

    transaction = Transaction(
        voucher_type = "PURCHASE",
        voucher_no = voucher_no,
        transaction_date = purchase_data.purchase_date,
        amount = gst_data["invoice_value"],
        narrations = "Purchase Voucher"
    )

    db.add(transaction)
    db.flush()

    purchase_ledger =  get_system_ledger(db, "PURCHASE")
    cgst_input = get_system_ledger(db, "INPUT_CGST")
    sgst_input = get_system_ledger(db, "INPUT_SGST")
    purchase_ledger_id = purchase_ledger.id
    input_cgst_ledger_id = cgst_input.id
    input_sgst_ledger_id = sgst_input.id

    supplier_ledger_id = supplier.ledger_id

    db.add(
        TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = purchase_ledger_id,
            debit = gst_data["taxable_value"],
            credit = 0
        )
    )

    if gst_data["cgst"] > 0:
        db.add(
            TransactionEntry(
                transaction_id = transaction.id,
                ledger_id = input_cgst_ledger_id,
                debit = gst_data["cgst"],
                credit = 0
            )
        )
    
    if gst_data["sgst"] > 0:
        db.add(
            TransactionEntry(
                transaction_id = transaction.id,
                ledger_id = input_sgst_ledger_id,
                debit = gst_data["sgst"],
                credit = 0
            )
        )
    db.add(
        TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = supplier_ledger_id,
            debit = 0,
            credit = gst_data["invoice_value"]
        )
    )

    db.commit()
    return {
        "message": "Purchase Created",
        "purchase_id": purchase.id,
        "voucher_no": voucher_no,
        "invoice_value": gst_data["invoice_value"]
    }


def get_all_purchases(db):
    return db.query(Purchase).all()