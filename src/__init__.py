import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "factureapp-local-demo-key"

    def format_cop(value):
        try:
            return "$ " + f"{float(value):,.0f}".replace(",", ".")
        except (TypeError, ValueError):
            return "$ 0"

    app.jinja_env.filters["cop"] = format_cop

    from src.controllers.dashboard.home_controller import home_bp
    from src.controllers.products.products_controller import products_bp
    from src.controllers.categories.categories_controller import categories_bp
    from src.controllers.clients.clients_controller import clients_bp
    from src.controllers.suppliers.suppliers_controller import suppliers_bp
    from src.controllers.purchases.purchases_controller import purchases_bp
    from src.controllers.invoices.invoices_controller import invoices_bp
    from src.controllers.inventory.inventory_controller import inventory_bp
    from src.controllers.accounting.accounting_controller import accounting_bp
    from src.controllers.users.users_controller import users_bp
    from src.repositories.users.in_memory_user_repository import InMemoryUserRepository
    from werkzeug.security import generate_password_hash

    # Repositorio temporal: se reemplazará por un adaptador SQL cuando se autorice.
    app.extensions["user_repository"] = InMemoryUserRepository([
        {"username": "admin", "password_hash": generate_password_hash("Admin123!"), "role": "ADMIN"},
        {"username": "cajero01", "password_hash": generate_password_hash("Cajero123!"), "role": "CASHIER"},
        {"username": "cajero02", "password_hash": generate_password_hash("Cajero123!"), "role": "CASHIER"},
    ])

    blueprints = (
        home_bp, products_bp, categories_bp, clients_bp, suppliers_bp,
        purchases_bp, invoices_bp, inventory_bp, accounting_bp, users_bp
    )
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
