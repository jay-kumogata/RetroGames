#
# Haskellで実装されたAsteroidsをPyxelに移植
# Asteroids in Haskell
# https://github.com/jay-kumogata/RetroGames/tree/main/haskell/asteroids
#
# Sep 02, 2024 ver.1 (changed graphics library to pyxel)
#
# -*- coding: utf-8 -*-

import pyxel
from Rock import *
from Ship import *
from Bullet import *
from Vec import *

class Asteroids():
    def __init__(self):

        # 0:開始 1:遊戯中 2:終了
        self.st = 0

    # いずれかの弾座標b.pが，岩rに衝突したか否かを返却．
    def collidesWithBullet(self, r : Rock):
        for b in self.bullets:
            if r.collidesWith(b.p):
                b.l = False
                return True
        return False

    # メインループ
    def update(self):

        # 開始
        if self.st == 0:


            # 初期化されたゲーム世界を返却する関数initialWorldを定義．
            self.rocks = [ Rock(Vec(60,60),   18, Vec(1,3)),
                           Rock(Vec(-18,80),  18, Vec(3,-1)),
                           Rock(Vec(18,9),    10, Vec(-1,3)),
                           Rock(Vec(-84,-6),  12, Vec(-1,-3)),
                           Rock(Vec(-18,-84),10, Vec(3,1)),
                          ]
            self.ship = Ship(Vec(0,0), Vec(0,0))
            self.bullets = []
            self.score = 0
            
            # 遊戯中へ遷移
            self.st = 1
    
        # 遊戯中    
        elif self.st == 1:
        
            # 岩衝突
            for r in self.rocks:
                # 岩と自機が衝突
                if r.collidesWith(self.ship.p):
                    self.st = 2
                    break
                
                # 岩に弾が当たって，岩のサイズが7より小さい場合には消滅．
                if self.collidesWithBullet(r) and r.s <= 6:
                    r.l = False
                    self.score += 500
                    
                # 岩に弾が当たって，岩のサイズが7より大きい場合には分裂．
                elif self.collidesWithBullet(r) and r.s > 6:
                    # サイズを半減，速度を60度左回転させた岩生成
                    self.rocks.append(Rock(r.p, r.s/2, r.v.rotateV(math.pi/3).mul(1.2)))
                    # サイズを半減，速度を60度右回転させた岩生成
                    self.rocks.append(Rock(r.p, r.s/2, r.v.rotateV(-math.pi/3).mul(1.2)))
                    # 元々の岩消滅
                    r.l = False
                    self.score += 100

            # 弾発射
            if pyxel.btnp(pyxel.KEY_SPACE):
                v = Vec( math.cos(self.ship.r - math.pi / 2),
                         math.sin(self.ship.r - math.pi / 2))
                
                self.bullets.append(
                    Bullet(self.ship.p, v.mul(4), 0)
                )
                # 慣性の法則で弾の速度にも自機の速度が影響
                self.ship.v = self.ship.v.add( v.mul(-0.2) )
                self.score += 10

            # 更新
            rocks = self.rocks
            self.rocks = list(filter(lambda r: r.l == True, rocks))
            for r in self.rocks: r.update(1)
            self.ship.update(1)
            bullets = self.bullets
            self.bullets = list(filter(lambda b: b.l == True, bullets))
            for b in self.bullets: b.update(1)

        # 終了
        elif self.st == 2:
            if pyxel.btnp(pyxel.KEY_RETURN):
                # 再ゲーム
                self.st = 0
        
    # 描画
    def draw(self):
        # 遊戯中    
        if self.st == 1:
            # 画面消去
            pyxel.cls(1) 
            # 自機表示
            self.ship.draw()
            # 岩表示
            for r in self.rocks: r.draw()
            # 弾表示
            for b in self.bullets: b.draw()

            # 点数表示
            pyxel.text(10,10, f'Score: {self.score}', 7)

        elif self.st == 2:
            # ゲームオーバー
            pyxel.text(140,120,"Game Over",7)
            pyxel.text(110,130,"Press Enter key to restart",7)

# メインループ
a = Asteroids()
pyxel.init(320,320,title="Asteroids",fps=20)
pyxel.run(a.update,a.draw)

# End of Asteroids.py
