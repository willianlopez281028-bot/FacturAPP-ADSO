"""Motor SQLAlchemy para conectarse a MySQL mediante variables de entorno."""
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_database_url() -> str:
    """Construye la URL de conexión sin almacenar credenciales en el código."""
    required = ("DB_USER", "DB_PASSWORD", "DB_HOST", "DB_NAME")
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        raise RuntimeError(
            "Faltan variables de entorno para MySQL: " + ", ".join(missing)
        )

    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    database = os.environ["DB_NAME"]

    from urllib.parse import quote_plus

    return (
        f"mysql+pymysql://{quote_plus(user)}:{quote_plus(password)}"
        f"@{host}:{port}/{database}?charset=utf8mb4"
    )


def create_database_engine() -> Engine:
    """Crea un motor de conexión; la conexión se abre cuando se ejecuta una consulta."""
    return create_engine(
        get_database_url(),
        pool_pre_ping=True,
        pool_recycle=3600,
    )
