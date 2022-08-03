import torch
import torch.nn as nn

import numpy as np

from aluneth.utils import *

class ConceptMeasurement(nn.Module):
    def __init__(self,keys,probs):
        super().__init__()
        assert probs.shape[0] == len(keys),"size of keys and probs don't match"
        self.keys = keys
        self.probs = probs / torch.sum(probs)
    
    def pdf(self,flag=False): 
        if flag:return np.concatenate([self.keys,dnp(self.probs)],0)
        else: return dnp(self.probs)
    
    def most_likely_result(self):return self.keys[np.argmax(dnp(self.probs))]

    def sample_result(self):return np.random.choice(self.keys,p=dnp(self.probs))


keys = ["red","blue","green"]
probs = torch.sigmoid(torch.randn([3]))
probs = probs/torch.sum(probs)
cout = ConceptMeasurement(keys,probs)

print(cout.pdf())
print(cout.most_likely_result())
print(cout.sample_result())