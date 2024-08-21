from fastapi import FastAPI, HTTPException, status
from models import Curso, cursos
from fastapi.responses import JSONResponse, Response
from fastapi import Path, Query, Header
from typing import Optional, Dict, List


app = FastAPI(title="API de cursos", summary="API para estudos do FastAPI", version="0.0.1k")




@app.get("/cursos",
         description="Retorna uma lista com todos os cursos",
         summary="Retorna os cursos",
         response_model=List[Curso],
         response_description="Cursos encontrados com sucesso")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}", response_model=Curso)
async def get_curso(
        curso_id: int = Path(title='ID do curso',description='Deve ser entre 1 e 2', gt=0, lt=3)
    ):
    try:
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):

    new_curso_id = max([curso.id for curso in cursos]) + 1 
    curso.id = new_curso_id
    cursos.append(curso)


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id not in cursos:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Não existe um curso com o id {curso_id}")

    cursos[curso_id] = curso
    del curso.id


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id not in cursos:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Não existe um curso com o id {curso_id}")

    cursos.pop(curso_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/calculadora')
async def calculadora(a: int = Query(gt=0, lt=100),
                      b: int = Query(gt=0, lt=100),
                      c: Optional[int] = Query(default=0, gt=0, lt=100),
                      x_mensagem: str = Header(default=None)):
    print("Mensagem: ", x_mensagem)
    soma = a + b + c
    return {"resultado": soma}


if __name__ == "__main__":
    import uvicorn
    app.debug = True
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
