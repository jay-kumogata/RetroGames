# Nixie Tube Clock v0.1: Nixie Tube Clock in Pyxel/Python
# Copyright (c) 2022 Kumogata Computing Laboratory.
# All Rights Reserved.

import pyxel

class Nixie:

    # Variables
    f1 = 0
    f2 = 1
    f3 = 2
    f4 = 3
    
    # Constructor
    def __init__( self ):
        pyxel.init( 128, 64, title="Nixie Tube Clock v0.1", fps=20)
        pyxel.load("Nixie.pyxres")
        pyxel.run(self.update,self.draw)
        
    def update( self ):
        # do nothing
        """NONE"""
        self.f1 = pyxel.frame_count % 10000 // 1000
        self.f2 = pyxel.frame_count % 1000 // 100
        self.f3 = pyxel.frame_count % 100 // 10
        self.f4 = pyxel.frame_count % 10
        
    def draw( self ):
        pyxel.cls(0)
        pyxel.blt(32, 16, 0, 0, 0, 16, 32) # tube #1
        pyxel.blt(48, 16, 0, 0, 0, 16, 32) # tube #2
        pyxel.blt(64, 16, 0, 0, 0, 16, 32) # tube #3
        pyxel.blt(80, 16, 0, 0, 0, 16, 32) # tube #4

        pyxel.blt(32, 24, 0, self.f1*16, 48, 16, 16) # figure #1
        pyxel.blt(48, 24, 0, self.f2*16, 48, 16, 16) # figure #2
        pyxel.blt(64, 24, 0, self.f3*16, 48, 16, 16) # figure #3
        pyxel.blt(80, 24, 0, self.f4*16, 48, 16, 16) # figure #4

# Main            
Nixie()

# End of Nixie.py


