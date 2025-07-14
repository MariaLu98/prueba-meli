from dataclasses import dataclass
from typing import List
from .seller import Seller
from .features import Features

@dataclass
class Product:
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
