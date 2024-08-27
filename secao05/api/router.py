from fastapi import APIRouter
from api.v1.endpoints.curso import router as curso_router
from core.configs import settings

router = APIRouter()

router.include_router(curso_router, prefix=settings.API_V1_PREFIX)