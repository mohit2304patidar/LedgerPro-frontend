from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import Base, engine
from app.models import user
from app.api.auth import router as auth_router
from app.api.company import router as company_router
from app.api.ledger_group import router as ledger_group_router
from app.api.ledger import router as ledger_router
from app.api.customer import router as customer_router
from app.api.supplier import router as supplier_router
from app.api.transaction import router as transaction_router
from app.api.product import router as product_router
from app.api.category import router as category_router
from app.api.unit import router as unit_router
from app.api.stock import router as stock_router
from app.api.purchase import router as purchase_router
from app.api.sale import router as sale_router
from app.api.dashboard import router as dashboard_router
from app.api.gst import router as gst_router
from app.api.company_settings import router as company_settings_router
from app.api.financial_year import router as financial_year_router
from app.api.bank import router as bank_router
from app.api.receipt import router as receipt_router
from app.api.payment import router as payment_router
from app.api.invoice import router as invoice_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "LedgerPro API",
    version = "1.0.0"
)

app.include_router(auth_router)
app.include_router(company_router)
app.include_router(ledger_group_router)
app.include_router(ledger_router)
app.include_router(customer_router)
app.include_router(supplier_router)
app.include_router(transaction_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(unit_router)
app.include_router(stock_router)
app.include_router(purchase_router)
app.include_router(sale_router)
app.include_router(dashboard_router)
app.include_router(gst_router)
app.include_router(company_settings_router)
app.include_router(financial_year_router)
app.include_router(bank_router)
app.include_router(receipt_router)
app.include_router(payment_router)
app.include_router(invoice_router)

#from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message" : "LedgerPro API Running"}
