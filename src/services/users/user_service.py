"""Reglas de negocio independientes del mecanismo de persistencia."""
from werkzeug.security import generate_password_hash


class UserValidationError(ValueError):
    """Error de validación controlado para formularios de usuarios."""


ALLOWED_ROLES = ("ADMIN", "CASHIER")


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def list_users(self, search=""):
        return self.repository.list(search)

    def get_user(self, user_id):
        return self.repository.get(user_id)

    def create_user(self, username, password, role):
        username = username.strip()
        self._validate_username(username)
        self._validate_password(password)
        self._validate_role(role)
        if self.repository.username_exists(username):
            raise UserValidationError("Ese nombre de usuario ya está registrado.")
        return self.repository.create({
            "username": username,
            "password_hash": generate_password_hash(password),
            "role": role,
        })

    def update_user(self, user_id, username, role, is_active):
        username = username.strip()
        self._validate_username(username)
        self._validate_role(role)
        if not self.repository.get(user_id):
            raise UserValidationError("El usuario que intentas modificar no existe.")
        if self.repository.username_exists(username, exclude_id=int(user_id)):
            raise UserValidationError("Ese nombre de usuario ya está registrado.")
        self.repository.update(user_id, username, role, is_active)

    def change_password(self, user_id, password):
        self._validate_password(password)
        if not self.repository.get(user_id):
            raise UserValidationError("El usuario no existe.")
        self.repository.update_password(user_id, generate_password_hash(password))

    @staticmethod
    def _validate_username(username):
        if not username:
            raise UserValidationError("El nombre de usuario es obligatorio.")
        if len(username) > 50:
            raise UserValidationError("El nombre de usuario admite máximo 50 caracteres.")

    @staticmethod
    def _validate_password(password):
        if len(password) < 8:
            raise UserValidationError("La contraseña debe tener al menos 8 caracteres.")

    @staticmethod
    def _validate_role(role):
        if role not in ALLOWED_ROLES:
            raise UserValidationError("Selecciona un rol válido.")
