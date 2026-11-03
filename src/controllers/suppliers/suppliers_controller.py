from flask import Blueprint, render_template
from src.demo_data import SUPPLIERS
suppliers_bp = Blueprint("suppliers", __name__, url_prefix="/suppliers")

@suppliers_bp.get("/")
def list_suppliers():
    return render_template("suppliers/index.html", active_page="suppliers", suppliers=SUPPLIERS)
