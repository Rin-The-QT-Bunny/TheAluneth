from pyexpat import features
import torch
import torch.nn as nn

import numpy as np

from aluneth.utils import *

OBJECT_FEATURE_DIM = 256
CONCEPT_FEATURE_DIM = 256
RELATION_FEATURE_DIM = 512

class ObjectSet(nn.Module):
    def __init__(self,features,probs):
        super().__init__()
        assert probs.shape[0] == features.shape[0],"size of features and probs don't match"
        self.features = features
        self.probs = probs
    def object_set(self): return 0
    def pdf(self): return dnp(self.probs)
    
class SingleObject(nn.Module):
    def __init__(self,features,probs,cast=True):
        super().__init__()
        assert probs.shape[0] == features.shape[0],"size of features and probs don't match"
        self.features = features
        self.probs = probs
    def pdf(self): return dnp(self.probs)

def normalize(tensor): return tensor/torch.sum(tensor)

def cast_object_set(OSet):return SingleObject(OSet.features,normalize(OSet.probs))


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

def mix_measurements(measurements,probs,unitary = False):
    size_meas = 0;size_probs = -1
    if isinstance(probs,torch.Tensor):size_meas = measurements.shape[0] 
    else: size_meas = len(measurements)
    if isinstance(probs,torch.Tensor):size_probs = probs.shape[0] 
    else: size_probs = len(probs)

    assert size_meas  == size_probs,"measurements and mix probs doesn't match"
    probs = torch.tensor(probs)
    if(unitary): probs = probs/torch.sum(probs)

    basic_meas = measurements[0].probs * probs[0]
    for i in range(len(measurements)-1):
        meas = measurements[i+1]
        basic_meas = basic_meas + meas.probs * probs[i + 1]
    return ConceptMeasurement(measurements[0].keys,basic_meas)

keys = ["red","blue","green"]
probs1 = torch.sigmoid(torch.randn([3]))
probs1 = probs1/torch.sum(probs1)
cout1 = ConceptMeasurement(keys,probs1)


probs2 = torch.sigmoid(torch.randn([3]))
probs2 = probs2/torch.sum(probs2)
cout2 = ConceptMeasurement(keys,probs2)

probs3 = torch.sigmoid(torch.randn([3]))
probs3 = probs3/torch.sum(probs3)
cout3 = ConceptMeasurement(keys,probs3)

cmix = mix_measurements([cout1,cout2,cout3],[0.5,0.5,0.5],True)



print(cout1.pdf())
print(cout2.pdf())
print(cout3.pdf())
print(cmix.pdf())

Oset = ObjectSet(torch.randn([3,OBJECT_FEATURE_DIM]),torch.ones([3]))
SO = cast_object_set(Oset)
print(Oset.pdf())
print(SO.pdf())