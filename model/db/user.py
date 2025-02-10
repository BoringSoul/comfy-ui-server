
import sqlalchemy
from pydantic import BaseModel
from .connector import METADATA
import decimal
from datetime import datetime
from .connector import DB
from typing import List

class User(BaseModel):
    id: int
    username: str
    email: str
    mobile: str
    pwd: str
    api_token: str
    balance: decimal.Decimal
    register_time: datetime | None

users = sqlalchemy.Table(
    "user",
    METADATA,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("mobile", sqlalchemy.String),
    sqlalchemy.Column("pwd", sqlalchemy.String),
    sqlalchemy.Column("api_token", sqlalchemy.String),
    sqlalchemy.Column("balance", sqlalchemy.Numeric),
    sqlalchemy.Column("register_time", sqlalchemy.DateTime),
)

async def add_user(user:BaseModel):
    await DB.execute(users.insert().values(**user.model_dump()))

async def find_by_username(username:str) -> List:
    result = await DB.fetch_all(users.select().where(users.c.username == username))
    return [User(**item) for item in result]