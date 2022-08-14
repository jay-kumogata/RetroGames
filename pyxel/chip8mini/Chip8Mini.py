# Chip8Mini v0.3: A CHIP8 emulator in Pyxel/Python
# Copyright (c) 2022 Kumogata Computing Laboratory.
# All Rights Reserved.

import pyxel
import threading
from System import *

class Chip8Mini:
    # Constants
    width = 64
    height = 32

    cabinet_width = 80
    cabinet_height = 120
    
    # 0: amabie 1: breakout 2: snakes 3: mastermind
    # 4: neon 5: reserved 6: reserved 7: reserved
    theme = 4
    
    # References
    _Sys = None

    # ------------------------------------------------------------
    #   Main Routine
    # ------------------------------------------------------------
    
    # Constructor
    def __init__( self ):
        pyxel.init( self.cabinet_width, self.cabinet_height,
                    title="Chip8Mini v0.3", fps=20)
        if self.theme == 0: 
            pyxel.load( "Amabie.pyxres")
        elif self.theme == 1: 
            pyxel.load( "Breakout.pyxres")
        elif self.theme == 2: 
            pyxel.load( "Snakes.pyxres")
        elif self.theme == 3: 
            pyxel.load( "Mastermind.pyxres")
        elif self.theme == 4: 
            pyxel.load( "Neon.pyxres")
            
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
        pyxel.blt(0, 0, 0, 0, 0, self.cabinet_width, self.cabinet_height)
        for _y in range( self.height ) :
            for _x in range( self.width ) :
                if ( self._Sys._PPU.PPU_GetPixel( _x, _y ) ) :
                    # Draw Rectangle
#                    pyxel.pset( _x+8,_y+24, 13)  # gray
#                    pyxel.pset( _x+8,_y+24, 9)  # amber                    
#                    pyxel.pset( _x+8,_y+24,10)  # yellow
#                    pyxel.pset( _x+8,_y+24, 8)  # magenta pink
                    pyxel.pset( _x+8,_y+24, 12) # light blue
                else :
                    # Draw None
#                    pyxel.pset( _x+8,_y+24, 1)  # dark blue
#                    pyxel.pset( _x+8,_y+24, 1)  # dark blue
#                    pyxel.pset( _x+8,_y+24, 9)  # amber
#                    pyxel.pset( _x+8,_y+24, 0)  # black
                    pyxel.pset( _x+8,_y+24, 1)  # dark blue

                    
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
Chip8Mini()

# End of Chip8Mini.py

