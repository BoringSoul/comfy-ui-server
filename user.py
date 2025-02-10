from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from model.request import user
from model.db.user import *

import base64


class Register(HTTPEndpoint):
    async def post(self, request):
        data = await request.json()
        add_user(user.RegisterRequest(**data))


class Login(HTTPEndpoint):
    async def post(self, request):
        data = await request.json()
        user = await self.validate(**data)
        if user:
            return JSONResponse({"token": self.parse_token(**data)})
        return JSONResponse({"code": 500, "msg":"validate failed"})

    async def validate(self, username:str, auth_type:str, credential:str) -> bool:
        users = await find_by_username(username=username)
        if users:
            return users[0]
        return None

    def parse_token(self, username:str, auth_type:str, credential:str):
        return base64.b64encode(f'Bearer {username}:{auth_type}:{credential}'.encode()).decode('utf8')

routes = [
    Route("/register", Register),
    Route("/login", Login),
]
