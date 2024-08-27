from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from core.deps import get_session
from models.curso import CursoModel, UpdateCursoSchema
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/cursos", tags=["curso"])


@router.get("/", response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    query = select(CursoModel)
    async with db as session:
        result = await session.execute(query)
    cursos = result.scalars().all()

    return cursos


@router.get("/{id_curso}", response_model=CursoModel)
async def get_cursos(id_curso:int, db: AsyncSession = Depends(get_session)):
    query = select(CursoModel).where(CursoModel.id == id_curso)
    async with db as session:
        result = await session.execute(query)
    curso = result.scalars().one_or_none()

    if not curso:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Curso {id_curso} não encontrado")

    return curso


@router.get("/{id_curso}", response_model=CursoModel)
async def get_curso(id_curso:int, db: AsyncSession = Depends(get_session)):
    query = select(CursoModel).where(CursoModel.id == id_curso)
    async with db as session:
        result = await session.execute(query)
    curso = result.scalars().one_or_none()

    if not curso:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Curso {id_curso} não encontrado")

    return curso


@router.post("/", response_model=CursoModel)
async def post_cursos(curso: CursoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        session.add(curso)
        await session.commit()
        await session.flush()

    return curso


@router.put("/{id_curso}", response_model=CursoModel, status_code=status.HTTP_200_OK)
async def put_curso(id_curso: int, dados_curso: UpdateCursoSchema, db: AsyncSession = Depends(get_session)):
    query = select(CursoModel).where(CursoModel.id == id_curso)
    async with db as session:
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if not curso:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Curso {id_curso} não encontrado")
        curso.update(dados_curso)
        session.add(curso)
        await session.commit()
    return curso


@router.delete("/{id_curso}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(id_curso: int, db: AsyncSession = Depends(get_session)):
    query = delete(CursoModel).where(CursoModel.id == id_curso)
    async with db as session:
        await session.execute(query)
        await session.commit()