import pytest
from unittest.mock import Mock, patch
from application.use_cases.get_product_detail import GetProductDetailUseCase
from application.use_cases.get_payment_methods import GetPaymentMethodsUseCase
from application.use_cases.get_recommended_products import GetRecommendedProductsUseCase
from application.use_cases.get_related_products import GetRelatedProductsUseCase
from domain.models.product import Product
from domain.models.payment_methods import PaymentMethods, Card
from domain.models.recommended_product import RecommendedProduct


class TestGetProductDetailUseCase:
    """Test cases for GetProductDetailUseCase"""
    
    def test_execute_success(self):
        """Test successful product retrieval"""
        # Arrange
        mock_repo = Mock()
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
            seller=Seller(
                name="Test Seller",
                is_official_store=True,
                sales=100,
                rating=4.5
            ),
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
        mock_repo.get_product_by_id.return_value = mock_product
        use_case = GetProductDetailUseCase(mock_repo)
        
        # Act
        result = use_case.execute("test-product")
        
        # Assert
        assert result == mock_product
        mock_repo.get_product_by_id.assert_called_once_with("test-product")
    
    def test_execute_not_found(self):
        """Test product not found scenario"""
        # Arrange
        mock_repo = Mock()
        mock_repo.get_product_by_id.return_value = None
        use_case = GetProductDetailUseCase(mock_repo)
        
        # Act
        result = use_case.execute("nonexistent-product")
        
        # Assert
        assert result is None
        mock_repo.get_product_by_id.assert_called_once_with("nonexistent-product")


class TestGetPaymentMethodsUseCase:
    """Test cases for GetPaymentMethodsUseCase"""
    
    def test_execute_success(self):
        """Test successful payment methods retrieval"""
        # Arrange
        mock_repo = Mock()
        from domain.models.payment_methods import PaymentMethods, Card
        mock_payment_methods = PaymentMethods(
            cuotasMessage="Test message",
            creditCards=[Card(name="Visa", logo="visa.png")],
            debitCards=[Card(name="Mastercard", logo="master.png")],
            cash=[Card(name="Cash", logo="cash.png")]
        )
        mock_repo.get_payment_methods.return_value = mock_payment_methods
        use_case = GetPaymentMethodsUseCase(mock_repo)
        
        # Act
        result = use_case.execute()
        
        # Assert
        assert result == mock_payment_methods
        mock_repo.get_payment_methods.assert_called_once()
    
    def test_execute_with_exception(self):
        """Test payment methods retrieval with repository exception"""
        # Arrange
        mock_repo = Mock()
        mock_repo.get_payment_methods.side_effect = Exception("Database error")
        use_case = GetPaymentMethodsUseCase(mock_repo)
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            use_case.execute()
        assert str(exc_info.value) == "Database error"
        mock_repo.get_payment_methods.assert_called_once()


class TestGetRecommendedProductsUseCase:
    """Test cases for GetRecommendedProductsUseCase"""
    
    def test_execute_success(self):
        """Test successful recommended products retrieval"""
        # Arrange
        mock_repo = Mock()
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
        mock_repo.get_all_recommended_products.return_value = mock_products
        use_case = GetRecommendedProductsUseCase(mock_repo)
        
        # Act
        result = use_case.execute()
        
        # Assert
        assert result == mock_products
        mock_repo.get_all_recommended_products.assert_called_once()
    
    def test_execute_empty_list(self):
        """Test empty recommended products list"""
        # Arrange
        mock_repo = Mock()
        mock_repo.get_all_recommended_products.return_value = []
        use_case = GetRecommendedProductsUseCase(mock_repo)
        
        # Act
        result = use_case.execute()
        
        # Assert
        assert result == []
        mock_repo.get_all_recommended_products.assert_called_once()


class TestGetRelatedProductsUseCase:
    """Test cases for GetRelatedProductsUseCase"""
    
    def test_execute_success(self):
        """Test successful related products retrieval"""
        # Arrange
        mock_repo = Mock()
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
        mock_repo.get_all_recommended_products.return_value = mock_products
        use_case = GetRelatedProductsUseCase(mock_repo)
        
        # Act
        result = use_case.execute()
        
        # Assert
        assert result == mock_products
        mock_repo.get_all_recommended_products.assert_called_once()
    
    def test_execute_empty_list(self):
        """Test empty related products list"""
        # Arrange
        mock_repo = Mock()
        mock_repo.get_all_recommended_products.return_value = []
        use_case = GetRelatedProductsUseCase(mock_repo)
        
        # Act
        result = use_case.execute()
        
        # Assert
        assert result == []
        mock_repo.get_all_recommended_products.assert_called_once()
