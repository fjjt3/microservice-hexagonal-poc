from pydantic import BaseModel
from typing import Optional

class UserDto(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str