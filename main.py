from starlette.applications import Starlette
from routes import routes
from middlewares import middlewares
from model.db.connector import lifespan
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Starlette(debug=True, routes=routes, lifespan=lifespan, middleware=middlewares)

import task_scheduler
import asyncio
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
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(scheduler._main_loop())

@app.on_event("shutdown")
async def shutdown_event():
    await scheduler.shutdown()