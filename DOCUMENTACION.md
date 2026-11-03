# Documentación técnica del código — FactureAPP

## 1. Descripción general

FactureAPP es una interfaz web de demostración para apoyar la gestión comercial y administrativa de un negocio. La aplicación presenta módulos de productos, categorías, clientes, proveedores, compras, ventas y facturación, inventario y finanzas.

La versión documentada es principalmente **frontend**: utiliza Flask para atender las rutas y renderizar las páginas, Jinja2 para construir las vistas HTML y Bootstrap 5.3.8 para los componentes visuales. La información que se muestra proviene de datos de demostración definidos en Python.

> **Alcance:** esta versión no conecta con MySQL, no guarda cambios de manera permanente y no ejecuta procesos reales de facturación, contabilidad, compras o inventario. Los botones y formularios identificados como demostrativos no deben interpretarse como operaciones productivas.

## 2. Tecnologías utilizadas

| Tecnología | Uso en el proyecto |
|---|---|
| Python 3.10 o superior | Lenguaje de programación del servidor |
| Flask 3.x | Aplicación web, rutas y controladores |
| Jinja2 | Plantillas HTML y presentación de datos |
| Bootstrap 5.3.8 | Diseño adaptable y componentes visuales |
| Bootstrap Icons 1.11.3 | Iconografía |
| JavaScript | Interacciones del frontend |
| CSS | Estilos propios de FactureAPP |
| pytest | Ejecución de pruebas automatizadas |

Bootstrap y Bootstrap Icons se cargan desde CDN; por eso la interfaz necesita conexión a internet para descargar esos recursos.

## 3. Estructura de carpetas

```text
FactureAPP/
├── run.py
├── requirements.txt
├── README.md
├── DOCUMENTACION.md
├── ESTRUCTURA_PROYECTO.txt
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── demo_data.py
│   ├── controllers/
│   │   ├── dashboard/
│   │   ├── products/
│   │   ├── categories/
│   │   ├── clients/
│   │   ├── suppliers/
│   │   ├── purchases/
│   │   ├── invoices/
│   │   ├── inventory/
│   │   └── accounting/
│   ├── templates/
│   │   ├── layout.html
│   │   ├── components/
│   │   ├── dashboard/
│   │   ├── products/
│   │   ├── categories/
│   │   ├── customers/
│   │   ├── suppliers/
│   │   ├── purchases/
│   │   ├── invoices/
│   │   ├── inventory/
│   │   └── accounting/
│   └── static/
│       ├── css/
│       ├── js/
│       └── img/
└── tests/
    └── test_routes.py
```

### Responsabilidad de los archivos principales

- `run.py`: crea la aplicación mediante `create_app()` y ejecuta el servidor de desarrollo.
- `requirements.txt`: declara las dependencias de Python.
- `src/__init__.py`: contiene la función fábrica `create_app`, configura Flask, registra el filtro de moneda y registra los Blueprints.
- `src/app.py`: punto de entrada alternativo que también crea y ejecuta la aplicación.
- `src/demo_data.py`: contiene listas de diccionarios con los registros ficticios utilizados por los controladores.
- `src/controllers/`: contiene los controladores organizados por funcionalidad. Cada módulo define un Blueprint y sus rutas.
- `src/templates/`: contiene las páginas HTML y componentes reutilizables escritos con Jinja2.
- `src/static/css/styles.css`: contiene los estilos propios de la interfaz.
- `src/static/js/app.js`: contiene interacciones generales del frontend.
- `tests/test_routes.py`: contiene pruebas automatizadas de rutas, filtro y paquetes de controladores.

## 4. Arquitectura y flujo de una solicitud

El proyecto utiliza una organización modular basada en **Blueprints de Flask** y el patrón de plantillas de Jinja2.

El flujo general es:

1. El usuario abre una URL en el navegador.
2. Flask recibe la solicitud y busca la ruta registrada.
3. El Blueprint del módulo correspondiente ejecuta la función del controlador.
4. El controlador obtiene datos de `src/demo_data.py` o prepara datos de demostración.
5. El controlador llama a `render_template()` y envía los datos a una plantilla.
6. Jinja2 combina la plantilla de la página con `layout.html`.
7. Flask devuelve el HTML al navegador, que carga además los archivos CSS y JavaScript.

### Application Factory

La función `create_app()` de `src/__init__.py` construye la instancia de Flask. Esta estrategia permite crear aplicaciones independientes para ejecución normal y pruebas.

Durante la inicialización:

- Se configura `SECRET_KEY`.
- Se registra el filtro Jinja2 `cop`.
- Se importan y registran los Blueprints de los módulos.

El filtro `cop` recibe un valor numérico y lo presenta con el símbolo `$` y separadores de miles mediante puntos. Si el valor no se puede convertir a número, devuelve `$ 0`.

### Blueprints

Un Blueprint agrupa rutas relacionadas con una funcionalidad. Por ejemplo, `products_bp` agrupa las rutas del catálogo de productos y utiliza el prefijo `/products`.

Los controladores contienen lógica de presentación y navegación; en esta versión no ejecutan consultas SQL ni guardan registros.

## 5. Módulos y rutas disponibles

| Módulo | URL principal | Función de la vista |
|---|---|---|
| Dashboard | `/` | Resumen de indicadores, facturas y compras |
| Productos | `/products/` | Listado, búsqueda y filtro por estado |
| Nuevo producto | `/products/new` | Formulario visual de producto |
| Editar producto | `/products/<id>/edit` | Formulario visual con el producto seleccionado |
| Categorías | `/categories/` | Listado y búsqueda visual de categorías |
| Clientes | `/customers/` | Listado y búsqueda de clientes |
| Nuevo cliente | `/customers/new` | Formulario visual de cliente |
| Editar cliente | `/customers/<id>/edit` | Formulario visual con el cliente seleccionado |
| Proveedores | `/suppliers/` | Listado de proveedores |
| Compras | `/purchases/` | Listado de órdenes de compra |
| Facturas | `/invoices/` | Listado de facturas |
| Nueva factura | `/invoices/new` | Formulario visual para preparar una factura |
| Inventario | `/inventory/` | Productos y movimientos de inventario de demostración |
| Finanzas | `/accounting/` | Listado de movimientos contables de demostración |

Los identificadores `<id>` de las rutas de edición son valores enteros. Las rutas de formularios muestran información, pero no persisten cambios.

## 6. Descripción de los controladores

Cada carpeta de `src/controllers/` representa un módulo funcional.

- `dashboard/home_controller.py`: calcula algunos indicadores a partir de los datos de demostración y muestra las últimas facturas y órdenes de compra.
- `products/products_controller.py`: muestra productos, aplica búsqueda por nombre, código de barras o marca y permite filtrar por estado activo/inactivo. También prepara el formulario de creación o edición.
- `categories/categories_controller.py`: prepara el listado de categorías de demostración.
- `clients/clients_controller.py`: muestra y filtra clientes por nombre, número de identificación o correo; prepara el formulario de creación o edición.
- `suppliers/suppliers_controller.py`: muestra el listado de proveedores.
- `purchases/purchases_controller.py`: muestra las órdenes de compra de demostración.
- `invoices/invoices_controller.py`: muestra las facturas y prepara el formulario de nueva factura con clientes y productos.
- `inventory/inventory_controller.py`: muestra movimientos y productos.
- `accounting/accounting_controller.py`: muestra los registros contables de demostración.

Cada paquete tiene un archivo `__init__.py` para identificarlo como paquete de Python. La lógica de las rutas está en el archivo `*_controller.py` correspondiente.

## 7. Datos de demostración

`src/demo_data.py` define constantes con listas de diccionarios:

- `PRODUCTS`: productos, códigos, precios, existencias y estado.
- `CUSTOMERS`: clientes y datos de contacto.
- `SUPPLIERS`: proveedores y datos tributarios/de contacto.
- `INVOICES`: facturas, clientes, fechas, totales, forma de pago y estado.
- `PURCHASES`: órdenes de compra, proveedores, fechas, totales y estado.
- `MOVEMENTS`: movimientos de inventario y sus referencias.
- `ENTRIES`: registros de ingresos y gastos.

Los controladores importan estas listas y las envían a las plantillas. Son datos estáticos en memoria: no se actualizan en una base de datos y pueden reiniciarse al reiniciar el servidor. El controlador de categorías define su lista de demostración directamente en `categories_controller.py`.

## 8. Plantillas Jinja2

`src/templates/layout.html` es la plantilla base. Define el documento HTML, idioma, metadatos, título, recursos externos, navegación, área principal, pie de página y carga de CSS/JavaScript.

Las páginas utilizan herencia de plantillas con:

- `{% extends "layout.html" %}` para heredar la estructura.
- `{% block content %}` para insertar el contenido de cada página.
- `{% block scripts %}` para añadir scripts específicos de una página, cuando se requiere.
- `{% include %}` para reutilizar componentes.

La carpeta `components/` contiene fragmentos compartidos, como barra lateral, barra superior, mensajes y tabla de facturas. Esto evita repetir el mismo HTML en cada página.

Los datos enviados por el controlador se muestran con expresiones Jinja2, por ejemplo `{{ customers }}` o dentro de ciclos `{% for ... %}`. Las condiciones `{% if ... %}` permiten mostrar estados o mensajes alternativos.

## 9. Archivos estáticos

### CSS

`src/static/css/styles.css` define la identidad visual de FactureAPP y complementa Bootstrap: colores, distribución, navegación, tablas, formularios y comportamiento adaptable.

### JavaScript

`src/static/js/app.js` ejecuta interacciones generales cuando el DOM está listo:

- Abre y cierra la barra lateral en pantallas pequeñas.
- Muestra mensajes de demostración al enviar formularios con la clase `demo-form`.
- Muestra mensajes para controles marcados con `data-demo-action`.
- Permite agregar filas al formulario de factura.
- Permite retirar filas, manteniendo al menos una línea de producto.

Estas interacciones son del lado del navegador. No representan una operación persistente ni validan reglas de negocio completas.

## 10. Instalación y ejecución en Windows con Git Bash

Abre Git Bash en la carpeta raíz del proyecto, donde se encuentran `run.py` y `requirements.txt`.

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activarlo en Git Bash

```bash
source .venv/Scripts/activate
```

Al activarse, el indicador de la terminal debe mostrar `(.venv)`.

### Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### Ejecutar la aplicación

```bash
python run.py
```

Abre en el navegador:

```text
http://127.0.0.1:5000
```

Para detener el servidor, vuelve a la terminal donde se está ejecutando y presiona `Ctrl + C`.

### Desactivar el entorno virtual

```bash
deactivate
```

## 11. Pruebas automatizadas

Las pruebas están en `tests/test_routes.py`. Utilizan el cliente de pruebas de Flask para realizar solicitudes sin abrir el navegador.

Instala pytest:

```bash
python -m pip install pytest
```

Ejecuta todas las pruebas:

```bash
python -m pytest -v
```

Las pruebas incluidas comprueban:

1. Que las páginas principales respondan con código HTTP 200.
2. Que el filtro de estado de productos responda correctamente.
3. Que los paquetes de controladores de clientes y productos puedan importarse y expongan sus Blueprints.

Una prueba exitosa indica que esas verificaciones pasaron; no demuestra que exista persistencia ni que todos los procesos de negocio estén implementados.

## 12. Configuración y seguridad

- La aplicación lee `SECRET_KEY` desde una variable de entorno. Si no está definida, utiliza una clave fija de demostración.
- La clave predeterminada solo es aceptable para desarrollo local. Antes de desplegar la aplicación debe definirse una clave secreta segura mediante variables de entorno.
- `debug=True` está habilitado en los puntos de ejecución para desarrollo. No debe utilizarse en producción.
- No se deben almacenar contraseñas, claves ni credenciales reales dentro del código fuente.
- Los datos del proyecto son ficticios y no deben reemplazarse por datos personales o comerciales reales sin implementar controles de seguridad y acceso.

## 13. Alcance pendiente para una versión conectada a MySQL

Para convertir esta demostración en una aplicación funcional se necesitará, como mínimo:

1. Configurar la conexión a MySQL mediante variables de entorno.
2. Definir modelos o una capa de acceso a datos para las entidades del esquema EER.
3. Crear servicios que contengan las reglas de negocio.
4. Actualizar los controladores para leer y guardar información mediante esos servicios.
5. Implementar validaciones del lado del servidor y manejo de errores.
6. Incorporar autenticación, autorización y gestión segura de sesiones.
7. Implementar operaciones reales de facturación, compras, inventario y contabilidad con transacciones.
8. Crear pruebas unitarias y de integración para las reglas de negocio y la base de datos.

El modelo EER de referencia contempla las entidades `users`, `customers`, `suppliers`, `product_categories`, `products`, `product_suppliers`, `purchase_orders`, `purchase_order_items`, `invoices`, `invoice_items`, `inventory_movements` y `accounting_entries`. La implementación de persistencia para esas entidades no forma parte de esta versión frontend.

## 14. Convenciones para mantener el código

- Mantener cada módulo dentro de su carpeta en `controllers/`.
- Usar nombres descriptivos para funciones, variables y rutas.
- Mantener las consultas y reglas de negocio fuera de las plantillas HTML.
- Reutilizar `layout.html` y los componentes compartidos.
- Evitar duplicar estilos o scripts que puedan centralizarse.
- Añadir pruebas cuando se incorpore una ruta o comportamiento nuevo.
- No crear capas vacías solo por completar una arquitectura; agregar modelos y servicios cuando se implemente la lógica que los necesite.


## 15. Módulo de usuarios (integración inicial con MySQL)

El módulo `users` se incorpora con una capa de controlador, servicio y acceso a datos:

```text
src/
├── controllers/users/users_controller.py
├── models/users/user_model.py
├── services/users/user_service.py
├── database/connection.py
└── templates/users/
    ├── index.html
    └── form.html
```

El módulo trabaja con la tabla `users` existente y utiliza los campos `id`, `username`, `password_hash`, `role`, `is_active`, `created_at` y `updated_at`. No ejecuta migraciones ni modifica el esquema.

- `database/connection.py`: construye la conexión a MySQL usando variables de entorno.
- `models/users/user_model.py`: ejecuta consultas parametrizadas sobre `users`.
- `services/users/user_service.py`: valida nombres, contraseñas, roles y genera hashes con Werkzeug.
- `controllers/users/users_controller.py`: recibe solicitudes HTTP y coordina el servicio y las vistas.
- `templates/users/`: presenta el listado y los formularios.

Los valores permitidos para `role` se consultan al propio ENUM de MySQL para evitar asumir nombres de roles. El hash se genera en Python mediante `generate_password_hash`; nunca se devuelve `password_hash` a las vistas.

### Configuración

1. Instala las dependencias actualizadas con `python -m pip install -r requirements.txt`.
2. Copia `.env.example` a `.env`.
3. Completa `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` y `DB_NAME`.
4. Comprueba que MySQL esté ejecutándose y que la tabla `users` exista.

### Protección pendiente

El controlador contiene una comprobación que exige `session["user_role"]` igual a `ADMIN_ROLE_VALUE`. El proyecto todavía no cuenta con inicio de sesión, por lo que las rutas del módulo responden con HTTP 403 hasta implementar autenticación y establecer esa sesión después de validar credenciales. No se debe quitar esta protección ni publicar el módulo accesible anónimamente.

Antes de usarlo en un entorno real también deben implementarse protección CSRF, limitación de intentos, auditoría de acciones y una política segura para evitar que se desactive la última cuenta administradora. El valor `ADMIN_ROLE_VALUE` debe coincidir con uno de los valores reales del ENUM `users.role`.


## Módulo de usuarios sin base de datos

La versión actual implementa una persistencia temporal en memoria mediante `InMemoryUserRepository`. El controlador HTTP depende de `UserService`; el servicio contiene validaciones y hashing de contraseñas; el repositorio se encarga del almacenamiento. Esta separación permite incorporar posteriormente un repositorio SQL que implemente las mismas operaciones, sin modificar las plantillas ni las rutas.

Operaciones disponibles: listado, búsqueda por usuario/rol, creación, edición de nombre y rol, activación/desactivación y cambio de contraseña. Los roles de demostración son `ADMIN` y `CASHIER`. Los usuarios iniciales se cargan al crear la aplicación y las modificaciones se pierden al reiniciar el proceso.

**Limitaciones:** no existe autenticación ni autorización real, no hay protección CSRF y el almacenamiento no es persistente. Las cuentas iniciales y sus contraseñas son solo para demostración. Antes de producción se debe implementar login, control de permisos, CSRF, gestión segura de secretos y persistencia SQL.

Para migrar a MySQL más adelante, se crea un adaptador `SqlUserRepository` con el mismo contrato que `InMemoryUserRepository` y se inyecta en `app.extensions["user_repository"]`. El servicio y las vistas permanecen desacoplados del motor de base de datos.
