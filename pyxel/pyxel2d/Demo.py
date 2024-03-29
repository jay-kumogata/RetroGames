#
# Pyxelを使った物理エンジン デモ
# 「ゲームで学ぶJavaScript入門 増補改訂版」物理エンジンTiny2Dを参考にしました．
# cf. https://thinkit.co.jp/article/8467
#
# Jan 27, 2024 ver.1 (Pyxel/Pythonに移植しました)
# Mar 21, 2024 ver.2 (サイズを1/5に変更)
#

# -*- coding: utf-8 -*-
import random
import math
import pyxel
from Engine import *

colors = [8, 9, 10, 11, 12] # 色の配列

pyxel.init(110, 100, title="demo", fps=20)
engine = Engine(0, 0, 120, 120, 0, 9.8) # 物理エンジン作成
r = RectangleEntity(100, 10, 10, 80) # 矩形を作成しエンジンに追加
r.color = 2
engine.entities.append(r)
r = RectangleEntity(0, 10, 10, 80)
r.color = 2
engine.entities.append(r)
r = LineEntity(10, 60, 80, 70) # 線分を作成しエンジンに追加
r.color = 14
engine.entities.append(r)
r = LineEntity(100, 80, 20, 90) # 線分を作成しエンジンに追加
r.color = 14
engine.entities.append(r)

# 7 x 3 = 21 個の円（固定）を作成
for i in range(7):
    for j in range(3):
        r = CircleEntity(i * 12 + 20, j * 12 + 20, 1, BodyStatic)
        r.color = colors[j]
        engine.entities.append(r)

# 20 個の円（移動）を作成
for i in range(20):
    r = CircleEntity(random.randint(0,80) + 10,
                     random.randint(0,40),
                     2, BodyDynamic)
    r.color = colors[random.randint(0,4)];
    r.velocity.x = random.randint(0,2) - 1
    r.velocity.y = random.randint(0,2) - 1
    engine.entities.append(r)

engine.setGravity(0,0.04)

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

