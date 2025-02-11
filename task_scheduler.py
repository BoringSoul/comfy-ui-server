'''
队列任务调度
'''

import requests
import json

'''
check  comfy ui server is free
'''
def server_free(host:str) -> bool:
    resp = requests.get(f"http://{host}:8188/queue")
    return resp.status_code == 200 and resp.json()["queue_running"] == [] 

'''
submit prompt to comfy ui server
'''
def prompt(host:str, client_id:str, prompt:dict):
    return requests.post(f'{host}:8188/prompt', json.dumps({
        "client_id": client_id,
        "prompt": prompt
    }))

def update_user_task(user_task:dict):
    pass
        


def get_history(host:str):
    return requests.get(f"http://{host}:8188/history")