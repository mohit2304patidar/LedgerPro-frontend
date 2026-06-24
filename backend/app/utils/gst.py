def calculate_gst(
        amount: float,
        gst_rate: float,
        intra_state: bool = True
):
    gst_amount = amount * gst_rate / 100

    if intra_state:

        cgst = gst_amount / 2
        sgst = gst_amount / 2
        igst = 0
    else:
        cgst = 0
        sgst = 0
        igst = gst_amount

    return {
        "taxable_value": amount,
        "gst_rate": gst_rate,
        "cgst": round(cgst, 2),
        "sgst": round(sgst, 2),
        "igst": round(igst, 2),
        "total_tax": round(gst_amount, 2),
        "invoice_value": round(
            amount + gst_amount,
            2
        )
    }