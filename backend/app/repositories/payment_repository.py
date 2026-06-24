from app.models.payment import Payment
from app.models.supplier import Supplier
from app.models.transaction import Transaction
from app.models.transaction_entry import TransactionEntry
from app.repositories.financial_year_repository import get_active_financial_year
from app.utils.voucher import generate_payment_voucher_no

def create_payment(db, payment_data):

    financial_year = get_active_financial_year(db)
    voucher_no = generate_payment_voucher_no(db, financial_year)
    supplier = (
        db.query(Supplier).filter(
            Supplier.id == payment_data.supplier_id
        ).first()
    )

    if not supplier:
        raise Exception(
            f"Supplier {payment_data.supplier_id} not found"
        )
    
    if not supplier.ledger_id:
        raise Exception(
            "Supplier Ledger not linked"
        )
    
    payment = Payment(
        voucher_no = voucher_no,
        payment_date = payment_data.payment_date,
        supplier_id = payment_data.supplier_id,
        bank_ledger_id = payment_data.bank_ledger_id,
        financial_year_id = financial_year.id,
        amount = payment_data.amount,
        narration = payment_data.narration
    )

    db.add(payment)
    db.flush()

    transaction = Transaction(
        voucher_type = "PAYMENT",
        voucher_date = payment_data.payment_date,
        narration = "Payment Voucher"
    )

    db.add(transaction)
    db.flush()

    supplier_entry = TransactionEntry(
        transaction_id = transaction.id,
        ledger_id = supplier.ledger_id,
        debit = payment_data.amount,
        credit = 0
    )

    db.add(supplier_entry)

    bank_entry = TransactionEntry(
        transaction_id = transaction.id,
        ledger_id = payment_data.bank_ledger_id,
        debit = 0,
        credit = payment_data.amount
    )

    db.add(bank_entry)
    db.commit()
    return {
        "message": "Payment Created",
        "voucher_no": voucher_no
    }