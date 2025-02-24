import contextlib

import databases
import sqlalchemy
from starlette.config import Config

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import task_scheduler



# Configuration from environment variables or '.env' file.
config = Config('.env')
DATABASE_URL = config('DATABASE_URL')
DB = databases.Database(DATABASE_URL)

@contextlib.asynccontextmanager
async def lifespan(app):
     # create scheduler
    scheduler = AsyncIOScheduler()
    '''
    add job
    interval = 5 seconds
    ''' 
    scheduler.add_job(task_scheduler.handle_pending_tasks, 'interval', seconds=5)
    scheduler.add_job(task_scheduler.update_unfinished_tasks, 'interval', seconds=10)

    # start scheduler
    scheduler.start()
    await DB.connect()
    yield
    await DB.disconnect()
    scheduler.shutdown()



# Database table definitions.
METADATA = sqlalchemy.MetaData()

