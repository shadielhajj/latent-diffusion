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


class GlobDir(GlobDirBase):
    def __init__(self, dir, size, start_index=0, end_index=-1, keys=None):
        super().__init__()
        paths = sorted(glob.glob(dir))[start_index:end_index]
        self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        self.keys = keys

