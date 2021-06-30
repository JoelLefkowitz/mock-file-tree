import os
from typing import NoReturn, Any

def not_supported(*args: Any, **kwargs: Any) -> NoReturn:
    raise NotImplementedError()

def block_unsupported() -> None:
    for _ in [
        open,
        os.access,
        os.chdir,
        os.chflags,
        os.chmod,
        os.chown,
        os.chroot,
        os.lchflags,
        os.lchmod,
        os.lchown,
        os.lstat,
        os.mkdir,
        os.mkfifo,
        os.mknod,
        os.open,
        os.path.getatime,
        os.path.getctime,
        os.path.getmtime,
        os.path.getsize,
        os.path.islink,
        os.path.ismount,
        os.path.lexists,
        os.pathconf,
        os.readlink,
        os.remove,
        os.rmdir,
        os.scandir,
        os.stat,
        os.statvfs,
        os.truncate,
        os.unlink,
        os.utime,
    ]:
        _ = not_supported
