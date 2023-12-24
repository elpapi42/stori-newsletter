from dataclasses import dataclass, field

from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo.errors import DuplicateKeyError

from source.domain.email_address import EmailAddress
from source.ports.unsubscribed_email_address_repository import UnsubscribedEmailAddressRepository
from source.infrastructure.mongo import unsubscribed_email_addresses_collection


@dataclass
class MongoUnsubscribedEmailAddressRepository(UnsubscribedEmailAddressRepository):
    collection: AsyncIOMotorCollection = unsubscribed_email_addresses_collection

    async def add(self, email_address: EmailAddress) -> None:
        try:
            await self.collection.insert_one({"_id": email_address.value})
        except DuplicateKeyError:
            pass

    async def is_unsubcribed(self, email_address: EmailAddress) -> bool:
        return await self.collection.find_one({"_id": email_address.value}) is not None
