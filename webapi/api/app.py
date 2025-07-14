from fastapi import FastAPI
from infrastructure.repositories.json_product_repository import JSONProductRepository
from application.use_cases.get_product_detail import GetProductDetailUseCase
from api.routes import product_routes, auth_routes

app = FastAPI(
    title="Product Detail API",
    description="Test API for retrieving product details Mercado Libre",
    version="1.0"
)

repo = JSONProductRepository(data_path="infrastructure/data/products.json")
use_case = GetProductDetailUseCase(repo)
app.include_router(product_routes.get_product_router(use_case))
app.include_router(auth_routes.router)
