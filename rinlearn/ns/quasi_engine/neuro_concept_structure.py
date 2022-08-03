import torch
import torch.nn as nn

# A concept structure is convieved as the way how concepts/relations interacts with object/objects
# and produce the probabilitic outcomes. Basically a concept structure is a set of functions that 
# contains the way to calculate the following things:
# Pr[c|e] which means the outcome prob of e entails c 
# Pr[r|e1,e2] which means the prob of (e1,e1) entails r


# Basic concept types of for the concept structure

class ConceptDot(nn.Module):
    def __init__(self,name,type,dim = 256):
        super().__init__()
        self.name = name
        self.type = type
        self.feature = torch.randn([1,dim])

    def __str__(self):return "concept:{}".format(self.name)

class RelationDot(nn.Module):
    def __init__(self,name,type,dim = 266):
        super().__init__()
        self.name = name
        self.type = type
        self.feature = torch.randn([1,dim])

    def __str__(self):return "relation:{}".format(self.name)
# This part contains the basic concept type and corresponding structures.

class NeuroConceptStructure(nn.Module):
    def __init__(self,concepts):
        self.concepts = nn.ModuleList(concepts)
    
    def add_concept(self,concept): self.concepts.append(concept)

    def MeasureConcept(concept,entity): return 0

    def PrConceptMeasure(value,entity): return 0

    def MeasureRelation(relation,entity1,entity2): return 0

    def PrRelationMeasure(relation,entity1,entity2): return 0

