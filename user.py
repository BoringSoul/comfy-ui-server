from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from model.db.user import *
from model.db.all_enums import UserType

import base64


class Register(HTTPEndpoint):
    async def post(self, request):
        data = await request.json()
        await add_user(data)
        return JSONResponse({"code": 200, "msg":"success"})


class Login(HTTPEndpoint):
    async def post(self, request):
        data = await request.json()
        user = await self.validate(**data)
        if user:
            return JSONResponse({"token": self.parse_token(**data), "user_type": UserType.VIP.value if user.balance and user.balance > 0 else UserType.NORMAL.value})
        return JSONResponse({"code": 500, "msg":"validate failed"})

    async def validate(self, username:str, auth_type:str, credential:str) -> bool:
        user = await find_by_username(username=username)
        if not user:
            return None
        if auth_type == 'password' and user.pwd == credential:
            return user
        elif auth_type == 'api_token' and user.api_token == credential:
            return user
        return None

    def parse_token(self, username:str, auth_type:str, credential:str):
        return f'{base64.b64encode(bytes(f'{username}:{auth_type}:{credential}', 'utf-8')).decode('utf-8')}'

routes = [
    Route("/register", Register),
    Route("/login", Login),
]
