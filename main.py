from starlette.applications import Starlette
from routes import routes
from middlewares import middlewares
from model.db.connector import lifespan

app = Starlette(debug=True, routes=routes, lifespan=lifespan, middleware=middlewares)