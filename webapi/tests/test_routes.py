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
from domain.models.payment_methods import PaymentMethods, Card
from domain.models.recommended_product import RecommendedProduct


class TestAuthRoutes:
    """Test cases for authentication routes"""
    
    def test_login_route_integration(self):
        """Test login route integration"""
        app = FastAPI()
        app.include_router(auth_router)
        client = TestClient(app)
        
        # Test successful login
        response = client.post("/login", data={
            "username": "admin",
            "password": "password"
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        
        # Test failed login
        response = client.post("/login", data={
            "username": "wrong",
            "password": "wrong"
        })
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid credentials"


class TestProductRoutes:
    """Test cases for product routes"""
    
    def test_get_product_route_success(self):
        """Test successful product retrieval route"""
        # Mock use case
        mock_use_case = Mock()
        from domain.models.seller import Seller
        from domain.models.features import Features
        mock_product = Product(
            id="test-product",
            title="Test Product",
            price=100,
            discount_percentage=10,
            installments="3 cuotas",
            images=["img1.jpg"],
            color="Red",
            stock=5,
            description="Test description",
            seller=Seller(name="Test Seller", is_official_store=True, sales=100, rating=4.5),
            payment_methods=["credit", "debit"],
            features=Features(
                screen_size="6.5 inches",
                internal_memory="256GB",
                front_camera="32MP",
                rear_camera="108MP",
                nfc=True,
                unlock="Face unlock"
            )
        )
        mock_use_case.execute.return_value = mock_product
        
        # Create app with router
        app = FastAPI()
        router = get_product_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/items/test-product")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "test-product"
        assert data["title"] == "Test Product"
        mock_use_case.execute.assert_called_once_with("test-product")
    
    def test_get_product_route_not_found(self):
        """Test product not found route"""
        # Mock use case
        mock_use_case = Mock()
        mock_use_case.execute.return_value = None
        
        # Create app with router
        app = FastAPI()
        router = get_product_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/items/nonexistent")
        assert response.status_code == 404
        assert response.json()["detail"] == "Product not found"
        mock_use_case.execute.assert_called_once_with("nonexistent")


class TestPaymentMethodsRoutes:
    """Test cases for payment methods routes"""
    
    def test_get_payment_methods_route_success(self):
        """Test successful payment methods retrieval route"""
        # Mock use case
        mock_use_case = Mock()
        from domain.models.payment_methods import PaymentMethods, Card
        mock_methods = PaymentMethods(
            cuotasMessage="Test message",
            creditCards=[Card(name="Visa", logo="visa.png")],
            debitCards=[Card(name="Mastercard", logo="master.png")],
            cash=[Card(name="Cash", logo="cash.png")]
        )
        mock_use_case.execute.return_value = mock_methods
        
        # Create app with router
        app = FastAPI()
        router = get_payment_methods_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/payment-methods")
        assert response.status_code == 200
        data = response.json()
        assert data["cuotasMessage"] == "Test message"
        assert len(data["creditCards"]) == 1
        assert data["creditCards"][0]["name"] == "Visa"
        mock_use_case.execute.assert_called_once()
    
    def test_get_payment_methods_route_exception(self):
        """Test payment methods route with use case exception"""
        # Mock use case that raises exception
        mock_use_case = Mock()
        mock_use_case.execute.side_effect = Exception("Database error")
        
        # Create app with router
        app = FastAPI()
        router = get_payment_methods_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint - FastAPI returns 500 for unhandled exceptions
        with pytest.raises(Exception):
            response = client.get("/api/payment-methods")
        
        mock_use_case.execute.assert_called_once()


class TestRecommendedProductsRoutes:
    """Test cases for recommended products routes"""
    
    def test_get_recommended_products_route_success(self):
        """Test successful recommended products retrieval route"""
        # Mock use case
        mock_use_case = Mock()
        mock_products = [
            RecommendedProduct(
                id="rec1", 
                title="Recommended 1", 
                image="img1.jpg",
                priceOld=100,
                priceNew=80,
                discount=20,
                installments="3 cuotas"
            ),
            RecommendedProduct(
                id="rec2", 
                title="Recommended 2", 
                image="img2.jpg",
                priceOld=150,
                priceNew=120,
                discount=20,
                installments="6 cuotas"
            )
        ]
        mock_use_case.execute.return_value = mock_products
        
        # Create app with router
        app = FastAPI()
        router = get_recommended_products_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/recommended-products")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert data[0]["id"] == "rec1"
        assert data[1]["id"] == "rec2"
        mock_use_case.execute.assert_called_once()
    
    def test_get_recommended_products_route_empty(self):
        """Test empty recommended products route"""
        # Mock use case
        mock_use_case = Mock()
        mock_use_case.execute.return_value = []
        
        # Create app with router
        app = FastAPI()
        router = get_recommended_products_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/recommended-products")
        assert response.status_code == 200
        data = response.json()
        assert data == []
        mock_use_case.execute.assert_called_once()


class TestRelatedProductsRoutes:
    """Test cases for related products routes"""
    
    def test_get_related_products_route_success(self):
        """Test successful related products retrieval route"""
        # Mock use case
        mock_use_case = Mock()
        mock_products = [
            RecommendedProduct(
                id="rel1", 
                title="Related 1", 
                image="img1.jpg",
                priceOld=50,
                priceNew=40,
                discount=20,
                installments="3 cuotas"
            ),
            RecommendedProduct(
                id="rel2", 
                title="Related 2", 
                image="img2.jpg",
                priceOld=70,
                priceNew=56,
                discount=20,
                installments="6 cuotas"
            )
        ]
        mock_use_case.execute.return_value = mock_products
        
        # Create app with router
        app = FastAPI()
        router = get_related_products_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/related-products")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert data[0]["id"] == "rel1"
        assert data[1]["id"] == "rel2"
        mock_use_case.execute.assert_called_once()
    
    def test_get_related_products_route_empty(self):
        """Test empty related products route"""
        # Mock use case
        mock_use_case = Mock()
        mock_use_case.execute.return_value = []
        
        # Create app with router
        app = FastAPI()
        router = get_related_products_router(mock_use_case)
        app.include_router(router)
        client = TestClient(app)
        
        # Test the endpoint
        response = client.get("/api/related-products")
        assert response.status_code == 200
        data = response.json()
        assert data == []
        mock_use_case.execute.assert_called_once()
