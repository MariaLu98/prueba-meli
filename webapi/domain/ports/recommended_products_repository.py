from abc import ABC, abstractmethod
from typing import List
from domain.models.recommended_product import RecommendedProduct

class RecommendedProductsRepository(ABC):
    @abstractmethod
    def get_all_recommended_products(self) -> List[RecommendedProduct]:
        pass
