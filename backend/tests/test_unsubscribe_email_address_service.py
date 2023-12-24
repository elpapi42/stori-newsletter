import pytest
from uuid import UUID

from source.domain.email_address import EmailAddress
from source.application.unsubscribe_email_address import UnsubscribeEmailAddressService
from source.adapters.unsubscribed_email_address_repository.fake import FakeUnsubscribedEmailAddressRepository


@pytest.mark.asyncio
async def test_unsubscribe_email_address_service():
    fake_repo = FakeUnsubscribedEmailAddressRepository()
    service = UnsubscribeEmailAddressService(fake_repo)

    email = "example@example.com"

    await service.execute(email)

    assert await fake_repo.is_unsubcribed(EmailAddress(value=email))
