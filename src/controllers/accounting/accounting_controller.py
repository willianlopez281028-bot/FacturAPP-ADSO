from flask import Blueprint, render_template
from src.demo_data import ENTRIES
accounting_bp = Blueprint("accounting", __name__, url_prefix="/accounting")

@accounting_bp.get("/")
def accounting_overview():
    return render_template("accounting/index.html", active_page="accounting", entries=ENTRIES)
