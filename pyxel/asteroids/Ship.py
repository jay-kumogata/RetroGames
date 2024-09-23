import pyxel
from Vec import *

class Ship():
    # 船情報Shipは，座標Vec，速度Velocityから構成．
    def __init__(self, p : Vec, v : Vec):
        self.p = p
        self.v = v
        self.s = [[0, -4], [-2, 4], [2, 4], [0, -4]]
        self.r = math.pi / 2

    def update(self, timeStep : float):
        # 弾を発射したら反動で動く
        self.p = self.p.add(self.v.mul(timeStep))
        self.p = self.p.restoreToScreen()

        # 回転
        if pyxel.btn(pyxel.KEY_LEFT):
            self.r -= math.pi / 8
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.r += math.pi / 8
            
        if self.r < 0:
            self.r += 2 * math.pi
        elif self.r > 2 * math.pi:
            self.r -= 2 * math.pi
            
    def draw(self):
        a = []
        for b in self.s:
            a.append(Vec(b[0],b[1]).rotateV(self.r))
            
        for n in range(len(self.s)-1):
            pyxel.line( self.p.x+a[n].x+160,
                        self.p.y+a[n].y+160,
                        self.p.x+a[n+1].x+160,
                        self.p.y+a[n+1].y+160,
                        7 )

# End of Ship.py
