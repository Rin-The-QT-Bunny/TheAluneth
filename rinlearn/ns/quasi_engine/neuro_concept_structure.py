import torch
import torch.nn as nn

# A concept structure is convieved as the way how concepts/relations interacts with object/objects
# and produce the probabilitic outcomes. Basically a concept structure is a set of functions that 
# contains the way to calculate the following things:
# Pr[c|e] which means the outcome prob of e entails c 
# Pr[r|e1,e2] which means the prob of (e1,e1) entails r


# Basic concept types of for the concept structure

class ConceptDot(nn.Module):
    def __init__(self,dim):
        super().__init__()
        self.feature = torch.randn([1,dim])

class RelationDot(nn.Module):
    def __init__(self,feature):
        super().__init__()
        self.feature = self.feature

# This part contains the basic concept type and corresponding structures.

class NeuroConceptStructure(nn.Module):
    def __init__(self,concepts,concept_relations):
        self.concepts = concepts
        self.concept_relations = concept_relations

    def PrConceptMeasure(value,entity): return 0

    def PrRelationMeasure(relation,entity1,entity2): return 0

