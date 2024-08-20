from fastapi import FastAPI
from time import sleep
import asyncio

app = FastAPI()


@app.get('/msg')
async def mensagem():
    await(asyncio.sleep(0.1))
    return {'msg': 'Fast api funcionando corretamente!'}


# uvicorn --reload --port=5000 main:app
# gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', log_level='info', reload=True)