# Mock file tree

A simple interface to mock the os module with a virtual file tree.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/mock-file-tree/review.yml)
![Version](https://img.shields.io/pypi/v/mock-file-tree)
![Downloads](https://img.shields.io/pypi/dw/mock-file-tree)
![Quality](https://img.shields.io/codacy/grade/f1ad5fa4cee24808afa66a5cf812c4ec)
![Coverage](https://img.shields.io/codacy/coverage/f1ad5fa4cee24808afa66a5cf812c4ec)

## Installing

```bash
pip install mock-file-tree
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/mock-file-tree).

## Usage

Create a virtual file tree:

```python
from mock_file_tree import FileTree

tree = FileTree.from_paths("file1", "dir1/file2")
```

Now we can import and overwrite the os module. This allows us to make all file interactions use our virtual tree.

```python
import os
from mock_file_tree import MockFileTree

with MockFileTree(os, tree):
     os.listdir(".")

['file1', 'dir1']
```

Similarly:

```python
os.listdir("dir1")

['file2']
```

And so on:

```python
os.path.isfile("dir1")

False
```

## Motivation

Mocking the file system is a typical task when writing unit tests. It is necessary to have a simple interface to declare paths to mock. It is not trivial to implement and so there has long been a need for an open source package to provide the functionality.

## Advanced

To mock file system without using a context manager:

```python
mock = MockFileTree(os, tree)
mock.apply()
```

And to restore the os module:

```python
mock.restore()
```

We would usually call the action of replacing methods in the os module as stubbing. However, the standard library refers to such tasks as mocking and so this package conforms to that naming scheme.

You may want to replace the os module with the stubbed methods only and explicitly restrict access to any un-stubbed methods that interact with the file system (analogous to replacing the os module with a fake). This can be achieved by setting the safe parameter:

```python
with MockFileTree(os, tree, safe=True):
     os.remove("file1")

... NotImplementedError
```

To cover all file system interactions the builtin 'open' function should be unset too.

## Roadmap

In models.unsupported there is a list of methods that interact with the file system that do not yet have mock implementations. Most notable are the methods that add and remove files from the file tree such as 'mkdir' and 'remove'.

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
