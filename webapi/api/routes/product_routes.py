from fastapi import APIRouter, HTTPException, Depends
from api.security import verify_token
from application.use_cases.get_product_detail import GetProductDetailUseCase

def get_product_router(use_case: GetProductDetailUseCase):
    router = APIRouter()

    @router.get("/api/items/{product_id}")
    async def get_product(product_id: str):
        product = use_case.execute(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    return router 
