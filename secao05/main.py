from fastapi import FastAPI
from api.router import router

app = FastAPI(title="API de cursos")
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, log_level="info")