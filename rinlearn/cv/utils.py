import torch
import torchvision.transforms as tranforms

import numpy as np

from PIL import Image

def resize(img,resolution): return 

def data2images(torch_data): return torch_data.permute([0,2,3,1])

def images2data(images): return 

def load_image(path,normalize = True):
    if normalize: return torch.tensor(np.array(Image.open(path))).float()/256
    return torch.tensor(np.array(Image.open(path))).float()