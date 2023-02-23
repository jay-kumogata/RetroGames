import sys

class PPU:

    # References
    parent = None

    # ------------------------------------------------------------
    #   PPU Resources                                             
    # ------------------------------------------------------------

    # Constants
    _FONT_TOP = 0x0F10

    _WIDTH = 64
    _HEIGHT = 32

    _HI_WIDTH = 128
    _HI_HEIGHT = 64

    # Registers
    VRAM = None
    HiResMode = False

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
        self.VRAM = [[0 for i in range( self._HI_HEIGHT )] for j in range( self._HI_WIDTH )]
        self.PPU_Erase()
        self.parent = p
        return 0

    # PPU Finalialize
    def PPU_Fin( self ) :
        return 0

    # Erase screen
    def PPU_Erase( self ) :
        if ( self.HiResMode ):
            # High Resolution Mode
            for _x in range( self._HI_WIDTH ) :
                for _y in range( self._HI_HEIGHT ) :
                    self.PPU_SetPixel( _x, _y, 0 )
        else:
            # Low Resolution Mode
            for _x in range( self._WIDTH ) :
                for _y in range( self._HEIGHT ) :
                    self.PPU_SetPixel( _x, _y, 0 )
                    
    # Set Pixel
    def PPU_SetPixel( self, x, y, c ) :
        if ( self.HiResMode ):
            # High Resolution Mode
            self.VRAM[ x % self._HI_WIDTH ][y % self._HI_HEIGHT] = c
        else :
            # Low Resolution Mode
            self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2     ] = c
            self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2     ] = c
            self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2 + 1 ] = c
            self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2 + 1 ] = c
            
    # Xor Pixel
    def PPU_XorPixel( self, x, y, c ) :
        if ( self.HiResMode ):
            # High Resolution Mode
            self.VRAM[ x % self._HI_WIDTH ][y % self._HI_HEIGHT] ^= c
        else :
            # Low Resolution Mode
            self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2     ] ^= c
            self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2     ] ^= c
            self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2 + 1 ] ^= c
            self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2 + 1 ] ^= c

            # Compatibility notes cf. https://chip-8.github.io/extensions/
            # In low-resolution mode (ie. the original 64 x 32), the screen memory should
            # still be represented as 128 x 64 with each “pixel” being represented by 2 x 2 pixels. 

    # Get Pixel
    def PPU_GetPixel( self, x, y ) :
        if ( self.HiResMode ):
            # High Resolution Mode
            return self.VRAM[ x % self._HI_WIDTH ][y % self._HI_HEIGHT] 
        else :
            # Low Resolution Mode
            return self.VRAM[(x % self._WIDTH) * 2 ][(y % self._HEIGHT) * 2]

    # Get VRAM directly
    def PPU_GetVRAM( self, x, y ) :
        return self.VRAM[ x % self._HI_WIDTH ][y % self._HI_HEIGHT] 

    # Set High Resolution Mode
    def PPU_SetHiResMode( self, f ) :
        self.HiResMode = f

    # Get High Resolution Mode
    def PPU_GetHiResMode( self ) :
        return self.HiResMode

    # Draws a sprite (VX,VY) starting at M(I).
    # VF = collision.
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

    # Draw 16 x 16 sprite (only if high-resolution mode is enabled)
    # VF = collision.
    def PPU_Draw16x16( self, vx, vy, n, i ) :
        # Clear Collision Detect Flag
        self.parent._CPU.V[ 0xF ] = 0x00

        for y in range( 16 ) :
            for x in range( 16 ) :
                if ( self.parent._CPU.CPU_ReadW( i + ( y << 1 ) ) & ( 0x8000 >> x ) ) :
                    # Set Collision Detect Flag
                    if ( self.PPU_GetPixel( vx + x, vy + y ) ) :
                        self.parent._CPU.V[ 0xF ] = 0x01
                                                    
                    # XOR Mode
                    self.PPU_XorPixel( vx + x, vy + y, 1 )
                        
# End of PPU.py
