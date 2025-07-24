import pytest
from fastapi.testclient import TestClient
from api.app import app
from api.security import create_jwt_token, verify_jwt_token
from datetime import timedelta
from unittest.mock import Mock, patch
import jwt


client = TestClient(app)

# Authentication Tests
def test_login_success():
    """Test successful login with valid credentials"""
    response = client.post("/login", data={
        "username": "admin",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    """Test login failure with invalid credentials"""
    response = client.post("/login", data={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_missing_username():
    """Test login with missing username"""
    response = client.post("/login", data={
        "password": "password"
    })
    assert response.status_code == 422

def test_login_missing_password():
    """Test login with missing password"""
    response = client.post("/login", data={
        "username": "admin"
    })
    assert response.status_code == 422

# Product Tests
def test_get_product_success():
    """Test getting a product successfully"""
    response = client.get("/api/items/samsung-a55-5g")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "samsung-a55-5g"
    assert "title" in data
    assert "price" in data

def test_get_product_not_found():
    """Test getting a non-existent product"""
    response = client.get("/api/items/nonexistent-product-id")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

# Payment Methods Tests  
def test_get_payment_methods():
    """Test getting payment methods"""
    response = client.get("/api/payment-methods")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "cuotasMessage" in data
    assert "creditCards" in data
    assert "debitCards" in data
    assert "cash" in data

# Recommended Products Tests
def test_get_recommended_products():
    """Test getting recommended products"""
    response = client.get("/api/recommended-products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# Related Products Tests
def test_get_related_products():
    """Test getting related products"""
    response = client.get("/api/related-products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# Security/JWT Tests
def test_create_jwt_token():
    """Test JWT token creation"""
    token = create_jwt_token({"sub": "testuser"})
    assert isinstance(token, str)
    assert len(token) > 0

def test_verify_jwt_token_valid():
    """Test JWT token verification with valid token"""
    token = create_jwt_token({"sub": "testuser"})
    payload = verify_jwt_token(token)
    assert payload["sub"] == "testuser"

def test_verify_jwt_token_expired():
    """Test JWT token verification with expired token"""
    expired_token = create_jwt_token({"sub": "testuser"}, expires_delta=timedelta(seconds=-10))
    with pytest.raises(Exception) as exc_info:
        verify_jwt_token(expired_token)
    assert "Token expired" in str(exc_info.value)

def test_verify_jwt_token_invalid():
    """Test JWT token verification with invalid token"""
    invalid_token = "invalid.token.here"
    with pytest.raises(Exception) as exc_info:
        verify_jwt_token(invalid_token)
    assert "Invalid token" in str(exc_info.value)

def test_verify_jwt_token_malformed():
    """Test JWT token verification with malformed token"""
    malformed_token = "not-a-jwt-token"
    with pytest.raises(Exception) as exc_info:
        verify_jwt_token(malformed_token)
    assert "Invalid token" in str(exc_info.value)
