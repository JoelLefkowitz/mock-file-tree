# pylint: disable=invalid-name
# pylint: disable=unused-variable
from typing import Any, NoReturn


def not_implemented(*args: Any, **kwargs: Any) -> NoReturn:
    raise NotImplementedError()


# Methods that interact with the file system that don't get
# have mock implementations:
os_unsupported = [
    "access",
    "chdir",
    "chflags",
    "chmod",
    "chown",
    "chroot",
    "lchflags",
    "lchmod",
    "lchown",
    "lstat",
    "mkdir",
    "mkfifo",
    "mknod",
    "open",
    "pathconf",
    "readlink",
    "remove",
    "rmdir",
    "scandir",
    "stat",
    "statvfs",
    "truncate",
    "unlink",
    "utime",
]

os_path_unsupported = [
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
    "islink",
    "ismount",
    "lexists",
]
