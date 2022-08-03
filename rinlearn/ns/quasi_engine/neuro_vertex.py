import torch
import torch.nn as nn

from aluneth.data_structure import *

class ImplementationNotFound(Exception):
    pass

class DiffVertex(nn.Module):
    def __init__(self):super().__init__()

    def prop(self,inputs,structure,context):return inputs

class VertexExecutor(nn.Module):
    def __init__(self):
        super().__init__()
        self.implementations = None # actual implementations of operators
        self.concept_structure = None # The basis of implementations
    
    def execute(self,program,context):
        if isinstance(program,DiffVertex):pass
        else: program = toFuncNode(program)
        def retrieve(p,context):
            inputs = []
            # look for arguments
            if p.has_arg():
                for arg in p.children:
                    inputs.append(retrieve(arg,context))
            # locate the implementation by the token name
            for implement in self.implementations:
                if implement.name == arg.token:
                    return implement.prop(inputs,self.concept_structure,context)
            raise ImplementationNotFound()
        return retrieve(program,context)
            
