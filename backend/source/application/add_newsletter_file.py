from dataclasses import dataclass
from uuid import UUID
from io import IOBase

from source.ports.newsletter_repository import NewsletterRepository
from source.ports.file_storage import FileStorage


@dataclass
class AddNewsletterFileService():
    newsletter_repo: NewsletterRepository
    file_storage: FileStorage

    async def execute(self, newsletter_id: UUID, file: IOBase, ext: str) -> None:
        newsletter = await self.newsletter_repo.get(newsletter_id)

        file_uri = await self.file_storage.save(str(newsletter.id), file, ext)

        newsletter.file_uri = file_uri

        await self.newsletter_repo.update(newsletter)
