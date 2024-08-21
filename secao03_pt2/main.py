from fastapi import FastAPI

from routes.curso_router import router as curso_router
from routes.usuario_router import router as usuario_router


app = FastAPI()

app.include_router(curso_router, tags=["cursos"])
app.include_router(usuario_router, tags=["usuarios"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
