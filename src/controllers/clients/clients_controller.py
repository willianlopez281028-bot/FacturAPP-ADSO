from flask import Blueprint, render_template, request
from src.demo_data import CUSTOMERS
clients_bp = Blueprint("clients", __name__, url_prefix="/customers")

@clients_bp.get("/")
def list_clients():
    query = request.args.get("q", "").strip().lower()
    customers = [c for c in CUSTOMERS if query in (c["name"] + c["identity_number"] + c["email"]).lower()]
    return render_template("customers/index.html", active_page="customers", customers=customers, query=query)

@clients_bp.get("/new")
@clients_bp.get("/<int:customer_id>/edit")
def client_form(customer_id=None):
    customer = next((c for c in CUSTOMERS if c["id"] == customer_id), None) if customer_id else None
    return render_template("customers/form.html", active_page="customers", customer=customer)
