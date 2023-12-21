import os
from uuid import uuid4
from dataclasses import dataclass
from io import IOBase

from source.ports.file_storage import FileStorage
from source.infrastructure import settings


@dataclass
class LocalFileStorage(FileStorage):
    storage_path: str = settings.default.local_storage_path

    async def save(self, id: str, file: IOBase, ext: str) -> str:
        file_path = os.path.join(self.storage_path, f"{id}:{uuid4().hex}.{ext}")
        with open(file_path, 'wb') as local_file:
            while True:
                batch = file.readline()
                if not batch:
                    break
                local_file.write(batch)
        return file_path

    async def get_by_uri(self, uri: str) -> IOBase:
        return open(uri, 'rb')
