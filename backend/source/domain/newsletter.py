from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from source.domain.email_address import EmailAddress


class Newsletter(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    audience: list[EmailAddress] = []
    body: str = ""
    file_uri: str | None = None

    class Config:
        validate_assignment = True
