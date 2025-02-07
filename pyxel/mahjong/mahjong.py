import pyxel
import random

class Mahjong:
    def __init__( self ):
        pyxel.init( 96, 96, title="Mahjong",fps=20)
        pyxel.load( "mahjong.pyxres")
        pyxel.run(self.update, self.draw)

    def update( self ):
        """NONE"""

    def draw( self ):
        pyxel.cls(3)

        for m in range(4):
            for n in range(9):
                self.draw_mahjong(m, n, n*9+7, m*11+26)

        #for m in range(6):
        #    for n in range(9):
        #        self.draw_mahjong(random.randint(0,3),
        #                          random.randint(0,8),
        #                          n*8, m*10)

    # m: 種類(0:字牌, 1:索子, 2:筒子, 3:萬子)
    # n: 順番(数牌:0~8, 字牌: 0~6)
    def draw_mahjong( self, m, n, x, y):
        # pyxel.rectb( x, y, 10, 12, 1 )
        # pyxel.blt( x+1, y+1, 0, n*8, m*16, 8, 10 )
        pyxel.blt( x, y, 0, n*8, m*16, 8, 10 )

Mahjong()
