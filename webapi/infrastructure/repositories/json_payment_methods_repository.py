import json
from pathlib import Path
from domain.models.payment_methods import PaymentMethods
from domain.ports.payment_methods_repository import PaymentMethodsRepository

class JSONPaymentMethodsRepository(PaymentMethodsRepository):
    def __init__(self, data_path):
        self.data_path = Path(data_path)

    def get_payment_methods(self) -> PaymentMethods:
        with self.data_path.open() as f:
            data = json.load(f)
            return PaymentMethods(**data)
