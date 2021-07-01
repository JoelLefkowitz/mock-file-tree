import os
from typing import List


def path_base(path: str) -> str:
    """
    >>> path_base('/dir1/dir2/file1.ext')
    ''

    >>> path_base('dir1/dir2/file1.ext')
    'dir1'
    """
    return os.path.normpath(path).split(os.sep)[0]


def path_from_base(path: str) -> str:
    """
    >>> path_from_base('/dir1/dir2/file1.ext')
    'dir1/dir2/file1.ext'

    >>> path_from_base('dir1/dir2/file1.ext')
    'dir2/file1.ext'
    """
    return path[1:] if path_base(path) == "" else os.path.relpath(path, path_base(path))


def child_paths(base: str, paths: List[str]) -> List[str]:
    """
    >>> child_paths('dir1', ['file1', 'dir1/file2'])
    ['file2']
    """
    return [
        path_from_base(j)
        for j in paths
        if path_base(j) == base and path_from_base(j) != "."
    ]
