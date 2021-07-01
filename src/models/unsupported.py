# pylint: disable=invalid-name
# pylint: disable=unused-variable
from typing import Any, NoReturn


def unsupported(*args: Any, **kwargs: Any) -> NoReturn:
    raise NotImplementedError()


# We can't do this as a loop as we're redefining the variables.
def block_unsupported(os: Any) -> None:
    os.access = unsupported
    os.chdir = unsupported
    os.chflags = unsupported
    os.chmod = unsupported
    os.chown = unsupported
    os.chroot = unsupported
    os.lchflags = unsupported
    os.lchmod = unsupported
    os.lchown = unsupported
    os.lstat = unsupported
    os.mkdir = unsupported
    os.mkfifo = unsupported
    os.mknod = unsupported
    os.open = unsupported
    os.path.getatime = unsupported
    os.path.getctime = unsupported
    os.path.getmtime = unsupported
    os.path.getsize = unsupported
    os.path.islink = unsupported
    os.path.ismount = unsupported
    os.path.lexists = unsupported
    os.pathconf = unsupported
    os.readlink = unsupported
    os.remove = unsupported
    os.rmdir = unsupported
    os.scandir = unsupported
    os.stat = unsupported
    os.statvfs = unsupported
    os.truncate = unsupported
    os.unlink = unsupported
    os.utime = unsupported
