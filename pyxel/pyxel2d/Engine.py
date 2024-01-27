from Const import *
from Vec import *
from RectangleEntity import *
from LineEntity import *
from CircleEntity import *

# 物理エンジン
class Engine:
    def __init__(self, x=0, y=0, width=1000, height=1000, gravityX=0, gravityY=0):
        self.worldX = x 
        self.worldY = y 
        self.worldW = width 
        self.worldH = height
        self.gravity = Vec(gravityX, gravityY)
        self.entities = []

    def setGravity(self,x, y):
        self.gravity.x = x
        self.gravity.y = y

    def step(self,elapsed):
        gravity = self.gravity.mul(elapsed, elapsed)
        entities = self.entities

        # entityを移動
        for e in entities:
            if (e.type == BodyDynamic):
                accel = e.accel.mul(elapsed, elapsed)
                e.velocity = e.velocity.add(gravity)
                e.velocity = e.velocity.add(accel)
                e.velocity = e.velocity.mul(e.deceleration)
                e.move(e.velocity.x, e.velocity.y)

        # 範囲外のオブジェクトを削除
        self.entities = list(filter(lambda e:
                                    self.worldX <= e.x and 
                                    e.x <= self.worldX + self.worldW and 
                                    self.worldY <= e.y and 
                                    e.y <= self.worldY + self.worldH,
                                    entities))

        # 衝突判定 & 衝突処理
        for i in range(len(entities)):
            for j in range(i+1, len(entities)):
                e0 = entities[i]
                e1 = entities[j]
                if (e0.type == BodyStatic and e1.type == BodyStatic):
                    continue

                if (e0.shape == ShapeCircle and e1.shape == ShapeCircle):
                    e0.collidedWithCircle(e1)
                elif (e0.shape == ShapeCircle and e1.shape == ShapeLine):
                    e0.collidedWithLine(e1)
                elif (e0.shape == ShapeLine and e1.shape == ShapeCircle):
                    e1.collidedWithLine(e0)
                elif (e0.shape == ShapeCircle and e1.shape == ShapeRectangle):
                    e0.collidedWithRect(e1)
                elif (e0.shape == ShapeRectangle and e1.shape == ShapeCircle):
                    e1.collidedWithRect(e0)

# End of Engine.py
