from typing import Optional
from sqlmodel import Field, SQLModel


class UpdateCursoSchema(SQLModel):
    titulo: Optional[str] = None
    aulas: Optional[int] = None
    horas: Optional[int] = None


class CursoModel(SQLModel, table=True):
    __tablename__ = "cursos"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int

    def update(self, curso: UpdateCursoSchema):
        if curso.titulo:
            self.titulo = curso.titulo
        if curso.aulas:
            self.aulas = curso.aulas
        if curso.horas:
            self.horas = curso.horas
