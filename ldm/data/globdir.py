from torch.utils.data import Dataset
import glob

from ldm.data.base import ImagePaths


class GlobDirBase(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = None
        self.keys = None

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        example = self.data[i]
        ex = {}
        if self.keys is not None:
            for k in self.keys:
                ex[k] = example[k]
        else:
            ex = example
        return ex


class GlobDirTrain(GlobDirBase):
    def __init__(self, dir, size, keys=None):
        super().__init__()
        paths = glob.glob(dir)
        self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        self.keys = keys


class GlobDirValidation(GlobDirBase):
    def __init__(self, dir, size, keys=None):
        super().__init__()
        paths = glob.glob(dir)
        self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        self.keys = keys
