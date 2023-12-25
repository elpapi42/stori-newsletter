import asyncio
from datetime import datetime, timezone
from traceback import format_exc

from source.application.send_newsletter import SendNewsletterService
from source.application.send_scheduled_newsletters import SendScheduledNewslettersService
from source.adapters.newsletter_repository.mongo import MongoNewsletterRepository
from source.adapters.file_storage.local import LocalFileStorage
from source.adapters.newsletter_dispatcher.ses import SESNewsletterDispatcher
from source.adapters.unsubscribed_email_address_repository.mongo import MongoUnsubscribedEmailAddressRepository
from source.infrastructure.logger import Logger


class ScheduledNewslettersSender:
    def __init__(self):
        file_storage = LocalFileStorage()
        unsubscribed_email_address_repo = MongoUnsubscribedEmailAddressRepository()
        self.newsletter_repo = MongoNewsletterRepository()
        self.newsletter_dispatcher = SESNewsletterDispatcher(file_storage, unsubscribed_email_address_repo)
        self.send_newsletter_service = SendNewsletterService(self.newsletter_repo, self.newsletter_dispatcher)
        self.send_scheduled_newsletters_service = SendScheduledNewslettersService(self.newsletter_repo, self.send_newsletter_service)

        self.task = None
        self.should_run = False

    async def start(self):
        self.should_run = True
        self.task = asyncio.create_task(self.run())

    async def run(self):
        try:
            while self.should_run:
                current_timestamp = datetime.utcnow()
                await self.send_scheduled_newsletters_service.execute(current_timestamp)
                await asyncio.sleep(60)
        except Exception as e:
            Logger.error(
                "ScheduledNewslettersSenderCrashed",
                error=str(e),
                traceback=format_exc()
            )

    async def stop(self):
        self.should_run = False
        await self.task
