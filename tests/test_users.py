"""Pruebas del CRUD de usuarios sin conexión a base de datos."""
import pytest
from src import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_users_list_loads_without_database(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert b'admin' in response.data


def test_create_user(client):
    response = client.post('/users/new', data={
        'username': 'nuevo', 'password': 'Password123',
        'password_confirmation': 'Password123', 'role': 'CASHIER',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'nuevo' in response.data


def test_duplicate_username_is_rejected(client):
    response = client.post('/users/new', data={
        'username': 'admin', 'password': 'Password123',
        'password_confirmation': 'Password123', 'role': 'ADMIN',
    }, follow_redirects=True)
    assert b'ya est' in response.data


def test_edit_user(client):
    response = client.post('/users/2/edit', data={
        'username': 'cajero_editado', 'role': 'CASHIER', 'is_active': '1',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'cajero_editado' in response.data


def test_change_password(client):
    response = client.post('/users/1/password', data={
        'password': 'NuevaClave123', 'password_confirmation': 'NuevaClave123',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Contrase' in response.data
