from fastapi import Depends
from feat1.domain.usermodel import UserDto
from feat1.infrastucture.db.userdbrepository import UserDbRepository

class UserService:

    def __init__(self, repository=Depends(UserDbRepository)):
        self.repository = repository

    def retrieve(self, id: int):    
        return self.repository.retrieve(id)

    def retrieveAll(self):
        return self.repository.retrieveAll()
    
    def create(self, user: UserDto):
        return self.repository.create(user)

    def update(self, user: UserDto):
        return self.repository.update(user)

    def delete(self, id: int):
        return self.repository.delete(id)
