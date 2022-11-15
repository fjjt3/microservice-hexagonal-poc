from fastapi import Depends
from feat2.domain.productmodel import ProductDto
from feat2.infrastructure.db.productdbrepository import ProductDbRepository

class ProductService:

    def __init__(self, repository=Depends(ProductDbRepository)):
        self.repository = repository

    def retrieve(self, id: int):    
        return self.repository.retrieve(id)

    def retrieveAll(self):
        return self.repository.retrieveAll()
    
    def create(self, p: ProductDto):
        return self.repository.create(p)

    def update(self, p: ProductDto):
        return self.repository.update(p)

    def delete(self, id: int):
        return self.repository.delete(id)
