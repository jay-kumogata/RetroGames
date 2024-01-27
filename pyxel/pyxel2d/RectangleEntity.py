from Const import *
from Vec import *

# 矩形オブジェクト
class RectangleEntity:
    def __init__(self, x, y, width, height):
        self.shape = ShapeRectangle
        self.type = BodyStatic
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.deceleration = 1.0
        self.color = 0

    def isHit(self, i, j):
        return (self.x <= i and i <= self.x + self.w and
            self.y <= j and j <= self.y + self.h)

# End of RectangleEntity.py
