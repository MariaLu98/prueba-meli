from typing import List
from domain.ports.recommended_products_repository import RecommendedProductsRepository
from domain.models.recommended_product import RecommendedProduct

class GetRelatedProductsUseCase:
    def __init__(self, repository: RecommendedProductsRepository):
        self.repository = repository

    def execute(self) -> List[RecommendedProduct]:
        return self.repository.get_all_recommended_products()
