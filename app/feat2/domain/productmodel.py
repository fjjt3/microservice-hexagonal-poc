from pydantic import BaseModel
from typing import Optional

class ProductDto(BaseModel):
    id: Optional[int] = None
    product: str