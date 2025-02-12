
import requests
import uuid
from datetime import datetime

from starlette.responses import JSONResponse
from starlette.responses import Response
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from model.req.task import *
from model.resp.task import *
from model.db.user_task import *
from prompt_map import *
from starlette.authentication import requires

HOST = "99.79.37.130"
URL = f"http://{HOST}:8188"

class Image(HTTPEndpoint):
    @requires("authenticated")
    async def post(self, request):
        async with request.form() as form:
            resp = self.upload_image({
                "image": (form["image"].filename, await form["image"].read(), "image/jpeg")
            })
            return JSONResponse(resp.json())
        
    def upload_image(self, files:dict):
        return requests.post(f'{URL}/upload/image', files=files)

class Prompt(HTTPEndpoint):
    @requires("authenticated")
    async def post(self, request:Request):
        inputs = await request.json()
        task_id = str(uuid.uuid4())
        client_id = request.user.username
        user_type = UserType.NORMAL.value if "vip" in request.auth.scopes else UserType.VIP.value
        user_task = {
            "task_id": task_id,
            "client_id": client_id,
            "user_type": user_type,
            "inputs": str(inputs),
            "status": TaskStatus.PENDING.value,
            "start_time": datetime.now()
        }
        await save_task(user_task)
        user_task["inputs"] = inputs
        return JSONResponse(user_task)
    
class Queue(HTTPEndpoint):
    @requires("authenticated")
    async def get(self, request:Request):
        client_id = request.user.username
        result = await find_unfinished_by_client_id(client_id)
        return JSONResponse(result)

class Status(HTTPEndpoint):
    @requires("authenticated")
    async def get(self, request):
        client_id = request.user.username
        result = await find_by_client_id(client_id=client_id)
        return JSONResponse(result)
    
class Video(HTTPEndpoint):
    async def get(self, request:Request):
        assert request.query_params["filename"]
        resp = self.get_video(request.query_params["filename"])
        return Response(content=resp.content, media_type="video/mp4")
    
    def get_video(self, filename):
        return requests.get(f'{URL}/view', params={
            "filename": filename,
            "type": "output"
        })


routes = [
    Route("/image", Image),
    Route("/prompt", Prompt),
    Route("/queue", Queue),
    Route("/status", Status),
    Route("/video", Video),
]