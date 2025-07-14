import json
from pathlib import Path
from domain.models.product import Product
from domain.models.seller import Seller
from domain.models.features import Features
from domain.ports.product_repository import ProductRepository

class JSONProductRepository(ProductRepository):
    def __init__(self, data_path):
        self.data_path = Path(data_path)

    def get_product_by_id(self, product_id: str) -> Product:
        with self.data_path.open() as f:
            data = json.load(f)
            for item in data:
                if item['id'] == product_id:
                    return self._parse_product(item)
        return None

    def _parse_product(self, item: dict) -> Product:
        seller = Seller(**item['seller'])
        features = Features(**item['features'])
        return Product(
            id=item['id'],
            title=item['title'],
            price=item['price'],
            discount_percentage=item['discount_percentage'],
            installments=item['installments'],
            images=item['images'],
            color=item['color'],
            stock=item['stock'],
            description=item['description'],
            seller=seller,
            payment_methods=item['payment_methods'],
            features=features
        )
