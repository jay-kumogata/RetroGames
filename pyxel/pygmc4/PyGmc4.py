# PyGmc4 v0.1: A GMC-4 emulator in Pyxel/Python
# Copyright (c) 2023 Kumogata Computing Laboratory.
# All Rights Reserved.

import pyxel
import sys, os
import threading
from System import *

class PyGmc4:
    # References
    _Sys = None

    # ------------------------------------------------------------
    #   Main Routine
    # ------------------------------------------------------------
    
    # Constructor
    def __init__( self ):
        pyxel.init( 160, 120, title="PyGmc4 v0.1", fps=30)
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
        """NONE"""
    def draw( self ):
        pyxel.cls(1)

        # LED
        for n in range( 7 ):
            if ( self._Sys._IO.LED[ n ] ) :
                pyxel.blt( n*24, 0, 0, 16, 0, 16, 16 )
            else :
                pyxel.blt( n*24, 0, 0, 0, 0, 16, 16 )

# Main            
PyGmc4()
                
# End of PyGmc4.py
