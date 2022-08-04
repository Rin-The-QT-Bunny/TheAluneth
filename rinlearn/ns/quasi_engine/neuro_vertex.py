import torch
import torch.nn as nn

from aluneth.data_structure import *

from neuro_types import *

class ImplementationNotFound(Exception):
    pass

class UnknownSupervisionType(Exception):
    pass

class DiffVertex(nn.Module):
    def __init__(self):super().__init__()

    def prop(self,inputs,structure,context):return inputs

class VertexExecutor(nn.Module):
    def __init__(self,structure,imps):
        super().__init__()
        self.implementations = imps # actual implementations of operators
        self.concept_structure = structure # The basis of implementations

    def supervise_prob(self,input,target):
        if isinstance(input,Rint): # prior distribution on real interger
            return torch.sigmoid((0.5 - torch.abs(target - input.value))/0.125)
        if isinstance(input,ConceptMeasurement): # prob of a pure state measurement on the input
            return input.probs[input.keys.index(target)]
        raise UnknownSupervisionType()
        return 
        
    def execute(self,program,context):
        if isinstance(program,FuncNode):pass
        else: program = toFuncNode(program)

        def retrieve(p,context):
            impl = None
            curr_name = p.token
            for implement in self.implementations:
                if implement.name == curr_name:
                    impl = implement
            inputs = []
            # look for arguments
            if p.has_args():
                for arg in p.children:
                    inputs.append(retrieve(arg,context))
            # locate the implementation by the token name

            if impl == None:return p.token
            return impl.prop(inputs,self.concept_structure,context)
        return retrieve(program,context)
            
