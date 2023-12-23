from motor.motor_asyncio import AsyncIOMotorClient

from source.infrastructure import settings


client = AsyncIOMotorClient(settings.default.mongo_url, uuidRepresentation='standard')

default_db = client.backend

newsletters_collection = default_db.newsletters
