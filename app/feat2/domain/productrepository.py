from abc import ABC, abstractmethod
from feat2.domain.productmodel import ProductDto

class ProductRepository(ABC):
    
    @abstractmethod    
    def retrieve(self, id: int):    
        raise NotImplementedError
    
    @abstractmethod    
    def retrieveAll(self):
        raise NotImplementedError

    @abstractmethod    
    def create(self, p: ProductDto):
        raise NotImplementedError

    @abstractmethod    
    def update(self, p: ProductDto):
        raise NotImplementedError

    @abstractmethod    
    def delete(selft, id: int):
        raise NotImplementedError