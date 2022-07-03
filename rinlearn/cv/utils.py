import torch
import torchvision.transforms as tranforms

import numpy as np

from PIL import Image

def resize(img,resolution): return 

def data2images(torch_data): return torch_data.permute([0,2,3,1])

def images2data(images): return torch.tensor(images).permute([0,3,1,2])

def load_image(path,normalize = True):
    if normalize: return torch.tensor(np.array(Image.open(path))).float()/256
    return torch.tensor(np.array(Image.open(path))).float().unsqueeze(0)

def combine_images(images):
    output = images2data(images[0:1])
    for i in range(len(images) - 1):
        output = torch.cat([output,images[i+1:i+2]],0)
    return output