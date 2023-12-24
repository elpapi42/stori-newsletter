from dataclasses import dataclass
from uuid import UUID

from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import DESCENDING

from source.ports.newsletter_repository import NewsletterRepository
from source.domain.newsletter import Newsletter
from source.domain.email_address import EmailAddress
from source.infrastructure.mongo import newsletters_collection


@dataclass
class MongoNewsletterRepository(NewsletterRepository):
    collection: AsyncIOMotorCollection = newsletters_collection

    async def add(self, newsletter: Newsletter) -> None:
        await self.collection.update_one(
            {"_id": newsletter.id},
            {"$set": {
                **newsletter.model_dump(exclude={"id"}),
                "audience": [email.value for email in newsletter.audience],
            }},
            upsert=True
        )

    async def get(self, id: UUID) -> Newsletter | None:
        newsletter = await self.collection.find_one({"_id": id})
        if newsletter is None:
            return None

        return Newsletter(
            id=newsletter["_id"],
            title=newsletter["title"],
            audience=[EmailAddress(value=address) for address in newsletter["audience"]],
            body=newsletter["body"],
            file_uri=newsletter["file_uri"],
            created_at=newsletter["created_at"],
        )

    async def get_all(self) -> list[Newsletter]:
        newsletters = await self.collection.find(sort={ 'created_at': DESCENDING }).to_list(length=None)
        return [
            Newsletter(
                id=newsletter["_id"],
                title=newsletter["title"],
                audience=[EmailAddress(value=address) for address in newsletter["audience"]],
                body=newsletter["body"],
                file_uri=newsletter["file_uri"],
                created_at=newsletter["created_at"],
            )
            for newsletter in newsletters
        ]
