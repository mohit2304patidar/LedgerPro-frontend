from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.customer import Customer
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.utils.pdf_generator import generate_invoice_pdf

router = APIRouter(
    prefix="/Invoice",
    tags=["Invoice"]
)

@router.get("/sales/{sale_id}")
def sales_invoice(
    sale_id: int,
    db: Session = Depends(get_db)
):

    sale = (db.query(Sale).filter(Sale.id == sale_id).first())

    if not sale:
        return {"error": "Sale not found"}

    customer = (
        db.query(Customer)
        .filter(Customer.id == sale.customer_id)
        .first()
    )

    if not customer:
        return {"error": "Customer not found"}

    sale_items = (db.query(SaleItem).filter(SaleItem.sale_id == sale.id).all())

    items = []

    for item in sale_items:

        product = (
            db.query(Product)
            .filter(Product.id == item.product_id)
            .first()
        )

        items.append({
            "product_name":
                product.name
                if product
                else "Unknown Product",

            "quantity":
                float(item.quantity),

            "rate":
                float(item.rate)
        })

    pdf_path = generate_invoice_pdf(
        invoice_no=sale.voucher_no,
        customer_name=customer.name,
        customer_mobile=customer.mobile,
        customer_email=customer.email,
        customer_gst=customer.gst_number,
        customer_pan=customer.pan_number,
        customer_address=
            f"{customer.address}, "
            f"{customer.city}, "
            f"{customer.state}",
        date=sale.sale_date,
        items=items,
        taxable_amount=float(sale.taxable_amount),
        cgst_amount=float(sale.cgst_amount),
        sgst_amount=float(sale.sgst_amount),
        total_amount=float(sale.total_amount)
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"{sale.voucher_no}.pdf"
    )