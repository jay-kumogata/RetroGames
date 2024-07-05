import pyxel

class Grass:

    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.energy = 20     # この牧草を食べたときに得られる体力
        self.eaten = False  # まだ食べられていない状態
        self.sz = sz

    def update(self):
        if self.eaten:
            pyxel.rect(self.x, self.y, self.sz, self.sz, 4)  # 茶
        else:
            pyxel.rect(self.x, self.y, self.sz, self.sz, 3)  # 緑

# End of Grass.py        
