import pytest
import json
import os
from unittest.mock import Mock, patch, mock_open, MagicMock
from pathlib import Path
from infrastructure.repositories.json_product_repository import JSONProductRepository
from infrastructure.repositories.json_payment_methods_repository import JSONPaymentMethodsRepository  
from infrastructure.repositories.json_recommended_products_repository import JSONRecommendedProductsRepository
from infrastructure.repositories.json_related_products_repository import JSONRelatedProductsRepository


class TestJSONProductRepository:
    """Test cases for JSONProductRepository"""
    
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[{"id": "test-product", "title": "Test Product", "price": 100, "discount_percentage": 10, "installments": "3 cuotas", "images": ["img1.jpg"], "color": "Red", "stock": 5, "description": "Test description", "seller": {"name": "Test Seller", "is_official_store": true, "sales": 100, "rating": 4.5}, "payment_methods": ["credit", "debit"], "features": {"screen_size": "6.5 inches", "internal_memory": "256GB", "front_camera": "32MP", "rear_camera": "108MP", "nfc": true, "unlock": "Face unlock"}}]')
    def test_get_product_by_id_success(self, mock_file):
        """Test successful product retrieval by ID"""
        repo = JSONProductRepository("test_data.json")
        product = repo.get_product_by_id("test-product")
        
        assert product is not None
        assert product.id == "test-product"
        assert product.title == "Test Product"
        assert product.price == 100
        
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[{"id": "other-product", "title": "Other Product", "price": 200, "discount_percentage": 15, "installments": "6 cuotas", "images": ["img2.jpg"], "color": "Blue", "stock": 10, "description": "Other description", "seller": {"name": "Other Seller", "is_official_store": false, "sales": 50, "rating": 4.0}, "payment_methods": ["cash"], "features": {"screen_size": "6.1 inches", "internal_memory": "128GB", "front_camera": "12MP", "rear_camera": "48MP", "nfc": false, "unlock": "Fingerprint"}}]')
    def test_get_product_by_id_not_found(self, mock_file):
        """Test product not found scenario"""
        repo = JSONProductRepository("test_data.json")
        product = repo.get_product_by_id("nonexistent-product")
        
        assert product is None
        
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[]')
    def test_get_product_by_id_empty_file(self, mock_file):
        """Test product retrieval from empty file"""
        repo = JSONProductRepository("test_data.json")
        product = repo.get_product_by_id("any-product")
        
        assert product is None
        
    @patch('pathlib.Path.open')
    def test_get_product_by_id_file_not_found(self, mock_open_method):
        """Test product retrieval when file doesn't exist"""
        mock_open_method.side_effect = FileNotFoundError("File not found")
        repo = JSONProductRepository("test_data.json")
        
        with pytest.raises(FileNotFoundError):
            repo.get_product_by_id("any-product")
    
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='invalid json')
    def test_get_product_by_id_invalid_json(self, mock_file):
        """Test product retrieval with invalid JSON"""
        repo = JSONProductRepository("test_data.json")
        with pytest.raises(json.JSONDecodeError):
            repo.get_product_by_id("any-product")


class TestJSONPaymentMethodsRepository:
    """Test cases for JSONPaymentMethodsRepository"""
    
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='{"cuotasMessage": "Test message", "creditCards": [{"name": "Visa", "logo": "visa.png"}], "debitCards": [{"name": "Mastercard", "logo": "master.png"}], "cash": [{"name": "Cash", "logo": "cash.png"}]}')
    def test_get_payment_methods_success(self, mock_file):
        """Test successful payment methods retrieval"""
        repo = JSONPaymentMethodsRepository("test_data.json")
        methods = repo.get_payment_methods()
        
        assert methods is not None
        assert methods.cuotasMessage == "Test message"
        assert len(methods.creditCards) == 1
        assert methods.creditCards[0].name == "Visa"
        
    @patch('pathlib.Path.open')
    def test_get_payment_methods_file_not_found(self, mock_open_method):
        """Test payment methods retrieval when file doesn't exist"""
        mock_open_method.side_effect = FileNotFoundError("File not found")
        repo = JSONPaymentMethodsRepository("test_data.json")
        
        with pytest.raises(FileNotFoundError):
            repo.get_payment_methods()
            
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='invalid json')
    def test_get_payment_methods_invalid_json(self, mock_file):
        """Test payment methods retrieval with invalid JSON"""
        repo = JSONPaymentMethodsRepository("test_data.json")
        with pytest.raises(json.JSONDecodeError):
            repo.get_payment_methods()


class TestJSONRecommendedProductsRepository:
    """Test cases for JSONRecommendedProductsRepository"""
    
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[{"id": "rec1", "title": "Recommended Product 1", "image": "rec1.jpg", "priceOld": 200, "priceNew": 150, "discount": 20, "installments": "6 cuotas"}]')
    def test_get_all_recommended_products_success(self, mock_file):
        """Test successful recommended products retrieval"""
        repo = JSONRecommendedProductsRepository("test_data.json")
        products = repo.get_all_recommended_products()
        
        assert products is not None
        assert len(products) == 1
        assert products[0].id == "rec1"
        assert products[0].title == "Recommended Product 1"
        
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[]')
    def test_get_all_recommended_products_empty_file(self, mock_file):
        """Test recommended products retrieval from empty file"""
        repo = JSONRecommendedProductsRepository("test_data.json")
        products = repo.get_all_recommended_products()
        
        assert products is not None
        assert len(products) == 0
        
    @patch('pathlib.Path.open')
    def test_get_all_recommended_products_file_not_found(self, mock_open_method):
        """Test recommended products retrieval when file doesn't exist"""
        mock_open_method.side_effect = FileNotFoundError("File not found")
        repo = JSONRecommendedProductsRepository("test_data.json")
        
        with pytest.raises(FileNotFoundError):
            repo.get_all_recommended_products()
            
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='invalid json')
    def test_get_all_recommended_products_invalid_json(self, mock_file):
        """Test recommended products retrieval with invalid JSON"""
        repo = JSONRecommendedProductsRepository("test_data.json")
        with pytest.raises(json.JSONDecodeError):
            repo.get_all_recommended_products()


class TestJSONRelatedProductsRepository:
    """Test cases for JSONRelatedProductsRepository"""
    
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[{"id": "rel1", "title": "Related Product 1", "image": "rel1.jpg", "priceOld": 140, "priceNew": 120, "discount": 20, "installments": "6 cuotas"}]')
    def test_get_all_recommended_products_success(self, mock_file):
        """Test successful related products retrieval"""
        repo = JSONRelatedProductsRepository("test_data.json")
        products = repo.get_all_recommended_products()
        
        assert products is not None
        assert len(products) == 1
        assert products[0].id == "rel1"
        assert products[0].title == "Related Product 1"
        
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='[]')
    def test_get_all_recommended_products_empty_file(self, mock_file):
        """Test related products retrieval from empty file"""
        repo = JSONRelatedProductsRepository("test_data.json")
        products = repo.get_all_recommended_products()
        
        assert products is not None
        assert len(products) == 0
        
    @patch('pathlib.Path.open')
    def test_get_all_recommended_products_file_not_found(self, mock_open_method):
        """Test related products retrieval when file doesn't exist"""
        mock_open_method.side_effect = FileNotFoundError("File not found")
        repo = JSONRelatedProductsRepository("test_data.json")
        
        with pytest.raises(FileNotFoundError):
            repo.get_all_recommended_products()
            
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='invalid json')
    def test_get_all_recommended_products_invalid_json(self, mock_file):
        """Test related products retrieval with invalid JSON"""
        repo = JSONRelatedProductsRepository("test_data.json")
        with pytest.raises(json.JSONDecodeError):
            repo.get_all_recommended_products()
