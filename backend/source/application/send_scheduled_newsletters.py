import asyncio
from dataclasses import dataclass
from datetime import datetime

from source.ports.newsletter_repository import NewsletterRepository
from source.application.send_newsletter import SendNewsletterService
from source.infrastructure.logger import Logger


@dataclass
class SendScheduledNewslettersService():
    newsletter_repo: NewsletterRepository
    send_newsletter_service: SendNewsletterService

    async def execute(self, timestamp: datetime) -> None:
        newsletters = await self.newsletter_repo.get_scheduled_for_timestamp(timestamp)

        if len(newsletters) == 0:
            return

        Logger.info(
            f"ScheduledNewslettersFound",
            count=len(newsletters),
            newsletters=[str(newsletter.id) for newsletter in newsletters]
        )

        await asyncio.gather(*[
            self.send_newsletter_service.execute(newsletter.id) 
            for newsletter in newsletters
        ])

        for newsletter in newsletters:
            newsletter.scheduled_at = None

        # TODO: Create a .add_batch() method in the repository
        asyncio.gather(*[
            self.newsletter_repo.add(newsletter)
            for newsletter in newsletters
        ])
