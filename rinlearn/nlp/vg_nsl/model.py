import torch
import torch.nn as nn

from aluneth.rinlearn.cv.utils import combine_tensors
from aluneth.rinlearn.nn.functional_net import FCBlock

class VG_NSL(nn.Module):
    def __init__(self,word_dim = 128):
        super().__init__()
        self.consittuent_matcher = FCBlock(128,3,word_dim + word_dim,1)
    
    def forward(self,x):
        """input x should be a series of vectors"""
        if isinstance(x,list):
            x = combine_tensors(x)
        return x