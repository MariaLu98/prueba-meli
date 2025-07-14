from fastapi import APIRouter, Depends
from api.security import verify_token
from application.use_cases.get_payment_methods import GetPaymentMethodsUseCase

def get_payment_methods_router(use_case: GetPaymentMethodsUseCase):
    router = APIRouter()

    @router.get("/payment-methods")
    async def get_payment_methods(
        auth: None = Depends(verify_token)
    ):
        result = use_case.execute()
        return result

    return router
