from feat2.domain.productmodel import ProductDto
from feat2.domain.productrepository import ProductRepository

class ProductDbRepository(ProductRepository):

    def __init__(self): 
        self.fakeDB=[
            ProductDto(id=1, product="Laptop"),
            ProductDto(id=2, product="Server")
        ]

    def retrieve(self, id: int):  
        return self.fakeDB[id]

    def retrieveAll(self):
        return self.fakeDB
    
    def create(self, p: ProductDto):
        self.fakeDB.append(p)
        return self.fakeDB

    def update(self, p: ProductDto):
        pFound = self.fakeDB[p.id]
        if pFound:
            self.fakeDB[p.id]= p
        return self.fakeDB

    def delete(self, id: int):
        pFound = self.fakeDB[id]
        if pFound:
            del self.fakeDB[id]
        return self.fakeDB