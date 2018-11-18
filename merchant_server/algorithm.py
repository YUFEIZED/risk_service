from decimal import Decimal

def risk_assessment(purchase_amount, credit):
    if Decimal(purchase_amount) <= credit:
        return True
    else:
        return False