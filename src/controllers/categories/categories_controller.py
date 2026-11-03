from flask import Blueprint, render_template
categories_bp = Blueprint("categories", __name__, url_prefix="/categories")

@categories_bp.get("/")
def list_categories():
    categories = [
        {"id": 1, "name": "Abarrotes", "description": "Productos de consumo básico", "products": 2, "is_active": True},
        {"id": 2, "name": "Granos", "description": "Arroz, fríjoles y cereales", "products": 1, "is_active": True},
        {"id": 3, "name": "Panadería", "description": "Pan y productos horneados", "products": 1, "is_active": True},
    ]
    return render_template("categories/index.html", active_page="categories", categories=categories)
