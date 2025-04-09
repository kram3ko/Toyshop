from pathlib import PurePosixPath

from storages.backends.dropbox import DropboxStorage

# FIXING MISTAKE that standart way somehpow adding Local disc to path
class PatchedDropboxStorage(DropboxStorage):
    def _full_path(self, name):
        return (PurePosixPath(self.root_path) / name).as_posix()
