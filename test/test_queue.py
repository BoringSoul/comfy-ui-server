import requests
import random
import json

HOST = "localhost"
NORMAL_TOKEN = "dGFvOnBhc3N3b3JkOjEyMzM0NQ=="
VIP_TOKEN = "Y2hhcm06cGFzc3dvcmQ6MTIzMzQ1"
TOKENS =  [NORMAL_TOKEN, VIP_TOKEN]

def prompt():
    params = {
        "image_name":"IMG_0209.jpeg",
        "model_name": "sdxl_lcm",
        "steps":random.randint(2,10)
    }
    return requests.post(f"http://{HOST}:8000/api/task/prompt", json=json.dumps(params), headers={"Authorization": f'basic {random.choice(TOKENS)}'})

if __name__ == "__main__":
    for i in range(1):
        resp = prompt()
        print(resp.json())