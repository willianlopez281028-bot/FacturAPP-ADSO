from flask import Blueprint, render_template
from src.demo_data import PURCHASES
purchases_bp = Blueprint("purchases", __name__, url_prefix="/purchases")

@purchases_bp.get("/")
def list_purchases():
    return render_template("purchases/index.html", active_page="purchases", purchases=PURCHASES)
