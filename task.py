
import json
import requests

from starlette.responses import JSONResponse
from starlette.responses import Response
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from model.req.task import *
from model.resp.task import *
from prompt_map import *
from starlette.authentication import requires

HOST = "35.183.70.208"
URL = f"http://{HOST}:8188"

import pickle

# username -> task_info:
#               task_id
#               prompt_id
#               inputs
#               outputs
#               status
USER_TASK = {}
# task_id -> prompt_id
TASK_ID_MAP = {}
# each queue includes a map, key = task_id, value = username
QUEUE_MAP = {
    "vip": [],
    "normal": []
}

def load_map():
    with open("./user_task.pkl", "rb") as f:
        global USER_TASK
        USER_TASK = pickle.load(f)
    with open("./task_id_map.pkl", "rb") as f:
        global TASK_ID_MAP
        TASK_ID_MAP = pickle.load(f)
    with open("./queue_map.pkl", "rb") as f:
        global QUEUE_MAP
        QUEUE_MAP = pickle.load(f)

load_map()

def save_user_task():
    with open("./user_task.pkl", "wb") as f:
        global USER_TASK
        pickle.dump(USER_TASK, f)

def save_task_id_map():
    with open("./task_id_map.pkl", "wb") as f:
        global TASK_ID_MAP
        pickle.dump(TASK_ID_MAP, f)

def save_queue_map():
    with open("./queue_map.pkl", "wb") as f:
        global QUEUE_MAP
        pickle.dump(QUEUE_MAP, f)

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
    async def post(self, request):
        data = await request.json()
        prompt_request = PromptRequest(**data)
        prompt = get_prompt(prompt_request=prompt_request)
        client_id = request.user.username
        resp = self.prompt(client_id=client_id, prompt=prompt)
        result = PromptResponse(**resp.json())
        if not result.node_errors:
            USER_TASK[client_id] = {
                result.prompt_id: {
                    "inputs": data
                }
            }
            save_user_task()
        return JSONResponse(resp.json())
    
    def prompt(self, client_id:str, prompt:dict):
        return requests.post(f'{URL}/prompt', json.dumps({
            "client_id": client_id,
            "prompt": prompt
        }))
    
class Queue(HTTPEndpoint):
    @requires("authenticated")
    async def get(self, request):
        client_id = request.user.username
        if not USER_TASK.__contains__(client_id):
            return JSONResponse({})
        resp = self.get_queue()
        result = QueueResponese(**resp.json())
        return JSONResponse({
            "queue_pending": [{"task_id":i[1], "inputs": USER_TASK[client_id][i[1]]["inputs"]} for i in result.queue_pending if USER_TASK[client_id].__contains__(i[1])],
            "queue_running": [{"task_id":i[1], "inputs": USER_TASK[client_id][i[1]]["inputs"]} for i in result.queue_running if USER_TASK[client_id].__contains__(i[1])]
        })
    
    def get_queue(self):
        return requests.get(f'{URL}/queue')

class Status(HTTPEndpoint):
    @requires("authenticated")
    async def get(self, request):
        client_id = request.user.username
        if not USER_TASK.__contains__(client_id):
            return JSONResponse({})
        resp = self.get_history()
        if resp.status_code == 200:
            history = resp.json()
            print(history)
            for k, v in USER_TASK[client_id].items():
                if history.__contains__(k):
                    result = StatusResponse(**history[k])
                    USER_TASK[client_id][k]["status"] = result.status
                    USER_TASK[client_id][k]["outputs"] = result.outputs
            save_user_task()
            return JSONResponse(USER_TASK[client_id])
    
    def get_history(self):
        return requests.get(f'{URL}/history')
    
class Video(HTTPEndpoint):
    async def get(self, request):
        assert request.query_params["filename"]
        resp = self.get_video(request.query_params["filename"])
        # print(resp)
        # with open(request.query_params["filename"], mode="wb") as f:
        #     f.write(resp.content)
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
