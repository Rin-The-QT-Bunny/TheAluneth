import torch
import torch.nn as nn

class GRUEncoder(nn.Module):
    def __init__(self,words_dim,semantics_dim,bilayer = True):
        super().__init__()
        self.GRU = nn.GRUCell
