from pydantic import BaseModel
from typing import Optional
        
'''
model_name = prompt.json

'''
class PromptRequest(BaseModel):
    image_name: str  # 图片名称
    model_name: str
    width: int
    height: int
    video_frames: int
    fps: int
    motion_bucket_id: int
    steps:int


    

class TaskStatus(BaseModel):
    task_id: str
    status: str  # pending/processing/completed/failed
    result_url: Optional[str] = None