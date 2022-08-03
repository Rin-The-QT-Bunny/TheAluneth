from neuro_config import *
from neuro_vertex import *
from neuro_concept_structure import *
from neuro_types import *

c1 = ConceptDot("blue","color")
c2 = ConceptDot("red","color")
c3 = ConceptDot("green","color")

r1 = RelationDot("left","position")
r2 = RelationDot("right","position")

clist = [c1,c2,c3]
rlist = [r1,r2]
for c in clist:print(c)
for r in rlist:print(r)