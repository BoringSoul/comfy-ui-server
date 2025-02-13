
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
    update_time: datetime | None

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
    sqlalchemy.Column("end_time", sqlalchemy.DateTime),
    sqlalchemy.Column("update_time", sqlalchemy.DateTime),
)

def format_datetime(data:dict):
    data["start_time"] = data["start_time"].isoformat()
    data["end_time"] = data["end_time"].isoformat()
    data["update_time"] = data["update_time"].isoformat()
    return data

async def save_task(user_task:dict) -> None:
    print(f'save task: {user_task}')
    await DB.execute(user_tasks.insert().values(**user_task))
async def find_pending_tasks() -> List:
    return await DB.fetch_all(user_tasks.select().where(user_tasks.c.status == TaskStatus.PENDING.value))

async def delete_pending_tasks(client_id:str):
    return await DB.execute(user_tasks.delete()
                            .where(user_tasks.c.client_id == client_id)
                            .where(user_tasks.c.status == TaskStatus.PENDING.value))

async def delete_pending_task(task_id:str):
    return await DB.execute(user_tasks.delete()
                            .where(user_tasks.c.task_id == task_id)
                            .where(user_tasks.c.status == TaskStatus.PENDING.value))

async def find_unfinished_tasks() -> List:
    return await DB.fetch_all(user_tasks.select().where(user_tasks.c.status.in_([TaskStatus.RUNNING.value, TaskStatus.PENDING.value])))

async def find_unfinished_by_client_id(client_id:str) -> List:
    lst = await DB.fetch_all(user_tasks
                            .select()
                            .where(user_tasks.c.client_id == client_id)
                            .where(user_tasks.c.status.in_([TaskStatus.RUNNING.value, TaskStatus.PENDING.value]))
                            .order_by(user_tasks.c.start_time.desc()))
    return None if not lst else [format_datetime(UserTask(**item).model_dump()) for item in lst]

async def find_by_task_id(task_id:str) -> dict:
    i = await DB.fetch_one(user_tasks.select().where(user_tasks.c.task_id == task_id))
    return None if not i else format_datetime(UserTask(**i).model_dump())

async def find_by_client_id(client_id:str) -> List:
    lst = await DB.fetch_all(user_tasks.select().where(user_tasks.c.client_id == client_id))
    return None if not lst else [format_datetime(UserTask(**item).model_dump()) for item in lst]

async def find_running_tasks(client_id:str) -> List:
    lst = await DB.fetch_all(user_tasks.select()
                             .where(user_tasks.c.client_id == client_id)
                             .where(user_tasks.c.status == TaskStatus.RUNNING.value))
    return None if not lst else [format_datetime(UserTask(**item).model_dump()) for item in lst]

async def update_user_task(user_task:dict) -> None:
    await DB.execute(user_tasks.update().where(user_tasks.c.task_id == user_task["task_id"]).values(**user_task))