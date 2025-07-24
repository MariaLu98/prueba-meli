import pytest
import json
from unittest.mock import patch, mock_open
from pathlib import Path
from infrastructure.repositories.json_product_repository import JSONProductRepository
from infrastructure.repositories.json_payment_methods_repository import JSONPaymentMethodsRepository
from infrastructure.repositories.json_recommended_products_repository import JSONRecommendedProductsRepository
from infrastructure.repositories.json_related_products_repository import JSONRelatedProductsRepository


class TestRepositoryEdgeCases:
    """Test edge cases for repository implementations"""
    
    @patch('pathlib.Path.open')
    def test_product_repository_permission_error(self, mock_open_method):
        """Test product repository with permission error"""
        mock_open_method.side_effect = PermissionError("Permission denied")
        repo = JSONProductRepository("test_data.json")
        
        with pytest.raises(PermissionError):
            repo.get_product_by_id("any-product")
    
    @patch('pathlib.Path.open')
    def test_payment_methods_repository_permission_error(self, mock_open_method):
        """Test payment methods repository with permission error"""
        mock_open_method.side_effect = PermissionError("Permission denied")
        repo = JSONPaymentMethodsRepository("test_data.json")
        
        with pytest.raises(PermissionError):
            repo.get_payment_methods()
    
    @patch('pathlib.Path.open')
    def test_recommended_products_repository_permission_error(self, mock_open_method):
        """Test recommended products repository with permission error"""
        mock_open_method.side_effect = PermissionError("Permission denied")
        repo = JSONRecommendedProductsRepository("test_data.json")
        
        with pytest.raises(PermissionError):
            repo.get_all_recommended_products()
    
    @patch('pathlib.Path.open')
    def test_related_products_repository_permission_error(self, mock_open_method):
        """Test related products repository with permission error"""
        mock_open_method.side_effect = PermissionError("Permission denied")
        repo = JSONRelatedProductsRepository("test_data.json")
        
        with pytest.raises(PermissionError):
            repo.get_all_recommended_products()
    
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[{"id": "test", "title": "Test", "price": 100, "discount_percentage": 10, "installments": "3 cuotas", "images": ["img.jpg"], "color": "Red", "stock": 5, "description": "Test", "seller": {"name": "Test", "is_official_store": true, "sales": 100, "rating": 4.5}, "payment_methods": ["credit"], "features": {"screen_size": "6.5 inches", "internal_memory": "256GB", "front_camera": "32MP", "rear_camera": "108MP", "nfc": true, "unlock": "Face unlock"}}]')
    def test_product_repository_large_dataset(self, mock_file):
        """Test product repository with large dataset"""
        repo = JSONProductRepository("test_data.json")
        
        # Test finding first item
        product = repo.get_product_by_id("test")
        assert product is not None
        assert product.id == "test"
        
        # Test not finding item in large dataset
        product = repo.get_product_by_id("nonexistent")
        assert product is None
    
    def test_repository_initialization(self):
        """Test repository initialization with different paths"""
        # Test with string path
        repo1 = JSONProductRepository("test.json")
        assert repo1.data_path == Path("test.json")
        
        # Test with Path object
        repo2 = JSONProductRepository(Path("test.json"))
        assert repo2.data_path == Path("test.json")
        
        # Test with absolute path
        abs_path = Path("C:/absolute/path/test.json")
        repo3 = JSONProductRepository(abs_path)
        assert repo3.data_path == abs_path
