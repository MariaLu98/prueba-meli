class GetProductDetailUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, product_id: str):
        return self.repository.get_product_by_id(product_id)
