#
# 麻雀デモ
# まぐち氏作の「mahjong! #アイロンビーズ #ドット絵 #麻雀 #mahjong」を参考にしました．
# https://x.com/maguchi_tweet/status/876398803732934657
#
# Feb 07, 2025 ver.1 (first release)
#
# -*- coding: utf-8 -*-
import pyxel
import random

class Mahjong:
    def __init__( self ):
        pyxel.init( 96, 96, title="Mahjong", fps=20)
        pyxel.load( "mahjong.pyxres")
        pyxel.run(self.update, self.draw)

    def update( self ):
        """NONE"""

    def draw( self ):
        pyxel.cls(3)

        for m in range(4):
            for n in range(9):
                self.draw_pi(m, n, n*9+7, m*11+26)

    # m: 種類(0:字牌, 1:索子, 2:筒子, 3:萬子)
    # n: 順番(数牌:0~8, 字牌: 0~6)
    def draw_pi( self, m, n, x, y):
        pyxel.blt( x, y, 0, n*8, m*16, 8, 10 )

# Main
Mahjong()

# End of mahjong.py
