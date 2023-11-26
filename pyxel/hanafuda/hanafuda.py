#
# 花札デモ
# matt氏作の「Hanafuda Koi-Koi(Japanese card game)」を参考にしました．
# https://www.lexaloffle.com/bbs/?tid=2421
#
# Nov 26, 2023 ver.1 (first release)
#
# -*- coding: utf-8 -*-
import pyxel

class Hanafuda:
    def __init__( self ):
        # Pyxel初期化
        pyxel.init( 128, 128, title="Hanafuda", fps=20)
        pyxel.load("hanafuda.pyxres")
        pyxel.run(self.update,self.draw)

    def update( self ):
        """NONE"""

    def draw( self ):
        pyxel.cls(1)

        # 全ての花札を表示(デモ)
        for i in range(48):
            m = int( i / 4 )
            n = int( i % 4 )
            x = int( i % 8 )*15
            y = int( i / 8 )*19
            self.draw_hanafuda( m, n, x+4, y+8)

    # 花札表示
    # m: 花(0..11), n: 札(0..3)
    # x: x座標(0..113), y座標(0..109)
    def draw_hanafuda( self, m, n, x, y ):
        pyxel.rectb( x, y, 14, 18, 4 ) 
        pyxel.blt( x+1, y+1, 0, n*16, m*16, 12, 16 )

# Main
Hanafuda()

# End of Hanafuda.py
