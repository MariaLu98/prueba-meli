from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.repositories.json_related_products_repository import JSONRelatedProductsRepository
from application.use_cases.get_related_products import GetRelatedProductsUseCase
from api.routes import related_products_routes
from infrastructure.repositories.json_product_repository import JSONProductRepository
from application.use_cases.get_product_detail import GetProductDetailUseCase
from infrastructure.repositories.json_payment_methods_repository import JSONPaymentMethodsRepository
from application.use_cases.get_payment_methods import GetPaymentMethodsUseCase
from infrastructure.repositories.json_recommended_products_repository import JSONRecommendedProductsRepository
from application.use_cases.get_recommended_products import GetRecommendedProductsUseCase
from api.routes import recommended_products_routes
from api.routes import product_routes, auth_routes, payment_methods_routes

app = FastAPI(
    title="Product Detail API",
    description="Test API for retrieving product details Mercado Libre",
    version="1.0"
)

# CORS (opcional pero recomendado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Productos
product_repo = JSONProductRepository(data_path="infrastructure/data/products.json")
product_use_case = GetProductDetailUseCase(product_repo)
app.include_router(product_routes.get_product_router(product_use_case))

# Payment methods
payment_repo = JSONPaymentMethodsRepository(data_path="infrastructure/data/payment_methods.json")
payment_use_case = GetPaymentMethodsUseCase(payment_repo)
app.include_router(payment_methods_routes.get_payment_methods_router(payment_use_case))

# Recommended Products
recommended_repo = JSONRecommendedProductsRepository(data_path="infrastructure/data/recommended_products.json")
recommended_use_case = GetRecommendedProductsUseCase(recommended_repo)
app.include_router(recommended_products_routes.get_recommended_products_router(recommended_use_case))

# Related Products
related_repo = JSONRelatedProductsRepository(data_path="infrastructure/data/related_products.json")
related_use_case = GetRelatedProductsUseCase(related_repo)
app.include_router(related_products_routes.get_related_products_router(related_use_case))

# Auth
app.include_router(auth_routes.router)
