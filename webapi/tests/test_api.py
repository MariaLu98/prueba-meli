import pytest
from fastapi.testclient import TestClient
from api.app import app
from api.security import create_jwt_token
from datetime import timedelta


client = TestClient(app)

def test_login_success():
    response = client.post("/login", data={
        "username": "admin",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    response = client.post("/login", data={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401

def test_get_product_unauthorized():
    response = client.get("/items/samsung-a55-5g")
    assert response.status_code == 403 or response.status_code == 401

def test_get_product_authorized():
    # Primero obtenemos un token válido
    login_resp = client.post("/login", data={
        "username": "admin",
        "password": "password"
    })
    token = login_resp.json()["access_token"]

    # Lo usamos en el header Authorization
    response = client.get(
        "/items/samsung-a55-5g",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "samsung-a55-5g"

def test_login_success():
    response = client.post("/login", data={
        "username": "admin",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    response = client.post("/login", data={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401

def test_get_product_unauthorized():
    response = client.get("/items/samsung-a55-5g")
    assert response.status_code in (401, 403)

def test_get_product_authorized():
    login_resp = client.post("/login", data={
        "username": "admin",
        "password": "password"
    })
    token = login_resp.json()["access_token"]
    response = client.get(
        "/items/samsung-a55-5g",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "samsung-a55-5g"

def test_get_product_not_found():
    login_resp = client.post("/login", data={
        "username": "admin",
        "password": "password"
    })
    token = login_resp.json()["access_token"]

    response = client.get(
        "/items/nonexistent-product-id",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_get_product_invalid_token():
    fake_token = "this.is.a.bad.token"
    response = client.get(
        "/items/samsung-a55-5g",
        headers={"Authorization": f"Bearer {fake_token}"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid token"

def test_get_product_expired_token():
    expired_token = create_jwt_token({"sub": "admin"}, expires_delta=timedelta(seconds=-10))
    response = client.get(
        "/items/samsung-a55-5g",
        headers={"Authorization": f"Bearer {expired_token}"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Token expired"
