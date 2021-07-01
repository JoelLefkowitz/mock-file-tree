# pylint: disable=invalid-name
# pylint: disable=unused-variable
# pylint: disable=redefined-builtin
from typing import Any, NoReturn


def not_supported(*args: Any, **kwargs: Any) -> NoReturn:
    raise NotImplementedError()

# We can't do this as a loop as we're redefining the variables.
def block_unsupported(os: Any) -> None:
    open = not_supported
    os.access = not_supported
    os.chdir = not_supported
    os.chflags = not_supported
    os.chmod = not_supported
    os.chown = not_supported
    os.chroot = not_supported
    os.lchflags = not_supported
    os.lchmod = not_supported
    os.lchown = not_supported
    os.lstat = not_supported
    os.mkdir = not_supported
    os.mkfifo = not_supported
    os.mknod = not_supported
    os.open = not_supported
    os.path.getatime = not_supported
    os.path.getctime = not_supported
    os.path.getmtime = not_supported
    os.path.getsize = not_supported
    os.path.islink = not_supported
    os.path.ismount = not_supported
    os.path.lexists = not_supported
    os.pathconf = not_supported
    os.readlink = not_supported
    os.remove = not_supported
    os.rmdir = not_supported
    os.scandir = not_supported
    os.stat = not_supported
    os.statvfs = not_supported
    os.truncate = not_supported
    os.unlink = not_supported
    os.utime = not_supported
