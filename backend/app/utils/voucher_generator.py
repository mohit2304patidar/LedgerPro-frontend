def generate_voucher_number(voucher_type, last_id):
    prefixes = {
        "PAYMENT": "PAY",
        "RECEIPT": "REC",
        "JOURNAL":  "JV",
        "CONTRA": "CON",
        "SALES": "SAL",
        "PURCHASE": "PUR"
    }

    prefix = prefixes.get(
        voucher_type.upper(),
        "VCH"
    )

    return f"{prefix}-{str(last_id).zfill(5)}"