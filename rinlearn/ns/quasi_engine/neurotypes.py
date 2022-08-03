import torch
import torch.nn as nn

import numpy as np

from aluneth.utils import *

CONCEPT_DIM = 256
RELATION_DIM = 512

class ConceptMeasurement(nn.Module):
    def __init__(self,keys,probs,cast = True):
        super().__init__()
        assert probs.shape[0] == len(keys),"size of keys and probs don't match"
        self.keys = keys
        self.probs = probs
        if cast: self.probs = self.probs/torch.sum(self.probs)
    
    def pdf(self,flag=False): 
        if flag:return np.concatenate([self.keys,dnp(self.probs)],0)
        else: return dnp(self.probs)
    
    def most_likely_result(self):return self.keys[np.argmax(dnp(self.probs))]

    def sample_result(self):return np.random.choice(self.keys,p=dnp(self.probs))

def mix_measurements(measurements,probs):
    assert measurements.shape[0] == probs.shape[0],"measurements and mix probs doesn't match"
    basic_meas = measurements[0].probs * probs[0]
    for i in range(len(measurements)-1):
        meas = measurements[i+1]
        basic_meas = basic_meas + meas.probs * probs[i + 1]
    return basic_meas
keys = ["red","blue","green"]
probs = torch.sigmoid(torch.randn([3]))
probs = probs/torch.sum(probs)
cout = ConceptMeasurement(keys,probs)

print(cout.pdf())
print(cout.most_likely_result())
print(cout.sample_result())