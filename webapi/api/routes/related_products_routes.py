from fastapi import APIRouter, Depends
from api.security import verify_token
from application.use_cases.get_related_products import GetRelatedProductsUseCase

def get_related_products_router(use_case: GetRelatedProductsUseCase):
    router = APIRouter()

    @router.get("/api/related-products")
    async def get_related_products():
        result = use_case.execute()
        return [item.dict() for item in result]
    return router 