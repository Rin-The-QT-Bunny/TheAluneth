import torch
import torch.nn as nn

from neuro_types import *
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
    def __init__(self,concepts,relations):
        super().__init__()
        if not isinstance(concepts,nn.ModuleList):
            self.concepts = nn.ModuleList(concepts)
        else:self.concepts = concepts

        if not isinstance(relations,nn.ModuleList):
            self.relations = nn.ModuleList(relations)
        else:self.relations = relations
    
    def add_concept(self,concept): self.concepts.append(concept)

    def MeasureConcept(self,concept,entity): 
        measures = []

        for i in range(entity.features.shape[0]):
            e = entity.features[i]
            scores = []
            concept_values = []
            for c in self.concepts:
                if c.type == concept:
                    concept_values.append(c.name)
                    scores.append(torch.sigmoid( (torch.cosine_similarity(c.feature,e)-0.2) / 0.15))
            scores = normalize(torch.cat(scores,0))
 
            meas = ConceptMeasurement(concept_values,scores)
            measures.append(meas)

        return mix_measurements(measures,entity.probs)

            
    def PrConceptMeasure(self,value,entity): return 0

    def MeasureRelation(self,relation,entity1,entity2): return 0

    def PrRelationMeasure(self,relation,entity1,entity2): return 0

