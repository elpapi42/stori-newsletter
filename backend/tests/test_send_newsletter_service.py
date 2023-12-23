import pytest

from source.domain.newsletter import Newsletter
from source.application.send_newsletter import SendNewsletterService
from source.adapters.newsletter_repository.fake import FakeNewsletterRepository
from source.adapters.newsletter_dispatcher.fake import FakeNewsletterDispatcher


@pytest.mark.asyncio
async def test_add_newsletter_file_service():
    fake_repo = FakeNewsletterRepository()
    fake_newsletter_dispatcher = FakeNewsletterDispatcher()
    service = SendNewsletterService(fake_repo, fake_newsletter_dispatcher)

    newsletter = Newsletter(title="Original Title")

    await fake_repo.add(newsletter)

    await service.execute(newsletter.id)

    assert fake_newsletter_dispatcher.hit_counter == 1
