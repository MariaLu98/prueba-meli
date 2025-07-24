import pytest
from domain.ports.product_repository import ProductRepository
from domain.ports.payment_methods_repository import PaymentMethodsRepository  
from domain.ports.recommended_products_repository import RecommendedProductsRepository


class TestAbstractPorts:
    """Test cases for abstract port interfaces"""
    
    def test_product_repository_abstract_method(self):
        """Test that ProductRepository is properly abstract"""
        with pytest.raises(TypeError):
            ProductRepository()
    
    def test_payment_methods_repository_abstract_method(self):
        """Test that PaymentMethodsRepository is properly abstract"""
        with pytest.raises(TypeError):
            PaymentMethodsRepository()
    
    def test_recommended_products_repository_abstract_method(self):
        """Test that RecommendedProductsRepository is properly abstract"""
        with pytest.raises(TypeError):
            RecommendedProductsRepository()


class TestRepositoryConcreteImplementation:
    """Test concrete repository method implementations"""
    
    def test_repository_inheritance(self):
        """Test that concrete repositories properly inherit from abstract bases"""
        from infrastructure.repositories.json_product_repository import JSONProductRepository
        from infrastructure.repositories.json_payment_methods_repository import JSONPaymentMethodsRepository
        from infrastructure.repositories.json_recommended_products_repository import JSONRecommendedProductsRepository
        
        # Test inheritance
        assert issubclass(JSONProductRepository, ProductRepository)
        assert issubclass(JSONPaymentMethodsRepository, PaymentMethodsRepository)
        assert issubclass(JSONRecommendedProductsRepository, RecommendedProductsRepository)
        
        # Test instantiation works
        product_repo = JSONProductRepository("test.json")
        payment_repo = JSONPaymentMethodsRepository("test.json")
        recommended_repo = JSONRecommendedProductsRepository("test.json")
        
        assert isinstance(product_repo, ProductRepository)
        assert isinstance(payment_repo, PaymentMethodsRepository)
        assert isinstance(recommended_repo, RecommendedProductsRepository)
