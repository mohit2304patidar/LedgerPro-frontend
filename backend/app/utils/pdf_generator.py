import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

def generate_invoice_pdf(
    invoice_no,
    customer_name,
    customer_mobile,
    customer_email,
    customer_gst,
    customer_pan,
    customer_address,
    date,
    items,
    taxable_amount,
    cgst_amount,
    sgst_amount,
    total_amount,
):

    folder = "generated_invoices"
    os.makedirs(folder, exist_ok=True)
    safe_invoice_no = (invoice_no.replace("/", "_"))
    filename = os.path.join(folder,f"{safe_invoice_no}.pdf")
    
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()
    elements = []
    title = Paragraph("<b>LEDGERPRO TAX INVOICE</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 15))

    company_table = Table([
        [
            "Company",
            "LedgerPro Pvt. Ltd."
        ],
        [
            "GSTIN",
            "23ABCDE1234F1Z5"
        ],
        [
            "Location",
            "Indore, Madhya Pradesh"
        ]
    ])

    company_table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ])
    )

    elements.append(company_table)
    elements.append(Spacer(1, 20))
    invoice_table = Table([
        ["Invoice No", invoice_no],
        ["Date", str(date)],
    ])
    invoice_table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ])
    )

    elements.append(invoice_table)
    elements.append(Spacer(1, 20))

    customer_table = Table([
        ["Customer", customer_name],
        ["Mobile", customer_mobile],
        ["Email", customer_email],
        ["GSTIN", customer_gst],
        ["PAN", customer_pan],
        ["Address", customer_address]
    ])

    customer_table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ])
    )

    elements.append(customer_table)
    elements.append(Spacer(1, 20))
    product_data = [[
        "Sr No",
        "Product",
        "Qty",
        "Rate",
        "Amount"
    ]]

    for index, item in enumerate(items, start=1):
        amount = (item["quantity"] * item["rate"])
        product_data.append([
            index,
            item["product_name"],
            item["quantity"],
            f"₹ {item['rate']}",
            f"₹ {amount}"
        ])

    products_table = Table(
        product_data,
        colWidths=[50,220,60,80,100]
    )

    products_table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#232F3E")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ])
    )

    elements.append(products_table)
    elements.append(Spacer(1, 20))
    summary_table = Table([
        ["Taxable Amount",
         f"₹ {taxable_amount}"],
        ["CGST",
         f"₹ {cgst_amount}"],
        ["SGST",
         f"₹ {sgst_amount}"],
        ["Grand Total",
         f"₹ {total_amount}"]
    ])

    summary_table.setStyle(
        TableStyle([
            ("GRID",(0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 3), (-1, 3), colors.lightgrey),
            ("FONTNAME", (0, 3), (-1, 3), "Helvetica-Bold"),
        ])
    )

    elements.append(summary_table)
    elements.append(Spacer(1, 30))
    elements.append(Paragraph("<b>Authorized Signature</b>", styles["Normal"]))
    elements.append(Spacer(1, 40))
    elements.append(Paragraph("This is a computer generated invoice.", styles["Italic"]))
    doc.build(elements)
    
    return filename