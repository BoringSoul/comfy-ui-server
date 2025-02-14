import requests
import random
import json

HOST = "99.79.37.130"
NORMAL_TOKEN = "dGFvOnBhc3N3b3JkOjEyMzM0NQ=="
VIP_TOKEN = "Y2hhcm06cGFzc3dvcmQ6MTIzMzQ1"
TOKENS =  [NORMAL_TOKEN, VIP_TOKEN]

def prompt():
    params = {
        "image_name":"IMG_0209.jpeg",
        "model_name": "svd",
        "steps":random.randint(2,10)
    }
    return requests.post(f"http://{HOST}:8000/task/prompt", json=json.dumps(params), headers={"Authorization": f'basic {random.choice(TOKENS)}'})

if __name__ == "__main__":
    for i in range(20):
        resp = prompt()
        print(resp.json())