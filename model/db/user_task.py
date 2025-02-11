
import sqlalchemy
from pydantic import BaseModel
from typing import Optional
from .connector import METADATA
from datetime import datetime
from .connector import DB
from typing import List
from enum import Enum

class UserTask(BaseModel):
    task_id: str
    client_id: str
    user_type:int
    prompt_id: Optional[str]
    server_ip: Optional[str]
    inputs: str
    outputs: Optional[str]
    status: int
    start_time: datetime | None
    end_time: datetime | None

class TaskStatus(Enum):
    PENDING = -1
    RUNNING = 0
    INTERUPTED = 1
    DONE = 2

class UserType(Enum):
    NORMAL = 0
    VIP = 1

user_tasks = sqlalchemy.Table(
    "user_task",
    METADATA,
    sqlalchemy.Column("task_id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("client_id", sqlalchemy.String),
    sqlalchemy.Column("user_type", sqlalchemy.Integer),
    sqlalchemy.Column("prompt_id", sqlalchemy.String),
    sqlalchemy.Column("server_ip", sqlalchemy.String),
    sqlalchemy.Column("inputs", sqlalchemy.String),
    sqlalchemy.Column("outputs", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.Integer),
    sqlalchemy.Column("start_time", sqlalchemy.DateTime),
    sqlalchemy.Column("start_time", sqlalchemy.DateTime),
)

async def save_task(user_task:dict) -> None:
    await DB.execute(user_tasks.insert().values(**user_task))
async def find_pending_tasks() -> List:
    return await DB.fetch_all(user_tasks.select().where(user_tasks.c.status == TaskStatus.PENDING.value))

async def find_unfinished_tasks() -> List:
    return await DB.fetch_all(user_tasks.select().where(user_tasks.c.status == TaskStatus.PENDING.value or user_tasks.c.status == TaskStatus.RUNNING.value))

async def find_unfinished_by_client_id(client_id:str) -> List:
    return await DB.fetch_all(user_tasks.select().where(user_tasks.c.client_id == client_id and (user_tasks.c.status == TaskStatus.PENDING.value or user_tasks.c.status == TaskStatus.RUNNING.value)))

async def find_by_client_id(client_id:str) -> List:
    return await DB.fetch_all(user_tasks.select().where(user_tasks.c.client_id == client_id))