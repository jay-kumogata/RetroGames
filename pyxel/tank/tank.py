import pyxel

class Tank:
    def __init__(self):
        self.x = 0x20
        self.y = 0x10
        self.i = 0

        pyxel.init(64, 32, title="tank", fps=20)
        pyxel.load("tank.pyxres")
        pyxel.run(self.update, self.draw)

    def up(self):
        self.y -= 1
        self.i = 0

    def down(self):
        self.y += 1
        self.i = 1

    def left(self):
        self.x -= 1
        self.i = 2

    def right(self):
        self.x += 1
        self.i = 3

    def update(self):
        if pyxel.btnp( pyxel.KEY_UP ): self.up()
        if pyxel.btnp( pyxel.KEY_DOWN ): self.down()
        if pyxel.btnp( pyxel.KEY_LEFT ): self.left()
        if pyxel.btnp( pyxel.KEY_RIGHT ): self.right()
            
    def draw(self):
        pyxel.cls(1)
        pyxel.blt(self.x, self.y, 0, self.i*8, 0, 8, 7)

Tank()        
