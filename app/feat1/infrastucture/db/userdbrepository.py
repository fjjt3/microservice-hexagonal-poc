from feat1.domain.usermodel import UserDto
from feat1.domain.userrepository import UserRepository

class UserDbRepository(UserRepository):

    def __init__(self): 
        self.fakeDB=[
            UserDto(user_id=1, first_name="Ilde",last_name="Serrano"),
            UserDto(user_id=2, first_name="Antonio",last_name="Serrano")
        ]

    def retrieve(self, id: int):  
        return self.fakeDB[id]

    def retrieveAll(self):
        return self.fakeDB
    
    def create(self, user: UserDto):
        self.fakeDB.append(user)
        return self.fakeDB

    def update(self, user: UserDto):
        userFound = self.fakeDB[user.user_id]
        if userFound:
            self.fakeDB[user.user_id]= user
        return self.fakeDB

    def delete(self, id: int):
        userFound = self.fakeDB[id]
        if userFound:
            del self.fakeDB[id]
        return self.fakeDB