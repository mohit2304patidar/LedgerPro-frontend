from app.models.receipt import Receipt
from app.models.customer import Customer
from app.models.transaction import Transaction
from app.models.transaction_entry import TransactionEntry
from app.utils.voucher import generate_receipt_voucher_no
from app.repositories.financial_year_repository import get_active_financial_year

def create_receipt(db, receipt_data):
    
    customer = (
        db.query(Customer).filter(
            Customer.id == receipt_data.customer_id
        ).first()
    )

    if not customer:
        raise Exception(
            f"Customer {receipt_data.customer_id} not found"
        )
    
    if not customer.ledger_id:
        raise Exception(
            "Customer Ledger not linked"
        )
    
    financial_year = get_active_financial_year(db)

    voucher_no = generate_receipt_voucher_no(db, financial_year)
    receipt = Receipt(
        voucher_no = voucher_no,
        receipt_date = receipt_data.receipt_date,
        customer_id = receipt_data.customer_id,
        bank_ledger_id = receipt_data.bank_ledger_id,
        amount = receipt_data.amount,
        narration = receipt_data.narration,
        financial_year_id = financial_year.id
    )

    db.add(receipt)
    db.flush()

    customer = (
        db.query(Customer).filter(
            Customer.id == receipt_data.customer_id
        ).first()
    )

    transaction = Transaction(
        voucher_type = "RECEIPT",
        voucher_no = voucher_no,
        amount = receipt_data.amount,
        narrations = "RECEIPT Voucher"
    )

    db.add(transaction)
    db.flush()

    # Bank DR

    db.add(
        TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = receipt_data.bank_ledger_id,
            debit = receipt_data.amount,
            credit = 0
        )
    )

    #Customer CR

    db.add(
        TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = customer.ledger_id,
            debit = 0,
            credit = receipt_data.amount
        )
    )

    db.commit()
    return {
        "message": "Receipt Created",
        "voucher_no": voucher_no
    }