from pydantic import BaseModel
from typing import Optional
class PromptResponse(BaseModel):
    task_id: str 
    number: int
    node_errors: dict
    prompt_id: Optional[str] = None

class QueueResponese(BaseModel):
    queue_running: list
    queue_pending: list

class StatusResponse(BaseModel):
    status: dict
    outputs: dict