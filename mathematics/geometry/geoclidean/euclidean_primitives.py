from Reflection.program import *
from Reflection.types import *
from Reflection.utils import *

tpoint = baseType("tpoint")
tline = baseType("tline")
tcircle = baseType("tcircle")

def make_point():return 0

def realize_point(x,y): return x,y

euc_realize_point = Primitive("euc_realize_point",arrow(treal,treal,tpoint),realize_point)