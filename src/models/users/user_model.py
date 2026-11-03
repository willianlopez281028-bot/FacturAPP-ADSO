"""Entidad de dominio para una cuenta de usuario."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    password_hash: str
    role: str
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None
