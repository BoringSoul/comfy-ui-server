from pydantic import BaseModel
from typing import Optional

class RegisterRequest(BaseModel):
    username: str
    pwd: str


    

class LoginRequest(BaseModel):
    username: str
    auth_type: str  
    credential: str