import pyxel
from Vec import *

class Rock():
    def __init__(self, p : Vec, s : float, v : Vec):
        # 岩情報Rockは，座標Vec，サイズSize，速度Velocityから構成．
        self.p = p
        self.s = s
        self.v = v
        self.l = True

        # 岩形状
        self.r = [[+0.7, +0.5],
                  [-0.1, +0.8], 
                  [-0.7, +0.6],
                  [-0.9, -0.1],
                  [-0.7, -0.9],
                  [+0.0, -0.7],
                  [+0.6, -0.8],
                  [+0.9, -0.2],
                  [+0.5, +0.1],
                  [+0.7, +0.5]]

    # 座標pが，岩Rockに衝突したか否かを返却．
    # 岩座標rpから岩サイズsだけ離れた領域（円）に，座標pが含まれるか否かを返却．
    def collidesWith(self, p : Vec):
        rp = self.p
        rp = rp.sub(p)
        rp = rp.magV()
        return rp < self.s
    
    # 時間timeStep分だけ位置を更新．
    # 岩に弾が当たって，岩のサイズが7の場合は，ここに含まれる．
    def update(self, timeStep : float):
        self.p = self.p.add(self.v.mul(timeStep))
        self.p = self.p.restoreToScreen()

    # 岩を描画
    def draw(self):
        for n in range(len(self.r)-1):
            pyxel.line( self.p.x+self.r[n][0]*self.s+160,
                        self.p.y+self.r[n][1]*self.s+160,
                        self.p.x+self.r[n+1][0]*self.s+160,
                        self.p.y+self.r[n+1][1]*self.s+160,
                        7 )

# End of Rock.py
