from agents.triage_agent import triage
from agents.retriever_agent import retrieve_policy
from agents.writer_agent import write_response
from agents.compliance_agent import check_compliance

ticket = "My cookies arrived melted. I want refund."
context = {
    "item_category": "perishable",
    "order_status": "delivered"
}

classification = triage(ticket)
docs = retrieve_policy(ticket)
response = write_response(ticket, docs)
final = check_compliance(response, docs)

print(final)
