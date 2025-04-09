from pathlib import PurePosixPath, PurePath

from storages.backends.dropbox import DropboxStorage

# FIXING MISTAKE that standart way somehpow adding Local disc to path
class PatchedDropboxStorage(DropboxStorage):
    def _full_path(self, name):
        fixed_name = PurePath(name).as_posix()
        full_path = (PurePosixPath(self.root_path) / fixed_name).as_posix()
        return full_path
