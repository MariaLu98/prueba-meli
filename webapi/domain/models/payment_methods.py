from typing import List
from pydantic import BaseModel

class Card(BaseModel):
    name: str
    logo: str

class PaymentMethods(BaseModel):
    cuotasMessage: str
    creditCards: List[Card]
    debitCards: List[Card]
    cash: List[Card]
