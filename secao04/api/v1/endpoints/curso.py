from typing import List
from fastapi import APIRouter, HTTPException
from fastapi import status, Depends
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, text

from schemas.curso_schema import CursoSchema, UpdateCursoSchema
from core.deps import get_session
from models.curso import CursoModel


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)) -> CursoSchema:
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)
    await db.commit()

    return novo_curso


@router.put("/{curso_id}")
async def put_curso(curso_id: int,
                    curso: UpdateCursoSchema,
                    db: AsyncSession = Depends(get_session)) -> CursoSchema:
    async with db as session:
        query = select(CursoModel).where(CursoModel.id==curso_id)
        result = await session.execute(query)
        curso_atualizado = result.one_or_none()
        if not curso_atualizado:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Curso com id {curso_id} não foi encontrado")
    
    curso_atualizado: CursoModel = curso_atualizado[0]
    curso_atualizado.update_fields(**curso.model_dump())

    db.add(curso_atualizado)
    await db.commit()
    return curso_atualizado


@router.get("/", response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos


@router.get("/{curso_id}")
async def get_curso(curso_id: int,
              db: AsyncSession = Depends(get_session)) -> CursoSchema:
    query = select(CursoModel).where(CursoModel.id == curso_id)
    async with db as session:
        result = await session.execute(query)
    curso = result.one_or_none()

    if not curso:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"Curso com id {curso_id} não foi encontrado")
    return curso[0]


@router.delete("/{curso_id}")
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    query = delete(CursoModel).where(CursoModel.id==curso_id)
    await db.execute(query)
    await db.commit()
    return Response(str(query))