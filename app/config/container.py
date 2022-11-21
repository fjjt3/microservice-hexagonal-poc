from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory

from feat1.domain.userservice import UserService
from feat1.infrastucture.db.userdbrepository import UserDbRepository
from feat2.domain.productservice import ProductService
from feat2.infrastructure.db.productdbrepository import ProductDbRepository


class Container(DeclarativeContainer):
    user_repository = Factory(UserDbRepository)
    user_service = Factory(UserService, repository=user_repository)

    product_repository = Factory(ProductDbRepository)
    product_service = Factory(ProductService, repository=product_repository)
