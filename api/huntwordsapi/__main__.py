import os
from fastapi import FastAPI, Request

from uvicorn import run

from .handler import handle

app = FastAPI()


@app.get("/")
def index(_request: Request):
    body = {'Hello': 'World from GET'}
    return handle({'oper': 'echo', 'body': body})


@app.post("/")
async def post_handler(request: Request):
    body = await request.json()
    return handle(body)


if __name__ == '__main__':
    host = os.environ['APP_HOST'] if 'APP_HOST' in os.environ else 'api'
    port_str = os.environ['APP_PORT'] if 'APP_PORT' in os.environ else '3000'
    port = int(port_str)
    root_path = os.environ['APP_ROOT'] if 'APP_ROOT' in os.environ else 'api'

    print(f'Running on {host}:{port} with root_path={root_path}')

    run(app, host=host, port=port, proxy_headers=True, root_path=root_path)
