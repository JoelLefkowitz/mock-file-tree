import pytest
from src.models.exceptions import SubtreeNotFound
from src.models.file_tree import FileTree


def test_from_paths() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2", "dir1/file3")
    assert sorted([i.base for i in tree.children]) == ["dir1", "file1"]

    dir1 = next(filter(lambda x: x.base == "dir1", tree.children))
    assert sorted([i.base for i in dir1.children]) == ["file2", "file3"]


def test_is_descendant() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")
    assert tree.is_descendant("file1")
    assert tree.is_descendant("dir1/file2")
    assert not tree.is_descendant("file2")


def test_get_descendant() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")

    file1 = tree.get_descendant("file1")
    assert isinstance(file1, FileTree)
    assert file1.base == "file1"

    file2 = tree.get_descendant("dir1/file2")
    assert isinstance(file2, FileTree)
    assert file2.base == "file2"

    with pytest.raises(SubtreeNotFound):
        tree.get_descendant("file2")


def test_listdir() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")
    assert sorted(tree.listdir(".")) == ["dir1", "file1"]
    assert sorted(tree.listdir("dir1")) == ["file2"]


def test_path_exists() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")
    assert tree.path_exists("file1")
    assert tree.path_exists("dir1")
    assert tree.path_exists("dir1/file2")
    assert not tree.path_exists("file2")


def test_path_isdir() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")
    assert not tree.path_isdir("file1")
    assert tree.path_isdir("dir1")
    assert not tree.path_isdir("dir1/file2")
    assert not tree.path_isdir("file2")


def test_path_isfile() -> None:
    tree = FileTree.from_paths("file1", "dir1/file2")
    assert tree.path_isfile("file1")
    assert not tree.path_isfile("dir1")
    assert tree.path_isfile("dir1/file2")
    assert not tree.path_isfile("file2")
