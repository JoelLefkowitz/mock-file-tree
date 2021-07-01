import os
from dataclasses import dataclass
from typing import List

from ..utils.paths import child_paths, path_base, path_from_base
from .exceptions import SubtreeNotFound


@dataclass
class FileTree:
    base: str
    children: List["FileTree"]

    @classmethod
    def from_paths(cls, *paths: str, base: str = ".") -> "FileTree":
        return cls(
            base,
            [
                cls.from_paths(*child_paths(i, list(paths)), base=i)
                for i in set(path_base(j) for j in paths)
            ],
        )

    def is_descendant(self, path: str) -> bool:
        path = os.path.normpath(path)
        return (
            path == self.base
            or path in [i.base for i in self.children]
            or any(i.is_descendant(path_from_base(path)) for i in self.children)
        )

    def get_descendant(self, path: str) -> "FileTree":
        if not self.is_descendant(path):
            raise SubtreeNotFound(path, self)

        path = os.path.normpath(path)

        if path == self.base:
            return self

        if path in [i.base for i in self.children]:
            return next(filter(lambda x: x.base == path, self.children))

        return next(
            i.get_descendant(path_from_base(path))
            for i in self.children
            if i.is_descendant(path_from_base(path))
        )

    def listdir(self, path: str = ".") -> List[str]:
        return [i.base for i in self.get_descendant(path).children]

    def path_exists(self, path: str) -> bool:
        return self.is_descendant(path)

    def path_isdir(self, path: str) -> bool:
        return self.is_descendant(path) and len(self.get_descendant(path).children) > 0

    def path_isfile(self, path: str) -> bool:
        return self.is_descendant(path) and len(self.get_descendant(path).children) == 0
