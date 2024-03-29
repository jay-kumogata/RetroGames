#
# Pyxelを使った物理エンジン パチンコゲーム
# 「ゲームで学ぶJavaScript入門 増補改訂版」物理エンジンTiny2Dを参考にしました．
# cf. https://thinkit.co.jp/article/8467
#
# Mar 29, 2024 ver.1 (Pyxel/Pythonに移植しました)
#
# -*- coding: utf-8 -*-
import random
import math
import pyxel
import PyxelUniversalFont as puf
from Engine import *

class Pachinko:

    walls = [
        [-20, -20, 20, 160],
        [-20, -20, 160, 20],
        [100, -20, 20, 160],
    ]

    corners = [
        [30, -10, 6, 6],
        [6, 6, -10, 30],
        [70, -10, 94, 6],
        [94, 6, 110, 30],
    ]

    lines = [
        [90, 40, 90, 160]
    ]

    def __init__( self ):

        # 初期化
        self.offset = 0
        self.score = 0
        self.bc = 6 # パチンコ玉の色
        
        # エンジン初期化 
        self.engine = Engine(-20, -20, 140, 160, 0, 1.96)

        # 壁
        for w in self.walls:
            r = RectangleEntity(w[0], w[1], w[2], w[3])
            r.color = 14
            self.engine.entities.append(r)

        # 角
        for w in self.corners:
            r = LineEntity(w[0], w[1], w[2], w[3], 0.8)
            r.color = 1
            self.engine.entities.append(r)

        # 線
        for w in self.lines:
            r = LineEntity(w[0], w[1], w[2], w[3], 0.8)
            r.color = 2
            self.engine.entities.append(r)

        # 釘
        for i in range(9):
            for j in range( 8 + i % 2 ):
                x = (j * 10 + 10) - 5 * (i % 2)
                r = CircleEntity(x, i * 10 + 20, 1, BodyStatic, 1)
                r.color = i+6
                self.engine.entities.append(r)

        # キャッチャー
        self.catcher = RectangleEntity(0, 110, 30, 5)
        self.catcher.color = 2
        self.catcher_sign = 1
        self.engine.entities.append(self.catcher)

        # Pyxel初期化
        pyxel.init( 100, 120, title="Pachinko", fps=30)
        pyxel.run(self.update, self.draw)

    def callback(self, me, peer ):
        if (peer == self.catcher):
            self.engine.entities = [e for e in self.engine.entities if e != me]
            self.score += 10
            
    def update( self ):
        if pyxel.btn(pyxel.KEY_SPACE):
            self.offset = min(self.offset + 1, 40)
        elif self.offset > 0:
            r = CircleEntity(95, 80, 2, BodyDynamic);
            r.color = self.bc
            r.velocity.y = -self.offset / 10
            r.onhit = self.callback
            self.offset = 0
            self.bc = random.randint(6,14)
            self.engine.entities.append(r);
            
        if self.catcher.x > 60 or self.catcher.x < 0:
            self.catcher_sign *= -1
        self.catcher.x = self.catcher.x + 1 * self.catcher_sign
       
        self.engine.step(0.01) # 物理エンジンの時刻を進める

    def draw( self ):
        pyxel.cls(1)
        for e in self.engine.entities:
            if (e.shape == ShapeCircle):
                pyxel.circ(e.x,e.y,e.radius,e.color)
            elif (e.shape == ShapeLine):
                pyxel.line(e.x0,e.y0,e.x1,e.y1,e.color)
            elif (e.shape == ShapeRectangle):
                pyxel.rect(e.x,e.y,e.w,e.h,e.color)

        # スコア表示
        pyxel.text(24, 2,"Score: ", 6)
        pyxel.text(64, 2,f"{self.score:d}", 6)

        # シューター表示
        pyxel.circ(95, 78 + self.offset, 2, self.bc)
        pyxel.rect(92, 81 + self.offset, 7, 40, 2)
        pyxel.text(self.catcher.x+12, self.catcher.y, "10", 6)

        # 壁表示
        pyxel.tri(-10, -10, 6-2, 6-2, -10, 30-2, 2)
        pyxel.tri(-10, -10, 6-2, 6-2, 30-2, -10, 2)
        pyxel.tri(110, -10, 94+2, 6-2, 70+2, -10, 2)
        pyxel.tri(110, -10, 94+2, 6-2, 110, 30-2, 2)
        
# Main
Pachinko()

# End of Pachinko.py
