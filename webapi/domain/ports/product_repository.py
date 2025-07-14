from abc import ABC, abstractmethod
from domain.models.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def get_product_by_id(self, product_id: str) -> Product:
        pass
