from flask import Blueprint, render_template
from src.demo_data import MOVEMENTS, PRODUCTS
inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

@inventory_bp.get("/")
def inventory_overview():
    return render_template("inventory/index.html", active_page="inventory", movements=MOVEMENTS, products=PRODUCTS)
