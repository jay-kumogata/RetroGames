import pyxel
from Vec import *

class Bullet():
    def __init__(self, p : Vec, v : Vec, a : int):
        # 弾情報Bulletは，座標Vec，速度Velocity，年齢Ageから構成．
        self.p = p
        self.v = v
        self.a = a
        self.l = True # 生死フラグ
        
    def update(self, timeStep : float):

        # 50サイクルで消滅
        if self.a > 50:
            self.l = False
        # timeStep分移動
        else:
            self.p = self.p.add(self.v.mul(timeStep))
            self.p = self.p.restoreToScreen()
            self.a += timeStep
            
    def draw(self):
        # 弾を表示
        pyxel.circb(self.p.x+160, self.p.y+160, 1, 7)

# End of Bullet.py
