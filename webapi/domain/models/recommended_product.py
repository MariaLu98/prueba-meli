from pydantic import BaseModel

class RecommendedProduct(BaseModel):
    id: str
    title: str
    image: str
    priceOld: float
    priceNew: float
    discount: int
    installments: str
