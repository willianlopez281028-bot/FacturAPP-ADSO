# FactureAPP — Frontend

Frontend administrativo construido con Flask, Jinja2 y Bootstrap 5.3.8.

## Requisitos
- Python 3.10+
- pip
- Navegador moderno
- Conexión a internet para cargar Bootstrap e iconos desde CDN

## Instalación (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

## Instalación (macOS/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Abrir http://127.0.0.1:5000

## Arquitectura
- `src/__init__.py`: Application Factory y registro de Blueprints.
- `src/controllers/`: controladores separados por módulo funcional (`clients/`, `products/`, `invoices/`, etc.); cada módulo contiene su propio archivo de rutas y `__init__.py`.
- `src/templates/`: vistas Jinja2 y layout compartido.
- `src/static/`: CSS y JavaScript propios.
- `src/demo_data.py`: datos ficticios para demostrar la interfaz.

La organización sigue la lógica del proyecto de referencia del instructor: paquete `src`, inicialización de Flask, controladores por funcionalidad y plantillas compartidas. Se amplía esa estructura agrupando cada controlador en su propia carpeta para mantener el proyecto modular.

## Alcance actual
Es una implementación de frontend con datos simulados. Los formularios y filtros permiten probar la experiencia de usuario, pero no guardan información en MySQL ni ejecutan operaciones contables o de inventario reales. Las rutas están organizadas para conectar posteriormente servicios y persistencia.

## Modelo de datos considerado
La interfaz toma como referencia las tablas del modelo EER suministrado: `users`, `customers`, `suppliers`, `product_categories`, `products`, `product_suppliers`, `purchase_orders`, `purchase_order_items`, `invoices`, `invoice_items`, `inventory_movements` y `accounting_entries`.

Los nombres de campos y estados usados en formularios se alinean con el modelo disponible. No se inventa persistencia para atributos que no existen en el esquema.


## Documentación detallada
Consulta [`DOCUMENTACION.md`](DOCUMENTACION.md) para conocer la arquitectura, los controladores, las rutas, las plantillas, los datos de demostración, la instalación, las pruebas y los pasos pendientes para conectar MySQL.


## Módulo de usuarios
Se incorporó una primera integración del módulo de gestión de cuentas con MySQL. Revisa `DOCUMENTACION.md` para configurar la conexión y conocer la protección temporal: el módulo requiere autenticación administrativa, que aún está pendiente de implementar.


## Módulo de usuarios (modo demostración)

El módulo de usuarios funciona sin MySQL. Utiliza un repositorio en memoria (`src/repositories/users/in_memory_user_repository.py`) y permite listar, buscar, crear, editar, activar/desactivar cuentas y cambiar contraseñas. Los cambios se pierden al reiniciar el servidor.

Usuarios iniciales de demostración:
- `admin` — rol `ADMIN` — contraseña `Admin123!`
- `cajero01` — rol `CASHIER` — contraseña `Cajero123!`
- `cajero02` — rol `CASHIER` — contraseña `Cajero123!`

Estas cuentas son únicamente datos de demostración; no implementan autenticación ni deben utilizarse en producción.

Para ejecutar: `python -m pip install -r requirements.txt` y `python run.py`. No se requiere archivo `.env`, servidor MySQL, SQLAlchemy ni PyMySQL.
