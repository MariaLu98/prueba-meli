import pytest
from domain.models.product import Product
from domain.models.payment_methods import PaymentMethods, Card
from domain.models.recommended_product import RecommendedProduct
from domain.models.seller import Seller
from domain.models.features import Features


class TestProduct:
    """Test cases for Product domain model"""
    
    def test_product_creation(self):
        """Test Product creation with all fields"""
        seller_data = Seller(
            name="Test Seller",
            is_official_store=True,
            sales=1000,
            rating=4.5
        )
        features_data = Features(
            screen_size="6.5 inches",
            internal_memory="256GB",
            front_camera="32MP",
            rear_camera="48MP",
            nfc=True,
            unlock="Face unlock"
        )
        
        product = Product(
            id="test-product",
            title="Test Product",
            price=99.99,
            discount_percentage=10,
            installments="3 cuotas sin interés",
            images=["image1.jpg", "image2.jpg"],
            color="Red",
            stock=50,
            description="Test product description",
            seller=seller_data,
            payment_methods=["credit", "debit"],
            features=features_data
        )
        
        assert product.id == "test-product"
        assert product.title == "Test Product"
        assert product.price == 99.99
        assert product.discount_percentage == 10
        assert product.installments == "3 cuotas sin interés"
        assert product.images == ["image1.jpg", "image2.jpg"]
        assert product.color == "Red"
        assert product.stock == 50
        assert product.description == "Test product description"
        assert product.seller == seller_data
        assert product.payment_methods == ["credit", "debit"]
        assert product.features == features_data
    
    def test_product_model_dump_method(self):
        """Test Product model_dump() method"""
        seller = Seller(name="Test", is_official_store=True, sales=100, rating=4.0)
        features = Features(
            screen_size="6.1 inches",
            internal_memory="128GB", 
            front_camera="12MP",
            rear_camera="24MP",
            nfc=False,
            unlock="Fingerprint"
        )
        product = Product(
            id="test-product",
            title="Test Product",
            price=99.99,
            discount_percentage=10,
            installments="3 cuotas",
            images=["image1.jpg"],
            color="Red",
            stock=50,
            description="Test description",
            seller=seller,
            payment_methods=["credit"],
            features=features
        )
        
        product_dict = product.model_dump()
        assert isinstance(product_dict, dict)
        assert product_dict["id"] == "test-product"
        assert product_dict["title"] == "Test Product"
        assert product_dict["price"] == 99.99


class TestPaymentMethod:
    """Test cases for PaymentMethod domain model"""
    
    def test_card_creation(self):
        """Test Card creation"""
        card = Card(
            name="Credit Card",
            logo="credit_card.png"
        )
        
        assert card.name == "Credit Card"
        assert card.logo == "credit_card.png"
    
    def test_payment_methods_creation(self):
        """Test PaymentMethods creation"""
        cards = [
            Card(name="Visa", logo="visa.png"),
            Card(name="Mastercard", logo="master.png")
        ]
        payment_methods = PaymentMethods(
            cuotasMessage="Pay in installments",
            creditCards=cards,
            debitCards=cards,
            cash=cards
        )
        
        assert payment_methods.cuotasMessage == "Pay in installments"
        assert len(payment_methods.creditCards) == 2
        assert payment_methods.creditCards[0].name == "Visa"
    
    def test_payment_methods_model_dump_method(self):
        """Test PaymentMethods model_dump() method"""
        cards = [Card(name="Test Card", logo="test.png")]
        payment_methods = PaymentMethods(
            cuotasMessage="Test message",
            creditCards=cards,
            debitCards=cards,
            cash=cards
        )
        
        payment_dict = payment_methods.model_dump()
        assert isinstance(payment_dict, dict)
        assert payment_dict["cuotasMessage"] == "Test message"
        assert len(payment_dict["creditCards"]) == 1


class TestRecommendedProduct:
    """Test cases for RecommendedProduct domain model"""
    
    def test_recommended_product_creation(self):
        """Test RecommendedProduct creation"""
        recommended_product = RecommendedProduct(
            id="rec-product-1",
            title="Recommended Product",
            image="recommended.jpg",
            priceOld=99.99,
            priceNew=79.99,
            discount=20,
            installments="3 cuotas sin interés"
        )
        
        assert recommended_product.id == "rec-product-1"
        assert recommended_product.title == "Recommended Product"
        assert recommended_product.image == "recommended.jpg"
        assert recommended_product.priceOld == 99.99
        assert recommended_product.priceNew == 79.99
        assert recommended_product.discount == 20
        assert recommended_product.installments == "3 cuotas sin interés"
    
    def test_recommended_product_model_dump_method(self):
        """Test RecommendedProduct model_dump() method"""
        recommended_product = RecommendedProduct(
            id="rec-product-2",
            title="Another Recommended Product",
            image="another_recommended.jpg",
            priceOld=149.99,
            priceNew=119.99,
            discount=20,
            installments="6 cuotas sin interés"
        )
        
        product_dict = recommended_product.model_dump()
        assert isinstance(product_dict, dict)
        assert product_dict["id"] == "rec-product-2"
        assert product_dict["title"] == "Another Recommended Product"
        assert product_dict["priceOld"] == 149.99
        assert product_dict["priceNew"] == 119.99


class TestSeller:
    """Test cases for Seller domain model"""
    
    def test_seller_creation(self):
        """Test Seller creation"""
        seller = Seller(
            name="Test Seller Inc.",
            is_official_store=True,
            sales=5000,
            rating=4.8
        )
        
        assert seller.name == "Test Seller Inc."
        assert seller.is_official_store == True
        assert seller.sales == 5000
        assert seller.rating == 4.8
    
    def test_seller_model_dump_method(self):
        """Test Seller model_dump() method"""
        seller = Seller(
            name="Another Seller",
            is_official_store=False,
            sales=1200,
            rating=4.2
        )
        
        seller_dict = seller.model_dump()
        assert isinstance(seller_dict, dict)
        assert seller_dict["name"] == "Another Seller"
        assert seller_dict["is_official_store"] == False
        assert seller_dict["sales"] == 1200
        assert seller_dict["rating"] == 4.2


class TestFeatures:
    """Test cases for Features domain model"""
    
    def test_features_creation(self):
        """Test Features creation"""
        features = Features(
            screen_size="6.5 inches",
            internal_memory="256GB",
            front_camera="32MP",
            rear_camera="108MP",
            nfc=True,
            unlock="Face unlock"
        )
        
        assert features.screen_size == "6.5 inches"
        assert features.internal_memory == "256GB"
        assert features.front_camera == "32MP"
        assert features.rear_camera == "108MP"
        assert features.nfc == True
        assert features.unlock == "Face unlock"
    
    def test_features_model_dump_method(self):
        """Test Features model_dump() method"""
        features = Features(
            screen_size="6.1 inches",
            internal_memory="128GB",
            front_camera="12MP", 
            rear_camera="48MP",
            nfc=False,
            unlock="Fingerprint"
        )
        
        features_dict = features.model_dump()
        assert isinstance(features_dict, dict)
        assert features_dict["screen_size"] == "6.1 inches"
        assert features_dict["internal_memory"] == "128GB"
        assert features_dict["nfc"] == False
