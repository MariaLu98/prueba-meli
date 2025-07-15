from typing import Optional
from pydantic import BaseModel

class Seller(BaseModel):
    id: Optional[int] = None
    name: str
    is_official_store: bool
    sales: int
    rating: float
