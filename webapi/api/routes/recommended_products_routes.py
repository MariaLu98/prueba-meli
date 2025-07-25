from fastapi import APIRouter, Depends
from api.security import verify_token
from application.use_cases.get_recommended_products import GetRecommendedProductsUseCase

def get_recommended_products_router(use_case: GetRecommendedProductsUseCase):
    router = APIRouter()

    @router.get("/api/recommended-products")
    async def get_recommended_products():
        result = use_case.execute()
        return [item.model_dump() for item in result]
    return router 