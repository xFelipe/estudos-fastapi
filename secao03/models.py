from typing import Optional

from pydantic import BaseModel, field_validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    def valida_titulo(cls, value: str):
        if len(value) < 4:
            raise ValueError("Título muito curto. Minimo: 4 caractéres.")
        if value[0].islower():
            raise ValueError("O título deve estar capitalizado.")


cursos = [
    Curso(id=1, titulo="Programação para leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Programação para leigos", aulas=112,horas=58),
    Curso(id=3, titulo="Algoritmos e lógica de programação", aulas=87, horas=67)
]