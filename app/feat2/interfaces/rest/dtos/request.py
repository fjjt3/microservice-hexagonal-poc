from pydantic import BaseModel
from typing import Optional

class ProductDto(BaseModel):
    idid: Optional[int] = None
    product: str