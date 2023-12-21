from abc import ABC, abstractmethod
from io import IOBase


class FileStorage(ABC):
    @abstractmethod
    async def save(self, id: str, file: IOBase, ext: str) -> str:
        """Returns the file URI"""
        raise NotImplementedError

    @abstractmethod
    async def get_by_uri(self, uri: str) -> IOBase:
        """Returns file-like object"""
        raise NotImplementedError
