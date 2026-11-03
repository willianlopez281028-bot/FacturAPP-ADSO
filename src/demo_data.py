"""Datos ficticios de demostración. No representan registros reales."""

PRODUCTS = [
    {"id": 1, "barcode": "7701234567890", "name": "Arroz premium 1 kg", "brand": "Diana", "category": "Granos", "cost": 3200, "sale_price": 4500, "current_stock": 42, "minimum_stock": 10, "is_active": True},
    {"id": 2, "barcode": "7709876543210", "name": "Huevos AA x 30", "brand": "Avinal", "category": "Abarrotes", "cost": 12500, "sale_price": 15800, "current_stock": 8, "minimum_stock": 12, "is_active": True},
    {"id": 3, "barcode": "7701111222233", "name": "Pan tajado", "brand": "Bimbo", "category": "Panadería", "cost": 4100, "sale_price": 5600, "current_stock": 25, "minimum_stock": 8, "is_active": True},
    {"id": 4, "barcode": "7704444555566", "name": "Aceite vegetal 900 ml", "brand": "Premier", "category": "Abarrotes", "cost": 7200, "sale_price": 9300, "current_stock": 4, "minimum_stock": 10, "is_active": False},
]
CUSTOMERS = [
    {"id": 1, "name": "Laura Martínez", "identity_type": "CC", "identity_number": "1032456789", "phone_number": "300 123 4567", "email": "laura@example.com", "city": "Medellín", "is_active": True},
    {"id": 2, "name": "Carlos Gómez", "identity_type": "CC", "identity_number": "98543210", "phone_number": "310 555 0198", "email": "carlos@example.com", "city": "Envigado", "is_active": True},
    {"id": 3, "name": "Comercial El Centro", "identity_type": "NIT", "identity_number": "901234567-1", "phone_number": "604 444 2233", "email": "compras@example.com", "city": "Sabaneta", "is_active": True},
]
SUPPLIERS = [
    {"id": 1, "name": "Distribuciones Antioquia", "tax_id": "900123456-7", "phone_number": "604 333 2211", "email": "ventas@distribuciones.example", "is_active": True},
    {"id": 2, "name": "Alimentos del Valle", "tax_id": "800987654-3", "phone_number": "310 222 1122", "email": "pedidos@alimentos.example", "is_active": True},
]
INVOICES = [
    {"id": 1, "invoice_number": "FAC-000128", "customer": "Laura Martínez", "issued_at": "02 nov 2026", "total": 185000, "payment_method": "CASH", "status": "PAID"},
    {"id": 2, "invoice_number": "FAC-000127", "customer": "Carlos Gómez", "issued_at": "01 nov 2026", "total": 96500, "payment_method": "CARD", "status": "ISSUED"},
    {"id": 3, "invoice_number": "FAC-000126", "customer": "Comercial El Centro", "issued_at": "31 oct 2026", "total": 428000, "payment_method": "BANK_TRANSFER", "status": "PARTIALLY_PAID"},
]
PURCHASES = [
    {"id": 1, "purchase_order_number": "OC-00042", "supplier": "Distribuciones Antioquia", "ordered_at": "02 nov 2026", "expected_delivery_date": "05 nov 2026", "total": 860000, "status": "SENT"},
    {"id": 2, "purchase_order_number": "OC-00041", "supplier": "Alimentos del Valle", "ordered_at": "30 oct 2026", "expected_delivery_date": "03 nov 2026", "total": 425000, "status": "PARTIALLY_RECEIVED"},
]
MOVEMENTS = [
    {"id": 1, "product": "Arroz premium 1 kg", "movement_type": "PURCHASE_IN", "quantity": 30, "reference_type": "PURCHASE_ORDER", "reference_id": 42, "created_at": "02 nov 2026"},
    {"id": 2, "product": "Huevos AA x 30", "movement_type": "SALE_OUT", "quantity": 4, "reference_type": "INVOICE", "reference_id": 128, "created_at": "02 nov 2026"},
    {"id": 3, "product": "Aceite vegetal 900 ml", "movement_type": "ADJUSTMENT_OUT", "quantity": 2, "reference_type": "MANUAL", "reference_id": "—", "created_at": "01 nov 2026"},
]
ENTRIES = [
    {"id": 1, "entry_number": "ASI-00128", "entry_type": "INCOME", "description": "Ingreso por factura FAC-000128", "amount": 185000, "recorded_at": "02 nov 2026"},
    {"id": 2, "entry_number": "ASI-00127", "entry_type": "EXPENSE", "description": "Compra de mercancía", "amount": 860000, "recorded_at": "02 nov 2026"},
]
