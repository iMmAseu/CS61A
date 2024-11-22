from collections.abc import Iterator
from os import PathLike
from typing import Any
from typing import IO

from .headers import Headers
from .structures import MultiDict

class FileStorage:
    name: str | None
    stream: IO[bytes]
    filename: str | None
    headers: Headers
    _parsed_content_type: tuple[str, dict[str, str]]
    def __init__(
        self,
        stream: IO[bytes] | None = None,
        filename: str | PathLike | None = None,
        name: str | None = None,
        content_type: str | None = None,
        content_length: int | None = None,
        headers: Headers | None = None,
    ) -> None: ...
    def _parse_content_type(self) -> None: ...
    @property
    def content_type(self) -> str: ...
    @property
    def content_length(self) -> int: ...
    @property
    def mimetype(self) -> str: ...
    @property
    def mimetype_params(self) -> dict[str, str]: ...
    def save(self, dst: str | PathLike | IO[bytes], buffer_size: int = ...) -> None: ...
    def close(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __getattr__(self, name: str) -> Any: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __repr__(self) -> str: ...

class FileMultiDict(MultiDict[str, FileStorage]):
    def add_file(
        self,
        name: str,
        file: FileStorage | str | IO[bytes],
        filename: str | None = None,
        content_type: str | None = None,
    ) -> None: ...
