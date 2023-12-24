from dataclasses import dataclass
from io import IOBase, BytesIO

from source.ports.file_storage import FileStorage


@dataclass
class FakeFileStorage(FileStorage):
    async def save(self, id: str, file: IOBase, ext: str) -> str:
        return "/dummy/uri"

    async def get_by_uri(self, uri: str) -> IOBase | None:
        return BytesIO(b"dummy file content")
