from sqlalchemy import func
from app.models.purchase import Purchase
from app.models.sale import Sale
from app.models.receipt import Receipt
from app.models.payment import Payment

def generate_purchase_voucher_no(db, financial_year):
    count = (
        db.query(
            func.count(Purchase.id)
        ).filter(
            Purchase.financial_year_id == financial_year.id
        ).scalar()
    )

    return (
        f"PUR/{financial_year.fy_name}"
        f"{str(count + 1).zfill(5)}"
    )

def generate_sale_voucher_no(db, financial_year):
    count = (
        db.query(
            func.count(Sale.id)
        ).filter(
            Sale.financial_year_id == financial_year.id
        ).scalar()
    )

    return (
        f"SAL/{financial_year.fy_name}"
        f"{str(count + 1).zfill(5)}"
    )

def generate_receipt_voucher_no(db, financial_year):
    count = (
        db.query(
            Receipt
        ).filter(
            Receipt.financial_year_id == financial_year.id
        ).count()
    )

    return f"REC/{financial_year.fy_name}/{str(count + 1).zfill(5)}"
    

def generate_payment_voucher_no(db, financial_year):

    count = (
        db.query(Payment).filter(
            Payment.financial_year_id == financial_year.id
        ).count()
    )

    return (
        f"PAY/{financial_year.fy_name}/"
        f"{str(count + 1).zfill(5)}"
    )