import contextlib

import databases
import sqlalchemy
from starlette.config import Config


# Configuration from environment variables or '.env' file.
config = Config('.env')
DATABASE_URL = config('DATABASE_URL')
DB = databases.Database(DATABASE_URL)

@contextlib.asynccontextmanager
async def lifespan(app):
    await DB.connect()
    yield
    await DB.disconnect()



# Database table definitions.
METADATA = sqlalchemy.MetaData()

