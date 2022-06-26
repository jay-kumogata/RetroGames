import sys

class PPU:

    # References
    parent = None

    # ------------------------------------------------------------
    #   PPU Resources                                             
    # ------------------------------------------------------------

    # Constants
    _WIDTH = 64
    _HEIGHT = 32
    _FONT_TOP = 0x0F10

    # Registers
    VRAM = []

    # Hexadecimal Fonts
    HEXFONT = [ 0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
                0x20, 0x60, 0x20, 0x20, 0x70,  # 1
                0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
                0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
                0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
                0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
                0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
                0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
                0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
                0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
                0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
                0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
                0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
                0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
                0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
                0xF0, 0x80, 0xF0, 0x80, 0x80 ] # F

    # ------------------------------------------------------------
    #   PPU Functions
    # ------------------------------------------------------------

    # PPU Initialize
    def PPU_Init( self, p ) :
        # Initialize VRAM
        for _x in range( self._WIDTH * self._HEIGHT ) :
            self.VRAM.append( 0 )

        self.PPU_Erase()

        self.parent = p
        return 0

    # PPU Finalialize
    def PPU_Fin( self ) :
        return 0

    # Erase screen
    def PPU_Erase( self ) :
        for _x in range( self._WIDTH ) :
            for _y in range( self._HEIGHT ) :
                self.PPU_SetPixel( _x, _y, 0 )

    # Set Pixel
    def PPU_SetPixel( self, x, y, c ) :
        self.VRAM[ ( y % self._HEIGHT ) * self._WIDTH + ( x % self._WIDTH ) ] = c

    # Xor Pixel
    def PPU_XorPixel( self, x, y, c ) :
        self.VRAM[ ( y % self._HEIGHT ) * self._WIDTH + ( x % self._WIDTH ) ] ^= c

    # Get Pixel
    def PPU_GetPixel( self, x, y ) :
        return self.VRAM[ ( y % self._HEIGHT ) * self._WIDTH + ( x % self._WIDTH ) ]

    # Draw sprite
    def PPU_Draw( self, vx, vy, n, i ) :
        # Clear Collision Detect Flag
        self.parent._CPU.V[ 0xF ] = 0x00

        for y in range( n ) :
            for x in range( 8 ) :
                if ( self.parent._CPU.CPU_Read( i + y ) & ( 0x80 >> x ) ) :
                    # Set Collision Detect Flag
                    if ( self.PPU_GetPixel( vx + x, vy + y ) ) :
                        self.parent._CPU.V[ 0xF ] = 0x01

                    # XOR Mode
                    self.PPU_XorPixel( vx + x, vy + y, 1 )

# End of PPU.py
