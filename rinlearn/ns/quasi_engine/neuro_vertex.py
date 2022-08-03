import torch
import torch.nn as nn

from aluneth.data_structure import *

class ImplementationNotFound(Exception):
    pass

class DiffVertex(nn.Module):
    def __init__(self):super().__init__()

    def prop(self,inputs,structure,context):return inputs

class VertexExecutor(nn.Module):
    def __init__(self,structure,imps):
        super().__init__()
        self.implementations = imps # actual implementations of operators
        self.concept_structure = structure # The basis of implementations
    
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

            if impl == None:return []
            return impl.prop(inputs,self.concept_structure,context)
        return retrieve(program,context)
            
