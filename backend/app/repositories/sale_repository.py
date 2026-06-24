from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.stock_movement import StockMovement
from app.models.transaction import Transaction
from app.models.transaction_entry import TransactionEntry
from app.models.customer import Customer
from app.repositories.stock_repository import get_current_stock
from app.utils.gst import calculate_gst
from app.repositories.ledger_repository import get_system_ledger
from app.utils.voucher import generate_sale_voucher_no
from app.repositories.financial_year_repository import get_active_financial_year


def create_sale(db, sale_data):
    
    total_amount = sum(
        item.quantity * item.rate
        for item in sale_data.items
    )

    financial_year = (get_active_financial_year(db))

    if not financial_year:
        raise Exception(
            "Active Financial Year not found"
        )
    
    voucher_no = (
        generate_sale_voucher_no(db, financial_year)
    )

    gst_data = calculate_gst(
        total_amount,
        sale_data.gst_rate,
        sale_data.intra_state
    )

    sale = Sale(
        voucher_no = voucher_no,
        sale_date = sale_data.sale_date,
        customer_id =  sale_data.customer_id,
        total_amount = gst_data["invoice_value"],
        taxable_amount = gst_data["taxable_value"],
        cgst_amount = gst_data["cgst"],
        sgst_amount = gst_data["sgst"],
        igst_amount = gst_data["igst"],
        total_tax = gst_data["total_tax"],
        financial_year_id = financial_year.id
    )

    db.add(sale)
    db.flush()

    for item in sale_data.items:
        current_stock = get_current_stock(
            db, 
            item.product_id
        )

        if current_stock < item.quantity:
            raise ValueError(
                f"Insufficient Stock. Available={current_stock}"
            )
        
        sale_item = SaleItem(
            sale_id = sale.id,
            product_id = item.product_id,
            quantity = item.quantity,
            rate = item.rate,
            amount = item.quantity * item.rate
        )
        db.add(sale_item)

        stock = StockMovement(
            product_id = item.product_id,
            movement_type = "SALE",
            quantity = item.quantity,
            rate = item.rate,
            reference_type = "SALE",
            reference_id = sale.id
        )

        db.add(stock)

    customer = (
        db.query(Customer)
        .filter(Customer.id == sale_data.customer_id)
        .first()
    )
    if not customer:
        raise Exception(
            f"Customer {sale_data.customer_id} not found"
        )
    transaction = Transaction(
        voucher_type = "SALE",
        voucher_no = voucher_no,
            transaction_date = sale_data.sale_date,
        amount = gst_data["invoice_value"],
        narrations = "Sales Voucher"

    )

    db.add(transaction)
    db.flush()

    sales_ledger = get_system_ledger(db, "SALES")
    cgst_output = get_system_ledger(db, "OUTPUT_CGST")
    sgst_output = get_system_ledger(db, "OUTPUT_SGST")
    sales_ledger_id = sales_ledger.id
    output_cgst_ledger_id = cgst_output.id
    output_sgst_ledger_id = sgst_output.id

    customer_ledger_id = customer.ledger_id

    db.add(
        TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = customer_ledger_id,
            debit = gst_data["invoice_value"],
            credit = 0
        )
    )
    db.add(
        TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = sales_ledger_id,
            debit = 0,
            credit = gst_data["taxable_value"]
        )
    )

    if gst_data["cgst"] > 0:
        db.add(
            TransactionEntry(
                transaction_id = transaction.id,
                ledger_id = output_cgst_ledger_id,
                debit = 0,
                credit = gst_data["cgst"]
            )
        )

    if gst_data["sgst"] > 0:
        db.add(
            TransactionEntry(
                transaction_id = transaction.id,
                ledger_id = output_sgst_ledger_id,
                debit = 0,
                credit = gst_data["sgst"]
            )
        )

    db.commit()

    return {
        "message": "Sales Created",
        "sales_id": sale.id,
        "voucher_no": voucher_no,
        "invoice_value": gst_data["invoice_value"]
    }

def get_all_sales(db):
    return db.query(Sale).all()