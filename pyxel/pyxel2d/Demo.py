#
# Pyxelを使った物理エンジン デモ
# 「ゲームで学ぶJavaScript入門 増補改訂版」物理エンジンTiny2Dを参考にしました．
# cf. https://thinkit.co.jp/article/8467
#
# Jan 27, 2024 ver.1 (Pyxel/Pythonに移植しました)
#

# -*- coding: utf-8 -*-
import random
import math
import pyxel
from Engine import *

colors = [8, 9, 10, 11, 12] # 色の配列

pyxel.init(550, 500, title="Demo", fps=20)
engine = Engine(0, 0, 600, 600, 0, 9.8) # 物理エンジン作成
r = RectangleEntity(500, 50, 50, 400) # 矩形を作成しエンジンに追加
r.color = 2
engine.entities.append(r)
r = RectangleEntity(0, 50, 50, 400)
r.color = 2
engine.entities.append(r)
r = LineEntity(50, 300, 400, 350) # 線分を作成しエンジンに追加
r.color = 14
engine.entities.append(r)
r = LineEntity(500, 400, 100, 450) # 線分を作成しエンジンに追加
r.color = 14
engine.entities.append(r)

# 7 x 3 = 21 個の円（固定）を作成
for i in range(7):
    for j in range(3):
        r = CircleEntity(i * 60 + 100, j * 60 + 100, 5, BodyStatic)
        r.color = colors[j]
        engine.entities.append(r)

# 20 個の円（移動）を作成
for i in range(20):
    r = CircleEntity(random.randint(0,400) + 50,
                     random.randint(0,200),
                     10, BodyDynamic)
    r.color = colors[random.randint(0,4)];
    r.velocity.x = random.randint(0,10) - 5
    r.velocity.y = random.randint(0,10) - 5
    engine.entities.append(r)

engine.setGravity(0,0.2)

def update():
    global engine
    engine.step(1)

def draw():
    global engine
    pyxel.cls(1)
    for e in engine.entities:
        if (e.shape == ShapeCircle):
            pyxel.circ(e.x,e.y,e.radius,e.color)
        elif (e.shape == ShapeLine):
            pyxel.line(e.x0,e.y0,e.x1,e.y1,e.color)
        elif (e.shape == ShapeRectangle):
            pyxel.rect(e.x,e.y,e.w,e.h,e.color)

# メイン            
pyxel.run(update, draw)

# End of Demo.py

