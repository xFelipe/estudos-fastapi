from fastapi import APIRouter
from api.v1.endpoints import curso
from core.configs import settings


router = APIRouter(prefix=settings.API_V1_PREFIX)

router.include_router(curso.router, prefix="/cursos", tags=["cursos"])

