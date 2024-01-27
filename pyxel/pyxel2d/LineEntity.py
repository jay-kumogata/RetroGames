import math
from Const import *
from Vec import *

# 線オブジェクト
class LineEntity:
    def __init__(self,x0, y0, x1, y1, restitution=0.9):
        self.shape = ShapeLine
        self.type = BodyStatic
        self.x = (x0 + x1) / 2
        self.y = (y0 + y1) / 2
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = 0

        self.restitution = restitution 
        self.vec = Vec(x1 - x0, y1 - y0)
        length = math.sqrt(self.vec.x ** 2 + self.vec.y ** 2)
        self.norm = Vec(y0 - y1, x1 - x0).mul(1 / length)

# End of LineEntity.py
