from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from source.adapters.controllers.newsletter import router as newsletter_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(newsletter_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
