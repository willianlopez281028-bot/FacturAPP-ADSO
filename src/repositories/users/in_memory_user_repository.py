"""Almacenamiento temporal en memoria. Se podrá sustituir por un repositorio SQL."""
from datetime import datetime
from threading import RLock

from src.models.users.user_model import User


class InMemoryUserRepository:
    def __init__(self, initial_users=None):
        self._lock = RLock()
        self._users = {}
        self._next_id = 1
        for user_data in initial_users or []:
            self.create(user_data)

    def list(self, search=""):
        term = search.strip().lower()
        with self._lock:
            users = list(self._users.values())
            if term:
                users = [u for u in users if term in u.username.lower() or term in u.role.lower()]
            return sorted(users, key=lambda user: user.id, reverse=True)

    def get(self, user_id):
        with self._lock:
            return self._users.get(int(user_id))

    def username_exists(self, username, exclude_id=None):
        normalized = username.casefold()
        with self._lock:
            return any(u.username.casefold() == normalized and u.id != exclude_id
                       for u in self._users.values())

    def create(self, data):
        now = datetime.now()
        with self._lock:
            user = User(
                id=self._next_id,
                username=data["username"].strip(),
                password_hash=data["password_hash"],
                role=data["role"],
                is_active=True,
                created_at=now,
                updated_at=now,
            )
            self._users[user.id] = user
            self._next_id += 1
            return user

    def update(self, user_id, username, role, is_active):
        with self._lock:
            user = self._users.get(int(user_id))
            if not user:
                return None
            user.username = username.strip()
            user.role = role
            user.is_active = bool(is_active)
            user.updated_at = datetime.now()
            return user

    def update_password(self, user_id, password_hash):
        with self._lock:
            user = self._users.get(int(user_id))
            if not user:
                return None
            user.password_hash = password_hash
            user.updated_at = datetime.now()
            return user
