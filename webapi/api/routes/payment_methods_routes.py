from fastapi import APIRouter, Depends
from api.security import verify_token
from application.use_cases.get_payment_methods import GetPaymentMethodsUseCase

def get_payment_methods_router(use_case: GetPaymentMethodsUseCase):
    router = APIRouter()
    @router.get("/api/payment-methods")
    async def get_payment_methods():
        return use_case.execute()
    return router 
