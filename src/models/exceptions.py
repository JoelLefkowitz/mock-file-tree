from typing import Any


class SubtreeNotFound(Exception):

    # We type the FileTree as Any here as a tradeoff. It lets us spearate out exceptions
    # into a standalone module and avoid a circular dependency without any import hacks.
    def __init__(self, path: str, tree: Any) -> None:
        super().__init__(
            f"Could not find the path: '{path}' in the file tree: '{tree}'."
        )
