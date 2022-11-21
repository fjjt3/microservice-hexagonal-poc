from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.responses import Response

from config.container import Container
from config.sennder_openapi_util import *
from feat1.interfaces.rest.dtos.request import UserDto

# Here we can put information about:
# - Prefix
# - Common Responses
# - Tag
router = APIRouter(prefix="/users", tags=["User"])

# ENDPOINTS
@router.get(
    "/",
    summary="Get a User List Summary",
    description="Get a User List Description",
    responses={**response_get},
)
@inject
def retrieveAll(service=Depends(Provide[Container.user_service])):
    return service.retrieveAll()


@router.get(
    "/{id}",
    summary="Get a User by ID Summary",
    description="Get a User by ID Description",
    responses={**response_get},
)
@inject
def retrieve(id: int, service=Depends(Provide[Container.user_service])) -> Response:
    return service.retrieve(id)


@router.post(
    "/",
    summary="Create a User Summary",
    description="Create a User Description",
    responses={**response_post},
)
@inject
async def create(
    user: UserDto, service=Depends(Provide[Container.user_service])
) -> Response:
    return service.create(user)


@router.put(
    "/{id}",
    summary="Update a User Summary",
    description="Update a User Description",
    responses={**response_update},
)
@inject
async def update(
    id: int, user: UserDto, service=Depends(Provide[Container.user_service])
) -> Response:
    return service.update(user)


@router.delete(
    "/{id}",
    summary="Delete a User Summary",
    description="Delete a User Description",
    responses={**response_delete},
)
@inject
async def delete(id: int, service=Depends(Provide[Container.user_service])) -> Response:
    return service.delete(id)
