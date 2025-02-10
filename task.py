
import json
import requests

from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from model.request.task import *
from prompt_map import *

URL = "http://35.183.41.190:8188"

class Image(HTTPEndpoint):
    # async def get(self, request):
    #     assert request.query_params["filename"]
    #     assert request.query_params["type"]
    #     resp = requests.get(f"{URL}/view", data={
    #         "filename": request.query_params["filename"],
    #         "type": request.query_params["type"]
    #     })
    #     return resp.content
    async def post(self, request):
        async with request.form() as form:
            resp = requests.post(f'{URL}/upload/image', files={
                "image": (form["image"].filename, await form["image"].read(), "image/jpeg")
            })
            return JSONResponse(resp.json())

class Prompt(HTTPEndpoint):
    async def post(self, request):
        data = await request.json()
        prompt_request = PromptRequest(**data)
        prompt = get_prompt(prompt_request=prompt_request)
        client_id = "12312312312"
        resp = requests.post(f'{URL}/prompt', json.dumps({
            "client_id": client_id,
            "prompt": prompt
        }))
        return JSONResponse(resp.json())
    

routes = [
    Route("/image", Image),
    Route("/prompt", Prompt),
]
