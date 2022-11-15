from fastapi import APIRouter, Depends
from starlette.responses import Response

from config.sennder_openapi_util import *

from feat1.interfaces.rest.dtos.request import UserDto
from feat1.domain.userservice import UserService

# Here we can put information about:
# - Prefix
# - Common Responses
# - Tag
router = APIRouter(
    prefix="/users",
    tags=["User"]
)

# ENDPOINTS
@router.get("/",
    summary= "Get a User List Summary",
    description= "Get a User List Description",
    responses={
        **response_get
    }
)
def retrieveAll(service = Depends(UserService)):
    return service.retrieveAll()

@router.get("/{id}",
    summary= "Get a User by ID Summary",
    description= "Get a User by ID Description",
    responses={
        **response_get
    }
)
def retrieve(id: int, service = Depends(UserService)) -> Response:
    return service.retrieve(id)

@router.post("/",
    summary= "Create a User Summary",
    description= "Create a User Description",
    responses={
        **response_post
    }
)
async def create(user: UserDto, service = Depends(UserService)) -> Response:    
    return service.create(user)

@router.put("/{id}",
    summary= "Update a User Summary",
    description= "Update a User Description",
    responses={
        **response_update
    }
)
async def update(id: int, user: UserDto, service = Depends(UserService)) -> Response:
    return service.update(user)

@router.delete("/{id}",
    summary= "Delete a User Summary",
    description= "Delete a User Description",
    responses={
        **response_delete
    }
)
async def delete(id: int, service = Depends(UserService)) -> Response:
    return service.delete(id)