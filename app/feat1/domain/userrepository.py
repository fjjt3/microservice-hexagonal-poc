from abc import ABC, abstractmethod
from feat1.domain.usermodel import UserDto

class UserRepository(ABC):
    
    @abstractmethod    
    def retrieve(self, user_id: int):    
        raise NotImplementedError
    
    @abstractmethod    
    def retrieveAll(self):
        raise NotImplementedError

    @abstractmethod    
    def create(self, user: UserDto):
        raise NotImplementedError

    @abstractmethod    
    def update(self, user: UserDto):
        raise NotImplementedError

    @abstractmethod    
    def delete(selft, user_id: int):
        raise NotImplementedError
