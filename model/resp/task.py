from pydantic import BaseModel

class PromptResponse(BaseModel):
    prompt_id: str 
    number: int
    node_errors: dict

class QueueResponese(BaseModel):
    queue_running: list
    queue_pending: list

class StatusResponse(BaseModel):
    status: dict
    outputs: dict