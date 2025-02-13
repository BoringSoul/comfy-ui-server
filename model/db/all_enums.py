from enum import Enum

class TaskStatus(Enum):
    PENDING = -1
    RUNNING = 0
    INTERUPTED = 1
    DONE = 2

class UserType(Enum):
    NORMAL = 0
    VIP = 1