from typing import Optional

from pydantic._internal._model_construction import ModelMetaclass as __ModelMetaclass
from pydantic import BaseModel as BaseSchema


class CursoSchema(BaseSchema):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    class Config:
        from_attributes = True


class UpdateCursoSchema(CursoSchema):
    id: Optional[int] = None
    titulo: str = None
    aulas: int = None
    horas: int = None
