from dataclasses import dataclass

from source.ports.newsletter_dispatcher import NewsletterDispatcher
from source.domain.newsletter import Newsletter


@dataclass
class FakeNewsletterDispatcher(NewsletterDispatcher):
    hit_counter: int = 0

    async def dispatch(self, newsletter: Newsletter) -> None:
        self.hit_counter += 1
