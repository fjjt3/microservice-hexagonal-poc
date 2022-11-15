from distutils.log import debug
import logging

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from feat1.interfaces.rest  import api1
from feat2.interfaces.rest import api2
from config.sennder_openapi_util import Contact, License

# Api Routing Configuration
api_router = APIRouter()
api_router.include_router(api1.router)
api_router.include_router(api2.router)

# Logging Configuration
LOGGER = logging.getLogger(__name__)

# Server Creation
def createServer() -> FastAPI:
    '''
        Create Server 
    '''
    try:
        LOGGER.info("Initiliase fast-API app")
        server = FastAPI(
            title="Hexagonal Rest Microservice",
            description="REST API Microservice.",
            version="1.0.0",
            terms_of_service= "http://example.com/terms/",
            contact= Contact("API Support", "http://www.example.com/support","support@example.com").__dict__,
            license_info= License("Apache 2.0", "https://www.apache.org/licenses/LICENSE-2.0.html").__dict__
        )
        origins = ["http://localhost:8005"]
        server.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        server.include_router(api_router, prefix="/api/v1")
    except Exception as e:
        LOGGER.error(f"Error in fast-API app initialisation => {e}")
    return server




