import os
import numpy as np
from torch.utils.data import Dataset
import glob

from ldm.data.base import ImagePaths


class FacesBase(Dataset):
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


class CelebAHQTrain(FacesBase):
    def __init__(self, size, keys=None):
        super().__init__()
        paths = glob.glob("data/celeba_hq_256/*")
        self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        self.keys = keys


class CelebAHQValidation(FacesBase):
    def __init__(self, size, keys=None):
        super().__init__()
        paths = glob.glob("data/celeba_hq_256/*")
        self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        self.keys = keys