#
# ロシア製8セグメントLEDのデモ
# 「ロシア語 8 セグメントディスプレイのデザイン」を参考にしました
# cf. https://www.reddit.com/r/worldbuilding/comments/8887km/russian_8_segment_display_design/?tl=ja
#
# Jan 11, 2026 ver.1 (AからLまで実装)

import pyxel

class russian8seg:

    # 8 Seg. LED
    # + +-2-+ +
    # | 4   5 |
    # 0  + +  1
    # | 6   7 |
    # + +-3-+ +

    # 8 Seg. LED's pos. and size 
    # [ X pos, Y pos, X size, Y size ]
    pos = [ [  0, 0, 3,30 ], # 0
            [ 17, 0, 3,30 ], # 1
            [  5, 0,10, 3 ], # 2
            [  5,27,10, 3 ], # 3
            [  4, 2, 5,12 ], # 4
            [ 11, 2, 5,12 ], # 5
            [  4,16, 5,12 ], # 6
            [ 11,16, 5,12 ]] # 7

    # Char data
    chr = [ [1,1,1,0,1,1,0,0], # A
            [1,0,1,1,1,1,1,1], # B
            [1,0,1,1,0,0,0,0], # C
            [0,1,0,0,0,0,1,1], # D
            [1,0,1,1,1,0,1,0], # E
            [1,0,1,0,1,0,1,0], # F
            [1,0,1,1,0,0,0,1], # G
            [1,1,0,0,1,1,1,1], # H
            [0,1,0,0,0,0,0,0], # I
            [0,1,0,1,0,0,0,0], # J
            [1,0,0,0,0,1,0,1], # K
            [1,0,0,1,0,0,0,0]] # L
    
    # Constructor
    def __init__( self ):
        pyxel.init( 300, 200, title="Russian 8 seg.")
        pyxel.load( "russian8seg.pyxres")

        # Constant
        self.ledx = 24
        self.ledy = 32

        # Start Pyxel's System
        pyxel.run( self.update, self.draw )
        
    def update( self ):
        """ dummy """

    def draw( self ):

        pyxel.cls(1)
        
        # 8 Seg. LED
        x = 10; y = 5
        for n in range(len(self.chr)):
            self.draw_led( x, y, self.chr[n] )
            x += self.ledx

    def draw_led( self, x, y, pat ):
        pyxel.blt( x, y, 0, 0, self.ledy, self.ledx, self.ledy )
        for n in range( 8 ):
            if ( n < 4 and pat[ n ] ):
                pyxel.blt( x + self.pos[n][0], y + self.pos[n][1], 0,
                           self.pos[n][0], self.pos[n][1],
                           self.pos[n][2], self.pos[n][3], 1 )
            elif ( 4 <= n and pat[ n ]):
                pyxel.blt( x + self.pos[n][0], y + self.pos[n][1], 0,
                           self.pos[n][0] + self.ledx, self.pos[n][1],
                           self.pos[n][2], self.pos[n][3], 1 )
                
# Main
russian8seg()

# End of russian8seg.py
