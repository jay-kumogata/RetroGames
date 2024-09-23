import math

# 2D座標を扱う関数ライブラリ
class Vec():
    def __init__(self, x : float, y: float):
        self.x = x
        self.y = y

    # ベクトル加減算
    def sub(self, p):
        return Vec(self.x - p.x, self.y - p.y)
    def add(self, p):
        return Vec(self.x + p.x, self.y + p.y)

    # ベクトル乗算
    def mul(self, s):
        return Vec(s * self.x, s * self.y)

    # ベクトル正規化
    def norm(self):
        m = self.magV()
        return Vec(self.x/m, self.y/m)

    # ベクトル長
    def magV(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # ベクトル長(制限あり)
    def limitMag(self, n):
        if self.magV() > n: return (self.norm()).mul(n)
        else: return self

    # ベクトル回転
    def rotateV(self, r):
        return Vec(
            self.x * math.cos(r) - self.y * math.sin(r),
            self.x * math.sin(r) + self.y * math.cos(r)
        )

    # 画面外に出たら反対から出現(トーラス化)
    def restoreToScreen(self):
        return Vec(
            self.cycleCoordinates(self.x), 
            self.cycleCoordinates(self.y), 
        )
    
    # 同上
    def cycleCoordinates(self, x):
        if x < -160: return 320+x
        elif x > 160: return x-320
        else: return x
    
# End of Vec.py
