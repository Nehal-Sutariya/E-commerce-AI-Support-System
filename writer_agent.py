def write_response(ticket, docs):
    return {
        "decision": "deny",
        "reason": docs[0],
        "customer_message": "Sorry, perishable items are not eligible for refund."
    }
