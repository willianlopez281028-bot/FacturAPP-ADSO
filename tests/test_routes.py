from src import create_app

def test_main_pages_load():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    for path in ["/", "/products/", "/categories/", "/customers/", "/suppliers/",
                 "/purchases/", "/invoices/", "/invoices/new", "/inventory/", "/accounting/"]:
        response = client.get(path)
        assert response.status_code == 200, path


def test_product_status_filter():
    app = create_app()
    app.config["TESTING"] = True
    response = app.test_client().get("/products/?status=active")
    assert response.status_code == 200
    assert b"Activos" in response.data


def test_modular_controller_packages_import():
    from src.controllers.clients.clients_controller import clients_bp
    from src.controllers.products.products_controller import products_bp
    assert clients_bp.name == "clients"
    assert products_bp.name == "products"
