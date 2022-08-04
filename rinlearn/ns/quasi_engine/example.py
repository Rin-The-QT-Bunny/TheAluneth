from neuro_config import *
from neuro_vertex import *
from neuro_concept_structure import *
from neuro_types import *

# start the session of declareing concepts and relations
c1 = ConceptDot("blue","color")
c2 = ConceptDot("red","color")
c3 = ConceptDot("green","color")
# color concept of red blue green

r1 = RelationDot("left","position")
r2 = RelationDot("right","position")
# positional relation of left and right

clist = nn.ModuleList([c1,c2,c3])
rlist = nn.ModuleList([r1,r2])

for c in clist:print(c)
for r in rlist:print(r)
# display all the relations and concepts

# create the concept structure that calculate the concepts
cstructure = NeuroConceptStructure(clist,rlist)

# write some basic implementations of these functions

class CScene(DiffVertex):
    def __init__(self):
        super().__init__()
        self.name = "scene"

    def prop(self,inputs,structure,context):
        assert isinstance(context,dict),print("context is not a valid diction.")
        return context["Objects"]

class CMeasureColor(DiffVertex):
    def __init__(self):
        super().__init__()
        self.name = "measure_color"

    def prop(self,inputs,structure,context):
        assert isinstance(context,dict),print("context is not a valid diction.")

        return structure.MeasureConcept("color",inputs[0])

class CFilterColor(DiffVertex):
    def __init__(self):
        super().__init__()
        self.name = "filter_color"
    
    def prop(self,inputs,structure,context):
        input_color = 'blue'
        input_set = inputs[1]
        filter_scores = []
        for i in range(input_set.features.shape[0]):
            prior_prob = input_set.probs[i]
            filter_prob = structure.PrConceptMeasure(input_color,input_set.features[i])
            filter_scores.append(torch.min(prior_prob,filter_prob).reshape([1,-1]))

        return ObjectSet(input_set.features,torch.cat(filter_scores))

class CUnique(DiffVertex):
    def __init__(self):
        super().__init__()
        self.name = "unique"

    def prop(self,inputs,structure,context):
        features = inputs[0].features
        scores = inputs[0].probs
        return SingleObject(features,scores/torch.sum(scores))

class CCount(DiffVertex):
    def __init__(self):
        super().__init__()
        self.name = "count"
    
    def prop(self,inputs,structure,context):
        return Rint(torch.sum(inputs[0].probs))

cimps = [CScene(),CMeasureColor(),CUnique(),CFilterColor(),CCount()]

# write the executor to execute the program in the context
context = {"Objects":ObjectSet(torch.randn([2,OBJECT_FEATURE_DIM]),0.999 * torch.ones([2]))}
NORD = VertexExecutor(cstructure,cimps)

program = toFuncNode("measure_color(unique(scene()))")
#program = toFuncNode("measure_color(scene())")

program = toFuncNode("count(filter_color('red',scene()))")

outputs = NORD.execute(program,context)
print(outputs.pdf(True))

program = toFuncNode("measure_color(unique(scene()))")
outputs = NORD.execute(program,context)
print(outputs.pdf(True))

programc = toFuncNode("count(filter_color('red',scene()))")

optim = torch.optim.Adam(clist.parameters(),lr = 2e-2)
for epoch in range(100):
    optim.zero_grad()
    outputs = NORD.execute(program,context)
    loss = 0 - NORD.supervise_prob(outputs,"red")
    loss.backward()
    optim.step()
    print("Working Loss: ",dnp(loss))

print(outputs.pdf(True))