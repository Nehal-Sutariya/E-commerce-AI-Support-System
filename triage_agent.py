def triage(ticket):
    if "refund" in ticket.lower():
        return {"issue": "refund", "confidence": 0.9}
    return {"issue": "other", "confidence": 0.5}
