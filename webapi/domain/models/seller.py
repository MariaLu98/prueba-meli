from dataclasses import dataclass
from pydantic import BaseModel
@dataclass
class Seller(BaseModel):
    name: str
    is_official_store: bool
    sales: int
    rating: float
