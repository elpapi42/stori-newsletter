from source.ports.newsletter_dispatcher import NewsletterDispatcher
from source.domain.newsletter import Newsletter


class FakeNewsletterDispatcher(NewsletterDispatcher):
    async def dispatch(self, newsletter: Newsletter) -> None:
        pass
