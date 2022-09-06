import torch
import torch.nn as nn

class Flatten(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self,x):return x.reshape([x.shape[0],-1])

class GaussianMixture(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,x):return x