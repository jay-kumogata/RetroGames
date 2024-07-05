import random
import pyxel

class Sheep:
    def __init__(self, x, y):
        self.p = None                      # 参照元
        self.x = x                         # x座標
        self.y = y                         # y座標 
        self.sz = 2                        # 大きさ
        self.energy = 20                   # 体力
        self.col = random.randint( 6, 15 ) # 色
        
    def update(self):
        # 羊がランダムに動き回るようにする
        move = 1 # 任意の方向に移動するときの最大距離
        self.energy -= 1
        if self.energy <= 0:
            self.p.sheepList.remove(self)
        self.x += random.randint( -move, move )
        self.y += random.randint( -move, move )

        # Asteroids式の「丸め」
        if self.x >= self.p.width:
            self.x %= self.p.width
        if self.y >= self.p.height:
            self.y %= self.p.height
        if self.x < 0:
            self.x += self.p.width
        if self.y < 0:
            self.y += self.p.height
        
        # grassListの中から牧草区画を見つける
        xscl = int(self.x / self.p.patchSize)
        yscl = int(self.y / self.p.patchSize)

        grass = self.p.grassList[xscl * self.p.rows_of_grass + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        
        pyxel.circ(self.x,self.y,self.sz,self.col)

# End of Sheep.py        
