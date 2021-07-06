# Mock file tree

A simple interface to mock the os module with a virtual file tree.

## Status

| Source     | Shields                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield] ![lines][lines_shield] ![languages][languages_shield]                                   |
| Health     | ![codacy][codacy_shield] ![readthedocs][readthedocs_shield] ![github_review][github_review_shield] ![codacy_coverage][codacy_coverage_shield] |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]                   |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]                                      |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]                            |

## Installing

```bash
pip install mock-file-tree
```

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

## Tests

To run unit tests and generate a coverage report:

```bash
grunt test
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To use quickdocs to generate a sphinx documentation configuration:

```bash
grunt docs
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

## Continuous integration

This repository uses github actions to lint and test each commit. Formatting tasks and writing/generating documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Public links -->

[semver]: http://semver.org/

<!-- External links -->

[readthedocs]: https://mock-file-tree.readthedocs.io/en/latest/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[author]: https://github.com/joellefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/mock-file-tree
[license_shield]: https://img.shields.io/github/license/joellefkowitz/mock-file-tree
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/mock-file-tree
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/mock-file-tree

<!-- Health shields -->

[codacy_shield]: https://img.shields.io/codacy/grade/f1ad5fa4cee24808afa66a5cf812c4ec
[readthedocs_shield]: https://img.shields.io/readthedocs/mock-file-tree
[github_review_shield]: https://img.shields.io/github/workflow/status/joellefkowitz/mock-file-tree/Review
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/f1ad5fa4cee24808afa66a5cf812c4ec

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/mock-file-tree
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/mock-file-tree
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/mock-file-tree
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/mock-file-tree

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/mock-file-tree
[python_versions_shield]: https://img.shields.io/pypi/pyversions/mock-file-tree
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/mock-file-tree

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/mock-file-tree
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/mock-file-tree
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/mock-file-tree
