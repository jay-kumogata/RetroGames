# PyGmc4 v0.5: A GMC-4 emulator in Pyxel/Python
# Copyright (c) 2023 Kumogata Computing Laboratory.
# All Rights Reserved.

import pyxel
import sys, os
import threading

from System import *

class PyGmc4:

    # References
    _Sys = None

    # Constants
    width = 176
    height = 104

    led_x = 154
    led_y = 13
    led_spc = 24
    led_on_x = 18
    led_on_y = 5
    led_off_x = 2
    led_off_y = 5
    led_len_x = 12
    led_len_y = 6

    _7seg_x = 14
    _7seg_y = 48
    _7seg_on_x = 24
    _7seg_on_y = 16
    _7seg_off_x = 0
    _7seg_off_y = 16

    # 7 Seg. LED
    # +-0-+ 
    # 5   1
    # +-6-+
    # 4   2
    # +-3-+ 7

    # 7 Seg. LED's pos. and size 
    # [ X pos, Y pos, X size, Y size ]
    pos = [ [  3, 1,10, 2 ],  # 0
            [ 13, 3, 2,10 ],  # 1
            [ 13,15, 2,10 ],  # 2
            [  3,25,10, 2 ],  # 3
            [  1,15, 2,10 ],  # 4
            [  1, 3, 2,10 ],  # 5
            [  3,13,10, 2 ],  # 6
            [ 17,25, 2, 2 ] ] # 7

    # ------------------------------------------------------------
    #   Main Routine
    # ------------------------------------------------------------
    
    # Constructor
    def __init__( self ):
        pyxel.init( self.width, self.height, title="PyGmc4 v0.5", fps=30)
        pyxel.load( "PyGmc4.pyxres")
        
        # Create Gmc4's System
        self._Sys = System()

        # Initialize Chip8's System
        if ( len( sys.argv ) < 2 or
             self._Sys.Init( self, sys.argv[ 1 ] ) < 0 ) :
            # Failed
            print ("Usage: python " + sys.argv[ 0 ] + " <FXP file name>")
            sys.exit()
        
        # Start Gmc4's System
        threading.Thread(target=self._Sys.Run, args=()).start()

        # Start Pyxel's System
        pyxel.run(self.update,self.draw)

    def update( self ):
        # Key Events
        self.update_key_press()
        self.update_key_release()

    def draw( self ):
        # Circuit Board
        pyxel.blt( 0,0,0,0,0,self.width,self.height)
        
        # LED
        for n in range( 7 ):
            if ( self._Sys._IO.LED[ n ] ) :
                # Nth LED ON
                pyxel.blt( self.led_x - n*self.led_spc , self.led_y, 1,
                           self.led_on_x, self.led_on_y, self.led_len_x, self.led_len_y )
            else :
                # Nth LED OFF
                pyxel.blt( self.led_x - n*self.led_spc , self.led_y, 1,
                           self.led_off_x, self.led_off_y, self.led_len_x, self.led_len_y )

        # 7Seg. LED
        for n in range( 8 ):
            if ( self._Sys._IO.LED_7Seg[ n ] ) :
                # 7Seg. LED ON
                pyxel.blt( self._7seg_x + self.pos[n][0], self._7seg_y + self.pos[n][1], 1,
                           self._7seg_on_x + self.pos[n][0], self._7seg_on_y + self.pos[n][1],
                           self.pos[n][2], self.pos[n][3] )
            else :
                # 7Seg. LED OFF
                pyxel.blt( self._7seg_x + self.pos[n][0], self._7seg_y + self.pos[n][1], 1,
                            self._7seg_off_x + self.pos[n][0], self._7seg_off_y + self.pos[n][1],
                           self.pos[n][2], self.pos[n][3] )

    # Key mapping:
    #
    # Original |C|D|E|F| Mapping to |1|2|3|4|
    #          |8|9|A|B|            |Q|W|E|R|
    #          |4|5|6|7|            |A|S|D|F|
    #          |0|1|2|3|            |Z|X|C|V|

    # Key Pressed
    def update_key_press( self ):
        if pyxel.btnp( pyxel.KEY_Z ) :
            self._Sys._IO.Key = 0x0
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_X ) :
            self._Sys._IO.Key = 0x1
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_C ) :
            self._Sys._IO.Key = 0x2
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_V ) :
            self._Sys._IO.Key = 0x3
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_A ) :
            self._Sys._IO.Key = 0x4
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_S ) :
            self._Sys._IO.Key = 0x5
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_D ) :
            self._Sys._IO.Key = 0x6
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_F ) :
            self._Sys._IO.Key = 0x7
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_Q ) :
            self._Sys._IO.Key = 0x8
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_W ) :
            self._Sys._IO.Key = 0x9
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_E ) :
            self._Sys._IO.Key = 0xA
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_R ) :
            self._Sys._IO.Key = 0xB
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_1 ) :
            self._Sys._IO.Key = 0xC
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_2 ) :
            self._Sys._IO.Key = 0xD
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_3 ) :
            self._Sys._IO.Key = 0xE
            self._Sys._IO.Key_F = 0x1
        if pyxel.btnp( pyxel.KEY_4 ) :
            self._Sys._IO.Key = 0xF
            self._Sys._IO.Key_F = 0x1
            
    # Key Released
    def update_key_release( self ):
        if pyxel.btnr( pyxel.KEY_Z ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_X ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_C ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_V ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_A ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_S ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_D ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_F ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_Q ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_W ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_E ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_R ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_1 ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_2 ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_3 ) :
            self._Sys._IO.Key_F = 0x0
        if pyxel.btnr( pyxel.KEY_4 ) :
            self._Sys._IO.Key_F = 0x0

    # Sound play no.
    # 0:G1 1:A2 2:B2 3:C2 4:D2 5:E2 6:F2 7:G2
    # 8:A3 9:B3 A:C3 B:D3 C:E3 D:F3 E:G3 F:A4
    def play(self, no):
        pyxel.play(1, no, loop = False) 
            
# Main            
PyGmc4()
                
# End of PyGmc4.py
