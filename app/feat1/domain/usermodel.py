from pydantic import BaseModel
from typing import Optional

# Model Package

# It contains Modelling clases. 

class UserDto(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str