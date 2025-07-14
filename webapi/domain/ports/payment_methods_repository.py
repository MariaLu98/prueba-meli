from abc import ABC, abstractmethod
from domain.models.payment_methods import PaymentMethods

class PaymentMethodsRepository(ABC):
    @abstractmethod
    def get_payment_methods(self) -> PaymentMethods:
        pass
