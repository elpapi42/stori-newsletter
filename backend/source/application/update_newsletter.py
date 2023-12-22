from dataclasses import dataclass
from uuid import UUID

from source.domain.email_address import EmailAddress
from source.ports.newsletter_repository import NewsletterRepository
from source.application import exceptions


@dataclass
class UpdateNewsletterService():
    newsletter_repo: NewsletterRepository

    async def execute(self, id: UUID, title: str, audience: list[str], body: str) -> None:
        newsletter = await self.newsletter_repo.get(id)
        if newsletter is None:
            raise exceptions.NotFound(f"Newsletter with id {id} not found")

        newsletter.title = title
        newsletter.audience = [EmailAddress(value=email) for email in audience]
        newsletter.body = body

        await self.newsletter_repo.update(newsletter)
