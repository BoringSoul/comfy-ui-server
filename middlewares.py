from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser
)
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
import base64
import model.db.user as user_query
from starlette.responses import JSONResponse


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        exclude = ["/user/login", "/user/register", "/api/user/login", "/api/user/register"]
        if conn.url.path in exclude:
            return
        if "Authorization" not in conn.headers:
            return

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("utf-8")
        except Exception as exc:
            raise AuthenticationError(f'Invalid basic auth credentials:{exc}')
        username, auth_type, credentials = decoded.split(":")
        user = await user_query.find_by_username(username)
        if not user or not self.validate(user, auth_type, credentials):
            return AuthCredentials(["failed"]), SimpleUser(username)
        return AuthCredentials(["authenticated", "normal" if not user.balance or user.balance == 0  else "vip"]), SimpleUser(username)
    
    def validate(self, user, auth_type, credential):
        if auth_type == 'password':
            return user.pwd == credential
        elif auth_type == 'api_token' :
            return user.api_token == credential
        return False

class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            # 自定义错误响应
            return JSONResponse(
                status_code=500,
                content={"error": "Internal Server Error", "detail": str(exc)}
            )

middlewares = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend()),
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*']),
    Middleware(GlobalExceptionMiddleware)
]
