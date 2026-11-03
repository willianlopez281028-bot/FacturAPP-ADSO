from flask import Blueprint, render_template
from src.demo_data import PRODUCTS, CUSTOMERS, INVOICES, PURCHASES

home_bp = Blueprint("home", __name__)

@home_bp.get("/")
def dashboard():
    total_sales = sum(item["total"] for item in INVOICES if item["status"] != "CANCELLED")
    return render_template(
        "dashboard/index.html",
        active_page="dashboard",
        stats=[
            {"label": "Ventas del período", "value": "$ 12.480.000", "change": "+12,8%", "icon": "cash-stack", "tone": "purple"},
            {"label": "Facturas emitidas", "value": str(len(INVOICES)), "change": "+8,2%", "icon": "receipt", "tone": "blue"},
            {"label": "Productos activos", "value": str(sum(p["is_active"] for p in PRODUCTS)), "change": "Catálogo", "icon": "box-seam", "tone": "green"},
            {"label": "Clientes registrados", "value": str(len(CUSTOMERS)), "change": "Base demo", "icon": "people", "tone": "orange"},
        ],
        invoices=INVOICES[:3],
        purchases=PURCHASES[:2],
    )
