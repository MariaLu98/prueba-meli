from domain.ports.payment_methods_repository import PaymentMethodsRepository
from domain.models.payment_methods import PaymentMethods

class GetPaymentMethodsUseCase:
    def __init__(self, repository: PaymentMethodsRepository):
        self.repository = repository

    def execute(self) -> PaymentMethods:
        return self.repository.get_payment_methods()
