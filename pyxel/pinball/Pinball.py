#
# Pyxelを使ったPinballゲーム
# Isidor氏作の「PINBALL PONG」を参考にしました．
# https://www.lexaloffle.com/bbs/?tid=28488
#
# Apr 30, 2023 ver.1 (changed graphics library to pyxel)
# Oct 23, 2023 ver.2 (added flippers and renamed to Pinball)
# Nov 17, 2023 ver.3 (fixed gravitational acceleration and added flipper speed)
#
# -*- coding: utf-8 -*-
import time
import pyxel
from random import *

class Pinball:
    def __init__( self ):
        # Pyxel初期化
        pyxel.init( 128, 128, title="Pinball", fps=30)
        pyxel.load("Pinball.pyxres")
        self.init()
        pyxel.run(self.update,self.draw)
        
    def update( self ):
        """NONE"""

    def draw( self ):
        if ( self.fi == 0 ):
            pyxel.cls(1)
            self.table()
            self.flipper()
            self.move()
        elif ( self.fi == 1 ):
            self.final()

    # ゲーム初期化        
    def init( self ):
        self.score = 0
        self.ball = 1
        self.color = 0
        self.x = 98
        self.y = 120
        self.vx = 0
        self.vy = -1
        self.launch = 0
        self.fi = 0
        self.bump = 0.3
        self.left = 0         # 左フリッパー状態(0,1,2)
        self.right = 0        # 右フリッパー状態(0,1,2)
        self.vl = 0           # 左フリッパー速度(0,1)
        self.vr = 0           # 右フリッパー速度(0,1)

    # PICO-8スプライト互換
    def spr( self, no, x, y ):
        pyxel.blt( x,y,0,no*8,0,8,8,0 )

    #　台
    def table( self ):
        self.spr(1,58,48)
        self.spr(1,42,58)
        self.spr(1,74,58)
        self.spr(1,58,68)

        self.spr(3,22,9)
        self.spr(4,98,9)

        self.spr(5,28,87)
        self.spr(6,28,95)
        self.spr(7,85,87)
        self.spr(8,85,95)

        self.spr(9,30,25)
        self.spr(10,47,25)
        self.spr(10,67,25)
        self.spr(9,84,25)
        self.spr(11,27,54)
        self.spr(11,27,62)
        self.spr(11,27,70)
        self.spr(11,86,54)
        self.spr(11,86,62)
        self.spr(11,86,70)

        self.spr(15,41,108) 
        self.spr(16,72,108) 
        
        pyxel.line(22,0,105,0,7)
        pyxel.line(22,8,105,8,7)
        pyxel.line(22,127,105,127,7)
        pyxel.line(22,0,22,127,7)
        pyxel.line(105,0,105,127,7)
        pyxel.line(98,23,98,127,7)
        if (self.launch == 1):
            pyxel.line(98,9,98,22,7)
        pyxel.rect(0,0,22,128,9)
        pyxel.rect(106,0,127,128,9)

    # フリッパー
    def flipper( self ):
        self.vl = self.vr = 0
        if ( pyxel.btn(pyxel.KEY_LEFT) ):
            if (self.left < 2): self.left += 1; self.vl = 1
        else:
            if (self.left > 0): self.left -= 1; self.vl = -1

        if ( pyxel.btn(pyxel.KEY_RIGHT) ):
            if (self.right < 2): self.right += 1; self.vr = 1
        else:
            if (self.right > 0): self.right -= 1; self.vr = -1
        
        # 表示        
        if (self.left == 0 ): self.spr( 12, 48, 114); self.spr( 12, 34, 102)
        if (self.left == 1 ): self.spr( 13, 48, 113); self.spr( 13, 34, 101) 
        if (self.left == 2 ): self.spr( 14, 48, 112); self.spr( 14, 34, 100)
        if (self.right == 0 ): self.spr( 14, 65, 114); self.spr( 14, 79, 102)
        if (self.right == 1 ): self.spr( 13, 65, 113); self.spr( 13, 79, 101)
        if (self.right == 2 ): self.spr( 12, 65, 112); self.spr( 12, 79, 100)
        
    # ボール移動
    def move( self ):
        pyxel.text(25,2,"SCORE",7)
        pyxel.text(47,2,f"{self.score:d}",7)
        pyxel.text(82,2,"BALL",7)
        pyxel.text(100,2,f"{3-self.ball:d}",7)

        # デバッグ用 
        #s = (f"vx={self.vx:.2f} vy={self.vy:.2f}\n")
        #pyxel.text(25,2,s,7)
        
        if (self.x < 92 and self.launch == 0):
            self.launch = 1
        if (self.y > 120 ):
            self.x = 98
            self.y = 120
            self.vx = 0
            self.vy = -1
            self.launch = 0
            if (self.ball < 4 ):
                self.ball = self.ball + 1

        # 重力加速度
        self.vy += 0.005

        # 移動と衝突
        for n in range(3):
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.collision()

        # 残ボールチェック
        if (self.ball > 3):
            self.fi = 1
        else:
            self.spr( 0, self.x,self.y )
            
    # ボール衝突
    def collision( self ):

        # Ball周辺の色を取得
        # [0][1][2] [3]
        # [4][ ][ ] [5]
        # [6][ ][ ] [7]
        # [8][9][10][11]
        pos = [ [2,2],[3,2],[4,2],[5,2],
                [2,3],[5,3],[2,4],[5,4],
                [2,5],[3,5],[4,5],[5,5]]
        col = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
        for n in range(12):
            col[n]=pyxel.pget(self.x+pos[n][0],self.y+pos[n][1])
        
        if (col[4] != 1 and col[1] != 1):
            # 左上壁衝突(45°)
            self.vx,self.vy = self.bump+random()/5,self.bump+random()/5
            self.color = col[4]
        elif (col[9] != 1 and col[6] != 1):
            # 左下壁衝突(135°)
            self.vx,self.vy = self.bump+random()/5,-self.bump-random()/5
            self.color = col[9]
        elif (col[7] != 1 and col[10] != 1):
            # 右下壁衝突(225°)
            self.vx,self.vy = -self.bump-random()/5,-self.bump-random()/5
            self.color = col[7]
        elif (col[5] != 1 and col[2] != 1):
            # 右上壁衝突(315°)
            self.vx,self.vy = -self.bump-random()/5,self.bump+random()/5
            self.color = col[5]
            
        elif (col[1] != 1 and col[2] != 1):
            # 上壁衝突(0°)
            self.vy = -self.vy
            self.color = col[1]
        elif (col[6] != 1 and col[4] != 1):
            # 左壁衝突(90°)
            self.vx = -self.vx
            self.color = col[6]
        elif (col[9] != 1 and col[10] != 1):
            # 下壁衝突(180°)
            self.vy = -self.vy
            self.color = col[9]
        elif (col[7] != 1 and col[5] != 1):
            # 右壁衝突(270°)
            self.vx = -self.vx
            self.color = col[7]

        # 壁通過防止
        if (self.vx < -1.0): self.vx = -1.0 
        if (self.vx > 1.0): self.vx = 1.0
        if (self.vy < -1.0): self.vy = -1.0
        if (self.vy > 1.0): self.vy = 1.0

        # 加点
        if (self.color == 8 or self.color == 14 or self.color == 15 ):
            # バンパー(10点)
            self.score += 10
        elif (self.color == 5 or self.color == 12):
            # フリッパー(20点)
            self.score += 20
            if (self.x < 64 and self.vl == 1): self.vy = -0.7
            if (self.x < 64 and self.vl == -1): self.vy = -0.1
            if (self.x > 64 and self.vr == 1): self.vy = -0.7
            if (self.x > 64 and self.vr == -1): self.vy = -0.1
        elif (self.color == 2 or self.color == 6):
            # 左右バー(5点)
            self.score += 5
            
        # 色情報クリア
        self.color = 0

    # ゲーム初期化        
    def final(self):
        # GAME OVER
        pyxel.text(44,85,"GAME OVER", 7)

        # 再ゲーム
        if pyxel.btn(pyxel.KEY_SPACE):
            self.init()
        
# Main
Pinball()

# End of Pinball.py
