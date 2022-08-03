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

clist = [c1,c2,c3]
rlist = [r1,r2]

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
        return context["Object"]

class CMeasureColor(DiffVertex):
    def __init__(self):
        super().__init__()
        self.name = "measure_color"

    def prop(self,inputs,structure,context):
        assert isinstance(context,dict),print("context is not a valid diction.")

        return structure.MeasureConcept("color",inputs[0])

cimps = [CScene(),CMeasureColor()]

# write the executor to execute the program in the context
context = {"Objects":ObjectSet(torch.randn([1,OBJECT_FEATURE_DIM]),0.999 * torch.ones([1,1]))}
NORD = VertexExecutor(cstructure,cimps)

program = toFuncNode("measure_color(scene())")


print(cstructure.MeasureConcept("color",ObjectSet(torch.randn([1,OBJECT_FEATURE_DIM]),0.999 * torch.ones([1,1]))).sample_result())

outputs = NORD.execute(program,context)
print(outputs)