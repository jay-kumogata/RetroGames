# PyxelChip8 v0.3: A CHIP8 emulator in Pyxel/Python
# Copyright (c) 2022,2023 Kumogata Computing Laboratory.
# All Rights Reserved.

import pyxel
import threading
from System import *

class PyxelChip8:
    # Constants
    width = 64
    height = 32
    pixel = 4

    # 0: white 1: yellow 2: blue 3: green
    # 4: red 5: default 6: pink 7: pale green
    # 8: default 9: orange sign 10: green sign
    # 11: green and pink 12: gray and pink
    theme = 12
    
    # References
    _Sys = None

    # ------------------------------------------------------------
    #   Main Routine
    # ------------------------------------------------------------
    
    # Constructor
    def __init__( self ):
        pyxel.init( self.width*self.pixel, self.height*self.pixel ,
                    title="PyxelChip8 v0.3", fps=30)
        pyxel.load( "PyxelChip8.pyxres")
        
        # Create Chip8's System
        self._Sys = System()

        # Initialize Chip8's System
        if ( len( sys.argv ) < 2 or
             self._Sys.Init( self, sys.argv[ 1 ] ) < 0 ) :
            # Failed
            print ("Usage: python " + sys.argv[ 0 ] + " <ROM file name>")
            sys.exit()

        # Start Chip8's System
        threading.Thread(target=self._Sys.Run, args=()).start()

        # Start Pyxel's System
        pyxel.run(self.update,self.draw)

    def update( self ):
        # Key Events
        self.update_key_press()
        self.update_key_release()

    def draw( self ):
        pyxel.cls(0)
        
        for _y in range( self.height ) :
            for _x in range( self.width ) :
                if ( self._Sys._PPU.PPU_GetPixel( _x, _y ) ) :
                    # Draw Rectangle
                    pyxel.blt( _x*self.pixel, _y*self.pixel, 
                               0, 0, self.theme*self.pixel,
                               self.pixel, self.pixel)
                else :
                    # Draw None
                    pyxel.blt( _x*self.pixel, _y*self.pixel,
                               0, self.pixel, self.theme*self.pixel,
                               self.pixel, self.pixel)

    # Original |1|2|3|C| Mapping to |1|2|3|4|
    #          |4|5|6|D|            |Q|W|E|R|
    #          |7|8|9|E|            |A|S|D|F|
    #          |A|0|B|F|            |Z|X|C|V|

    # Key Pressed
    def update_key_press( self ):
        if pyxel.btnp( pyxel.KEY_X ) :
            self._Sys._IO.Key |= ( 1 << 0 )
        if pyxel.btnp( pyxel.KEY_1 ) :
            self._Sys._IO.Key |= ( 1 << 1 )
        if pyxel.btnp( pyxel.KEY_2 ) :
            self._Sys._IO.Key |= ( 1 << 2 )
        if pyxel.btnp( pyxel.KEY_3 ) :
            self._Sys._IO.Key |= ( 1 << 3 )
        if pyxel.btnp( pyxel.KEY_Q ) :
            self._Sys._IO.Key |= ( 1 << 4 )
        if pyxel.btnp( pyxel.KEY_W ) :
            self._Sys._IO.Key |= ( 1 << 5 )
        if pyxel.btnp( pyxel.KEY_E ) :
            self._Sys._IO.Key |= ( 1 << 6 )
        if pyxel.btnp( pyxel.KEY_A ) :
            self._Sys._IO.Key |= ( 1 << 7 )
        if pyxel.btnp( pyxel.KEY_S ) :
            self._Sys._IO.Key |= ( 1 << 8 )
        if pyxel.btnp( pyxel.KEY_D ) :
            self._Sys._IO.Key |= ( 1 << 9 )
        if pyxel.btnp( pyxel.KEY_Z ) :
            self._Sys._IO.Key |= ( 1 << 10 )
        if pyxel.btnp( pyxel.KEY_C ) :
            self._Sys._IO.Key |= ( 1 << 11 )
        if pyxel.btnp( pyxel.KEY_4 ) :
            self._Sys._IO.Key |= ( 1 << 12 )
        if pyxel.btnp( pyxel.KEY_R ) :
            self._Sys._IO.Key |= ( 1 << 13 )
        if pyxel.btnp( pyxel.KEY_F ) :
            self._Sys._IO.Key |= ( 1 << 14 )
        if pyxel.btnp( pyxel.KEY_V ) :
            self._Sys._IO.Key |= ( 1 << 15 )

    # Key Released
    def update_key_release( self ):
        if pyxel.btnr( pyxel.KEY_X ) :
            self._Sys._IO.Key &= ~( 1 << 0 )
        if pyxel.btnr( pyxel.KEY_1 ) :
            self._Sys._IO.Key &= ~( 1 << 1 )
        if pyxel.btnr( pyxel.KEY_2 ) :
            self._Sys._IO.Key &= ~( 1 << 2 )
        if pyxel.btnr( pyxel.KEY_3 ) :
            self._Sys._IO.Key &= ~( 1 << 3 )
        if pyxel.btnr( pyxel.KEY_Q ) :
            self._Sys._IO.Key &= ~( 1 << 4 )
        if pyxel.btnr( pyxel.KEY_W ) :
            self._Sys._IO.Key &= ~( 1 << 5 )
        if pyxel.btnr( pyxel.KEY_E ) :
            self._Sys._IO.Key &= ~( 1 << 6 )
        if pyxel.btnr( pyxel.KEY_A ) :
            self._Sys._IO.Key &= ~( 1 << 7 )
        if pyxel.btnr( pyxel.KEY_S ) :
            self._Sys._IO.Key &= ~( 1 << 8 )
        if pyxel.btnr( pyxel.KEY_D ) :
            self._Sys._IO.Key &= ~( 1 << 9 )
        if pyxel.btnr( pyxel.KEY_Z ) :
            self._Sys._IO.Key &= ~( 1 << 10 )
        if pyxel.btnr( pyxel.KEY_C ) :
            self._Sys._IO.Key &= ~( 1 << 11 )
        if pyxel.btnr( pyxel.KEY_4 ) :
            self._Sys._IO.Key &= ~( 1 << 12 )
        if pyxel.btnr( pyxel.KEY_R ) :
            self._Sys._IO.Key &= ~( 1 << 13 )
        if pyxel.btnr( pyxel.KEY_F ) :
            self._Sys._IO.Key &= ~( 1 << 14 )
        if pyxel.btnr( pyxel.KEY_V ) :
            self._Sys._IO.Key &= ~( 1 << 15 )

# Main            
PyxelChip8()
