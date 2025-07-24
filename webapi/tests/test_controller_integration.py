import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import Mock
from api.routes.auth_routes import router as auth_router
from api.routes.product_routes import get_product_router
from api.routes.payment_methods_routes import get_payment_methods_router
from api.routes.recommended_products_routes import get_recommended_products_router
from api.routes.related_products_routes import get_related_products_router
from domain.models.product import Product
from domain.models.seller import Seller
from domain.models.features import Features
from domain.models.payment_methods import PaymentMethods, Card
from domain.models.recommended_product import RecommendedProduct


class TestControllerIntegration:
    """Test de integración para verificar que todos los controladores funcionen correctamente"""

    def test_auth_controller_integration(self):
        """Verificar que el controlador de autenticación funciona correctamente"""
        app = FastAPI()
        app.include_router(auth_router)
        client = TestClient(app)
        
        # Test login exitoso
        response = client.post("/login", data={
            "username": "admin",
            "password": "password"
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        
        # Test login fallido
        response = client.post("/login", data={
            "username": "wrong",
            "password": "wrong"
        })
        assert response.status_code == 401

    def test_product_controller_integration(self):
        """Verificar que el controlador de productos funciona correctamente"""
        # Mock del use case
        mock_use_case = Mock()
        
        # Crear producto de prueba
        seller = Seller(name="Test Seller", is_official_store=True, sales=100, rating=4.5)
        features = Features(
            screen_size="6.5 inches",
            internal_memory="256GB", 
            front_camera="32MP",
            rear_camera="108MP",
            nfc=True,
            unlock="Face unlock"
        )
        test_product = Product(
            id="test-product",
            title="Test Product",
            price=100,
            discount_percentage=10,
            installments="3 cuotas",
            images=["img1.jpg"],
            color="Red",
            stock=5,
            description="Test description",
            seller=seller,
            payment_methods=["credit", "debit"],
            features=features
        )
        
        mock_use_case.execute.return_value = test_product
        
        app = FastAPI()
        router = get_product_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test obtener producto existente
        response = client.get("/api/items/test-product")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "test-product"
        assert data["title"] == "Test Product"
        
        # Test producto no encontrado
        mock_use_case.execute.return_value = None
        response = client.get("/api/items/nonexistent")
        assert response.status_code == 404

    def test_payment_methods_controller_integration(self):
        """Verificar que el controlador de métodos de pago funciona correctamente"""
        # Mock del use case
        mock_use_case = Mock()
        
        # Crear métodos de pago de prueba
        credit_card = Card(name="Visa", logo="visa.png")
        debit_card = Card(name="Mastercard", logo="master.png")
        cash = Card(name="Cash", logo="cash.png")
        
        test_payment_methods = PaymentMethods(
            cuotasMessage="Test message",
            creditCards=[credit_card],
            debitCards=[debit_card],
            cash=[cash]
        )
        
        mock_use_case.execute.return_value = test_payment_methods
        
        app = FastAPI()
        router = get_payment_methods_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test obtener métodos de pago
        response = client.get("/api/payment-methods")
        assert response.status_code == 200
        data = response.json()
        assert data["cuotasMessage"] == "Test message"
        assert len(data["creditCards"]) == 1
        assert data["creditCards"][0]["name"] == "Visa"

    def test_recommended_products_controller_integration(self):
        """Verificar que el controlador de productos recomendados funciona correctamente"""
        # Mock del use case
        mock_use_case = Mock()
        
        # Crear productos recomendados de prueba
        recommended_product = RecommendedProduct(
            id="rec1",
            title="Recommended Product",
            image="rec1.jpg",
            priceOld=200,
            priceNew=150,
            discount=25,
            installments="6 cuotas"
        )
        
        mock_use_case.execute.return_value = [recommended_product]
        
        app = FastAPI()
        router = get_recommended_products_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test obtener productos recomendados
        response = client.get("/api/recommended-products")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["id"] == "rec1"
        assert data[0]["title"] == "Recommended Product"

    def test_related_products_controller_integration(self):
        """Verificar que el controlador de productos relacionados funciona correctamente"""
        # Mock del use case
        mock_use_case = Mock()
        
        # Crear productos relacionados de prueba
        related_product = RecommendedProduct(
            id="rel1",
            title="Related Product",
            image="rel1.jpg",
            priceOld=180,
            priceNew=140,
            discount=22,
            installments="3 cuotas"
        )
        
        mock_use_case.execute.return_value = [related_product]
        
        app = FastAPI()
        router = get_related_products_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test obtener productos relacionados
        response = client.get("/api/related-products")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["id"] == "rel1"
        assert data[0]["title"] == "Related Product"

    def test_all_controllers_error_handling(self):
        """Verificar que todos los controladores manejen errores correctamente"""
        # Test controlador de productos con excepción
        mock_use_case = Mock()
        mock_use_case.execute.side_effect = Exception("Database error")
        
        app = FastAPI()
        router = get_product_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Este debería generar un error 500 (internal server error)
        with pytest.raises(Exception):
            response = client.get("/api/items/any-product")
