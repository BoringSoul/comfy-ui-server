from starlette.applications import Starlette
from routes import routes
from middlewares import middlewares
from model.db.connector import lifespan
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Starlette(debug=True, routes=routes, lifespan=lifespan, middleware=middlewares)

import task_scheduler

@app.on_event("startup")
async def startup_event():
    # create scheduler
    app.state.scheduler = AsyncIOScheduler()
    '''
    add job
    interval = 5 seconds
    ''' 
    app.state.scheduler.add_job(task_scheduler.handle_pending_tasks, 'interval', seconds=5)
    app.state.scheduler.add_job(task_scheduler.update_unfinished_tasks, 'interval', seconds=10)

    # start scheduler
    app.state.scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    app.state.scheduler.shutdown()