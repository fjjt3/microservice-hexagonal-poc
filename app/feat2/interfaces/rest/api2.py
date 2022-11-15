from fastapi import APIRouter, Depends
from feat2.domain.productservice import ProductService
from feat2.interfaces.rest.dtos.request import ProductDto
from starlette.responses import Response

# Feature Router Configuration
router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={
        200: {"description": "Successfull Response"},
        404: {"description": "Not found"}
    }
)

# ENDPOINTS
@router.get("/")
def retrieveAll(service = Depends(ProductService)):
    return service.retrieveAll()

@router.get("/{id}")
def retrieve(id: int, service = Depends(ProductService)) -> Response:
    return service.retrieve(id)

@router.post("/")
async def create(p: ProductDto, service = Depends(ProductService)) -> Response:    
    return service.create(p)

@router.put("/{id}")
async def update(id: int, p: ProductDto, service = Depends(ProductService)) -> Response:
    return service.update(p)

@router.delete("/{id}")
async def delete(id: int, service = Depends(ProductService)) -> Response:
    return service.delete(id)