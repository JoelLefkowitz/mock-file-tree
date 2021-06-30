from __future__ import annotations
from functools import partial
import os
import importlib
from types import TracebackType
from typing import Tuple, Optional, Type, List
from .support import block_unsupported


class MockFileTree:
    paths: Tuple[str, ...]

    def __init__(self, *paths: str, safe: bool = False) -> None:
        self.paths = paths
        self.patch()

        if safe:
            block_unsupported()

    def __enter__(self) -> MockFileTree:
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self.restore()

    def patch(self) -> None:
        os.listdir = partial(self.listdir, self)  # type: ignore
        os.path.exists = partial(self.path_exists, self)
        os.path.isdir = partial(self.path_isdir, self)
        os.path.isfile = partial(self.path_isfile, self)

    def restore(self) -> None:
        importlib.reload(os)

    def listdir(self, path: str) -> List[str]:
        return []

    def path_exists(self, path: str) -> bool:
        return True

    def path_isdir(self, path: str) -> bool:
        return True

    def path_isfile(self, path: str) -> bool:
        return True
