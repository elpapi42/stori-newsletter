from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from source.adapters.scripts.scheduled_newsletters_sender import ScheduledNewslettersSender
from source.adapters.controllers.newsletter import router as newsletter_router
from source.adapters.controllers.unsubscribe_email_address import router as unsubscribe_email_address_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    background_newsletter_sender = ScheduledNewslettersSender()
    await background_newsletter_sender.start()

    yield

    await background_newsletter_sender.stop()


app = FastAPI(lifespan=lifespan)


app.include_router(newsletter_router)
app.include_router(unsubscribe_email_address_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
