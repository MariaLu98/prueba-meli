import json
from pathlib import Path
from typing import List
from domain.models.recommended_product import RecommendedProduct
from domain.ports.recommended_products_repository import RecommendedProductsRepository

class JSONRecommendedProductsRepository(RecommendedProductsRepository):
    def __init__(self, data_path):
        self.data_path = Path(data_path)

    def get_all_recommended_products(self) -> List[RecommendedProduct]:
        with self.data_path.open() as f:
            data = json.load(f)
            return [RecommendedProduct(**item) for item in data]
