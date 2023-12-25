from dataclasses import dataclass
from uuid import UUID

from source.ports.newsletter_repository import NewsletterRepository
from source.ports.newsletter_dispatcher import NewsletterDispatcher
from source.infrastructure.logger import Logger
from source.application import exceptions


@dataclass
class SendNewsletterService():
    newsletter_repo: NewsletterRepository
    newsletter_dispatcher: NewsletterDispatcher

    async def execute(self, id: UUID) -> None:
        newsletter = await self.newsletter_repo.get(id)
        if newsletter is None:
            Logger.error("NewsletterToSendNotFound", newsletter_id=str(id))
            raise exceptions.NotFound(f"Newsletter with id {id} not found")

        await self.newsletter_dispatcher.dispatch(newsletter)

        Logger.info("NewsletterSent", newsletter_id=str(id))
