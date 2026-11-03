from flask import Blueprint, render_template
from src.demo_data import INVOICES, CUSTOMERS, PRODUCTS
invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")

@invoices_bp.get("/")
def list_invoices():
    return render_template("invoices/index.html", active_page="invoices", invoices=INVOICES)

@invoices_bp.get("/new")
def new_invoice():
    return render_template("invoices/form.html", active_page="invoices", customers=CUSTOMERS, products=PRODUCTS)
