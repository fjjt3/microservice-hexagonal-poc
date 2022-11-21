from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from starlette.responses import Response

from config.container import Container
from feat2.interfaces.rest.dtos.request import ProductDto

# Feature Router Configuration
router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={
        200: {"description": "Successfull Response"},
        404: {"description": "Not found"},
    },
)

# ENDPOINTS
@router.get("/")
@inject
def retrieveAll(service=Depends(Provide[Container.product_service])):
    return service.retrieveAll()


@router.get("/{id}")
@inject
def retrieve(id: int, service=Depends(Provide[Container.product_service])) -> Response:
    return service.retrieve(id)


@router.post("/")
@inject
async def create(
    p: ProductDto, service=Depends(Provide[Container.product_service])
) -> Response:
    return service.create(p)


@router.put("/{id}")
@inject
async def update(
    id: int, p: ProductDto, service=Depends(Provide[Container.product_service])
) -> Response:
    return service.update(p)


@router.delete("/{id}")
@inject
async def delete(
    id: int, service=Depends(Provide[Container.product_service])
) -> Response:
    return service.delete(id)
