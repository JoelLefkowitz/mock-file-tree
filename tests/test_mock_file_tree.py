import os

import pytest

from src.models.file_tree import FileTree
from src.models.mock_file_tree import MockFileTree


# These assertions are duplicated by those in test_file_tree.py.
# They are kept here as a necessary sanity check.
def test_builtins() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")
    MockFileTree(os, tree).apply()

    assert os.path.exists("file1")
    assert os.path.exists("dir1")
    assert os.path.exists("dir1/file2")
    assert not os.path.exists("file2")

    assert os.path.isfile("file1")
    assert not os.path.isfile("dir1")
    assert os.path.isfile("dir1/file2")
    assert not os.path.isfile("file2")

    assert not os.path.isdir("file1")
    assert os.path.isdir("dir1")
    assert not os.path.isdir("dir1/file2")
    assert not os.path.isdir("file2")

    assert sorted(os.listdir(".")) == ["dir1", "file1"]
    assert sorted(os.listdir("dir1")) == ["file2"]


def test_context_manager() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")

    with MockFileTree(os, tree) as mock:
        assert isinstance(mock, MockFileTree)
        assert os.path.exists("file1")

    assert not os.path.exists("file1")

    # We include a test for the safe=True behavior here since it
    # saves implementing an explicit teardown method to restore
    # the os module (which our test runners rely on).
    with MockFileTree(os, tree, safe=True):
        with pytest.raises(NotImplementedError):
            os.remove("file1")
