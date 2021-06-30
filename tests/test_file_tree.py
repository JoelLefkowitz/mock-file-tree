import os
import pytest
from src.file_tree import MockFileTree


def test_mocked_builtins() -> None:
    MockFileTree("file1", "dir1/file2")

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

    assert os.listdir(".") == ["file1", "dir"]
    assert os.listdir("dir") == ["file2"]


def test_restore() -> None:
    tree = MockFileTree("file1")
    assert os.path.exists("file1")

    tree.restore()
    assert not os.path.exists("file1")


def test_context_manager() -> None:
    with MockFileTree("file1") as tree:
        assert isinstance(tree, MockFileTree)
        assert os.path.exists("file1")

    assert not os.path.exists("file1")


def test_safe() -> None:
    MockFileTree("file1", safe=True)

    with pytest.raises(NotImplementedError):
        os.remove("file1")
