from pydantic import BaseModel
from typing import Optional
        
'''
model_name = prompt.json

'''
class PromptRequest(BaseModel):
    image_name: str  # 图片名称
    model_name: str
    width: Optional[int] = None
    height: Optional[int] = None
    video_frames: Optional[int] = None
    fps: Optional[int] = None
    motion_bucket_id: Optional[int] = None
    steps: Optional[int] = None
