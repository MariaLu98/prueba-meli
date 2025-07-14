from dataclasses import dataclass

@dataclass
class Seller:
    name: str
    is_official_store: bool
    sales: int
    rating: float
