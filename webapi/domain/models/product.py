from typing import List
from .seller import Seller
from .features import Features
from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str
    price: float
    discount_percentage: int
    installments: str
    images: List[str]
    color: str
    stock: int
    description: str
    seller: Seller
    payment_methods: List[str]
    features: Features
