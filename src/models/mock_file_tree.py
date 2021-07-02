# pylint: disable=invalid-name

import importlib
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Optional, Type

from .file_tree import FileTree
from .unsupported import not_implemented, os_path_unsupported, os_unsupported


@dataclass
class MockFileTree:
    os: Any
    tree: FileTree
    safe: bool = False

    def __enter__(self) -> "MockFileTree":
        self.apply()
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self.restore()

    def apply(self) -> None:
        self.os.listdir = self.tree.listdir
        self.os.path.exists = self.tree.path_exists
        self.os.path.isdir = self.tree.path_isdir
        self.os.path.isfile = self.tree.path_isfile

        if self.safe:
            for i in os_unsupported:
                setattr(self.os, i, not_implemented)

            for i in os_path_unsupported:
                setattr(self.os.path, i, not_implemented)

    def restore(self) -> None:
        importlib.reload(self.os)
        importlib.reload(self.os.path)
