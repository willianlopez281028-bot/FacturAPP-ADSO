from flask import Blueprint, render_template, request
from src.demo_data import PRODUCTS

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.get("/")
def list_products():
    query = request.args.get("q", "").strip().lower()
    status = request.args.get("status", "all")
    products = [p for p in PRODUCTS if query in (p["name"] + p["barcode"] + p["brand"]).lower()]
    if status == "active":
        products = [p for p in products if p["is_active"]]
    elif status == "inactive":
        products = [p for p in products if not p["is_active"]]
    return render_template("products/index.html", active_page="products", products=products, query=query, status=status)

@products_bp.get("/new")
@products_bp.get("/<int:product_id>/edit")
def product_form(product_id=None):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None) if product_id else None
    return render_template("products/form.html", active_page="products", product=product)
