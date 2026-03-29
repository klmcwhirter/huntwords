import os
from http import HTTPStatus

import uvicorn
from fastapi import BackgroundTasks, FastAPI, Request, Response

from .commands.adapter import handle_request

app = FastAPI()


@app.get("/api/")
def index(_request: Request):
    body = {'message': 'Not intended to be used directly.'}
    return handle_request({'oper': 'echo', 'body': body})


@app.post("/api/")
async def post_handler(request: Request):
    body = await request.json()
    return handle_request(body)


@app.post("/api/async")
async def post_handler_async(request: Request, bg_tasks: BackgroundTasks):
    body = await request.json()
    bg_tasks.add_task(handle_request, body)
    return Response(status_code=HTTPStatus.ACCEPTED)


if __name__ == '__main__':
    host = os.environ['APP_HOST'] if 'APP_HOST' in os.environ else 'localhost'
    port_str = os.environ['APP_PORT'] if 'APP_PORT' in os.environ else '3000'
    port = int(port_str)

    print(f'Running on {host}:{port}')

    uvicorn.run(app, host=host, port=port, proxy_headers=True)
