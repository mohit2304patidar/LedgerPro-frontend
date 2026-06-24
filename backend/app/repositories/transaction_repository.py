from decimal import Decimal
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from app.models.transaction import Transaction
from app.models.transaction_entry import TransactionEntry
from app.utils.voucher_generator import generate_voucher_number
from app.models.ledger import Ledger
from app.models.ledger_group import LedgerGroup


def create_transaction(db, transaction_data):
    transaction = Transaction(
        voucher_type = transaction_data.voucher_type,
        narration = transaction_data.narrations
    )

    db.add(transaction)
    db.flush()

    transaction.voucher_no = generate_voucher_number(
        transaction.voucher_type,
        transaction.id
    )

    for entry in transaction_data.entries:
        transaction_entry = TransactionEntry(
            transaction_id = transaction.id,
            ledger_id = entry.ledger_id,
            debit = entry.debit,
            credit = entry.credit
        )
        db.add(transaction_entry)
    
    db.commit()
    db.refresh(transaction)

    print( f"Transaction Created : {transaction.voucher_no}")
    return transaction

def get_transactions(db):
    return db.query(Transaction).all()

def get_daybook(db):
    return (
        db.query(Transaction)
        .order_by(
            Transaction.created_at.desc()
        )
        .all()
    )

def get_ledger_statement(db, ledger_id: int):
    ledger = (
        db.query(Ledger)
        .filter(Ledger.id == ledger_id)
        .first()
    )

    if not ledger:
        return None
    
    entries = (
        db.query(TransactionEntry)
        .filter(
            TransactionEntry.ledger_id == ledger_id
        )
        .all()
    )

    total_debit = sum(
        Decimal(entry.debit or 0)
        for entry in entries
    )

    total_credit = sum(
        Decimal(entry.credit or 0)
        for entry in entries
    )

    closing_balance = (
        ledger.opening_balance
        + total_debit 
        - total_credit
    )

    return {
        "ledger": ledger.name,
        "opening_balance": float(ledger.opening_balance or 0),
        "total_debit": float(total_debit),
        "total_credit": float(total_credit),
        "closing_balance": float(closing_balance),
        "transactions": entries
    }

def get_trial_balance(db):
    ledgers = db.query(Ledger).all()

    result = []

    total_debit = 0
    total_credit = 0
    for ledger in ledgers:

        debit = (
            db.query(
                func.coalesce(
                    func.sum(TransactionEntry.debit),
                    0
                )
            )
            .filter(
                TransactionEntry.ledger_id == ledger.id
            )
            .scalar()
        )

        credit = (
            db.query(
                func.coalesce(
                    func.sum(TransactionEntry.credit),
                    0
                )
            )
            .filter(
                TransactionEntry.ledger_id == ledger.id
            )
            .scalar()
        )

        if debit != 0 or credit != 0:

            result.append(
                {
                    "ledger_id": ledger.id,
                    "ledger_name": ledger.name,
                    "debit": float(debit),
                    "credit": float(credit)
                }
            )

            total_debit += float(debit)
            total_credit += float(credit)

    return {
        "ledgers": result,
        "total_debit": total_debit,
        "total_credit": total_credit,
        "difference": total_debit - total_credit
    }

def get_profit_loss(db):

    income_groups = [
        "Sales",
        "Direct Income",
        "Indirect Income"
    ]

    expense_groups = [
        "Purchase",
        "Direct Expense",
        "Indirect Expense"
    ]

    income_total = 0
    expense_total = 0

    income_ledgers = []
    expense_ledgers = []

    ledgers = db.query(Ledger).all()

    for ledger in ledgers:

        group = (
            db.query(LedgerGroup)
            .filter(LedgerGroup.id == ledger.group_id)
            .first()
        )

        if not group:
            continue

        debit = (
            db.query(
                func.coalesce(
                    func.sum(TransactionEntry.debit),
                    0
                )
            )
            .filter(
                TransactionEntry.ledger_id == ledger.id
            )
            .scalaer()
        )

        credit = (
            db.query(
                func.coalesce(
                    func.sum(TransactionEntry.credit),
                    0
                )
            )
            .filter(
                TransactionEntry.ledger_id == ledger.id
            )
            .scalar()
        )

        balance = float(credit) - float(debit)

        if group.name in income_groups:
            
            income_ledgers.append({
                "ledger": ledger.name,
                "amount": balance
            })

            income_total += balance
        
        elif group.name in expense_groups:
            
            amount = float(debit) - float(credit)

            expense_ledgers.append({
                "ledger": ledger.name,
                "amount": amount
            })

            expense_total += amount

    profit = income_total - expense_total

    return {
        "income": income_ledgers,
        "expenses": expense_ledgers,
        "total_income": income_total,
        "total_expense": expense_total,
        "net_profit": profit
    }

def get_balance_sheet(db):

    asset_groups = [
        "Cash-in-Hand",
        "Bank Accounts",
        "Sundry Debtors",
        "Current Assets",
        "Fixed Assets",
        "Stock-in-Hand"
    ]

    liability_groups = [
        "Sundry Creditors",
        "Current Liabilities",
        "Loans",
        "DUties & Taxes"
    ]

    capital_groups = [
        "Capital Account",
        "Reserves & Surplus"
    ]

    assets = []
    liabilities = []
    capitals = []
    total_assets = 0
    total_liabilities = 0
    total_captial = 0
    ledgers = db.query(Ledger).all()

    for ledger in ledgers:
        group = (
            db.query(LedgerGroup)
            .filter(
                LedgerGroup.id == ledger.group_id
            )
            .first()
        )

        if not group:
            continue

        debit = (
            db.query(
                func.coalesce(
                    func.sum(TransactionEntry.debit),
                    0
                )
            )
            .filter(
                TransactionEntry.ledger_id == ledger.id
            )
            .scalar()
        )

        credit = (
            db.query(
                func.coalesce(
                    func.sum(TransactionEntry.credit),
                    0
                )
            )
            .filter(
                TransactionEntry.ledger_id == ledger.id
            )
            .scalar()
        )

        asset_balance = (
            float(ledger.opening_balance)
            + float(debit)
            - float(credit)
        )

        liability_balance = (
            float(ledger.opening_balance)
            + float(credit)
            - float(debit)
        )

        if group.name in asset_groups:
            assets.append({
                "ledger": ledger.name,
                "amount": asset_balance
            })

            total_assets += asset_balance
        elif group.name in liability_groups:
            liabilities.append({
                "ledger": ledger.name,
                "amount": liability_balance
            })

        elif group.name in capital_groups:
            capitals.append({
                "ledger": ledger.name,
                "amount": liability_balance
            })

            total_captial += liability_balance

    return {
        "assets": assets,
        "liabilities": liabilities,
        "capital": capitals,
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "total_capital": total_captial,
        "difference": total_assets - (total_liabilities + total_captial)
    }

def get_cash_flow(db):
    
    cash_ledgers = (
        db.query(Ledger)
        .filter(
            Ledger.ledger_type == "CASH"
        )
        .all()
    )

    cash_ids = [l.id for l in cash_ledgers]

    inflow = 0
    outflow = 0

    entries = (
        db.query(TransactionEntry)
        .filter(
            TransactionEntry.ledger_id.in_(cash_ids)
        )
        .all()
    )

    for entry in entries:

        inflow += float(entry.debit or 0)
        outflow += float(entry.credit or 0)

    opening_cash = sum(
        float(l.opening_balance or 0)
        for l in cash_ledgers
    )

    closing_cash = (
        opening_cash
        + inflow
        - outflow
    )

    return {
        "opening_cash": opening_cash,
        "cash_inflow": inflow,
        "cash_outflow": outflow,
        "closing_cash": closing_cash
    }