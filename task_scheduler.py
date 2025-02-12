'''
队列任务调度
'''

import requests
import json
from datetime import datetime
from model.db.user_task import *
from prompt_map import *
from collections import defaultdict
from model.req.task import PromptRequest


'''
check  comfy ui server is free
'''

def get_servers() -> List:
    return ["99.79.37.130"]

def server_free(host:str) -> bool:
    resp = requests.get(f"http://{host}:8188/queue")
    return resp.status_code == 200 and resp.json()["queue_running"] == [] 

'''
submit prompt to comfy ui server
'''
def prompt(host:str, client_id:str, prompt:dict):
    return requests.post(f'http://{host}:8188/prompt', json.dumps({
        "client_id": client_id,
        "prompt": prompt
    }))


'''
get tasks history from server
'''
def get_history(host:str):
    return requests.get(f"http://{host}:8188/history")

def group_task_by_user_type(tasks:List):
    user_tasks = defaultdict(list)
    for task in tasks:
        user_tasks[task["user_type"]].append(task)
    return user_tasks

async def handle_pending_tasks():
    tasks = await find_pending_tasks()
    if not tasks:
        return
    available_servers = [server for server in get_servers() if server_free(server)]
    if not available_servers:
        return
    group_tasks = group_task_by_user_type(tasks)
    while len(available_servers) > 0:
        server = available_servers.pop()
        task = None
        if group_tasks.__contains__(UserType.VIP.value) and len(group_tasks[UserType.VIP.value]) > 0:
            task = group_tasks[UserType.VIP.value].pop()
        else:
            task = group_tasks[UserType.NORMAL.value].pop() if len(group_tasks[UserType.NORMAL.value]) > 0 else None
        if task:
            inputs = task["inputs"].replace("'", '"')
            target_prompt = get_prompt(PromptRequest(**json.loads(inputs)))
            resp = prompt(server, task["client_id"], target_prompt)
            if resp.status_code == 200:
                update_task = {
                    "task_id": task["task_id"],
                    "prompt_id": resp.json()["prompt_id"],
                    "server_ip": server,
                    "status": TaskStatus.RUNNING.value,
                    "update_time": datetime.now()
                }
                await update_user_task(update_task)

