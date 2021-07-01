# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name

from __future__ import annotations

import os
import importlib
from types import TracebackType
from typing import List, Optional, Type, Any

from .support import block_unsupported


class MockFileTree:
    paths: List[str]

    def __init__(self, os: Any, *paths: str, safe: bool = False) -> None:
        self.paths = [os.path.normpath(i) for i in paths]

        if safe:
            block_unsupported(os)

        os.listdir = self.listdir
        os.path.exists = self.path_exists
        os.path.isdir = self.path_isdir
        os.path.isfile = self.path_isfile

    def __enter__(self) -> MockFileTree:
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self.restore()

    def restore(self) -> None:
        importlib.reload(os)
        importlib.reload(os.path)

    def listdir(self, path: Optional[str] = None) -> List[str]:
        path = os.path.normpath(path) if path is not None else "."
        return []

    def path_exists(self, path: str) -> bool:
        return True

    def path_isdir(self, path: str) -> bool:
        return True

    def path_isfile(self, path: str) -> bool:
        return True
