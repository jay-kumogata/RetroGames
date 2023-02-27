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

    _HIGH_WIDTH = 128
    _HIGH_HEIGHT = 64

    # Registers
    VRAM = None
    HIGH_RES = False
    
    # ------------------------------------------------------------
    #   PPU Functions
    # ------------------------------------------------------------

    # PPU Initialize
    def PPU_Init( self, p ) :
        # Initialize VRAM
        self.VRAM = [[0 for i in range( self._HIGH_HEIGHT )] for j in range( self._HIGH_WIDTH )]

        self.PPU_Erase()
        self.parent = p
        return 0

    # PPU Finalialize
    def PPU_Fin( self ) :
        return 0

    # ------------------------------------------------------------
    #   SuperChip 1.0 
    # ------------------------------------------------------------

    # Compatibility notes cf. https://chip-8.github.io/extensions/#super-chip-10
    # In low-resolution mode (ie. the original 64 x 32), the screen memory should
    # still be represented as 128 x 64 with each “pixel” being represented by 2 x 2 pixels. 
    
    # Erase screen
    def PPU_Erase( self ) :
        if ( self.HIGH_RES ):
            # High Resolution Mode
            for _x in range( self._HIGH_WIDTH ) :
                for _y in range( self._HIGH_HEIGHT ) :
                    self.PPU_SetPixel( _x, _y, 0 )
        else:
            # Low Resolution Mode
            for _x in range( self._WIDTH ) :
                for _y in range( self._HEIGHT ) :
                    self.PPU_SetPixel( _x, _y, 0 )
                    
    # Set Pixel
    def PPU_SetPixel( self, x, y, c ) :
        if ( self.HIGH_RES ):
            # VIP, SCHIP: clip sprites at screen edges instead of wrapping.
            if ( x < self._HIGH_WIDTH and y < self._HIGH_HEIGHT ) :
                # High Resolution Mode
                self.VRAM[ x % self._HIGH_WIDTH ][y % self._HIGH_HEIGHT] = c
        else :
            # VIP, SCHIP: clip sprites at screen edges instead of wrapping.
            if ( x < self._WIDTH and y < self._HEIGHT ) :
                # Low Resolution Mode
                self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2     ] = c
                self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2     ] = c
                self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2 + 1 ] = c
                self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2 + 1 ] = c
            
    # Xor Pixel
    def PPU_XorPixel( self, x, y, c ) :
        if ( self.HIGH_RES ):
            # VIP, SCHIP: clip sprites at screen edges instead of wrapping.
            if ( x < self._HIGH_WIDTH and y < self._HIGH_HEIGHT ) :
                # High Resolution Mode
                self.VRAM[ x % self._HIGH_WIDTH ][y % self._HIGH_HEIGHT] ^= c
        else :
            # VIP, SCHIP: clip sprites at screen edges instead of wrapping.
            if ( x < self._WIDTH and y < self._HEIGHT ) :
                # Low Resolution Mode
                self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2     ] ^= c
                self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2     ] ^= c
                self.VRAM[ (x % self._WIDTH) * 2     ][(y % self._HEIGHT) * 2 + 1 ] ^= c
                self.VRAM[ (x % self._WIDTH) * 2 + 1 ][(y % self._HEIGHT) * 2 + 1 ] ^= c

    # Get Pixel
    def PPU_GetPixel( self, x, y ) :
        if ( self.HIGH_RES ):
            # High Resolution Mode
            return self.VRAM[ x % self._HIGH_WIDTH ][y % self._HIGH_HEIGHT] 
        else :
            # Low Resolution Mode
            return self.VRAM[(x % self._WIDTH) * 2 ][(y % self._HEIGHT) * 2]

    # Get VRAM directly
    def PPU_GetVRAM( self, x, y ) :
        return self.VRAM[ x % self._HIGH_WIDTH ][y % self._HIGH_HEIGHT] 

    # Enable High Resolution Mode
    def PPU_EnableHighRes( self, f ) :
        self.HIGH_RES = f

    # Check High Resolution Mode
    def PPU_isHighRes( self ) :
        return self.HIGH_RES

    # ------------------------------------------------------------
    #   SuperChip 1.1 
    # ------------------------------------------------------------
    
    # TODO: Compatibility notes cf. https://chip-8.github.io/extensions/#super-chip-11
    # In high resolution mode, DXYN/DXY0 sets VF to the number of rows that either
    # collide with another sprite or are clipped by the bottom of the screen.
    # The original CHIP-8 interpreter only set VF to 1 if there was a collision.

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

    # Scroll display N pixels down; in low resolution mode, N/2 pixels                
    def PPU_ScrollDown( self, n ) :
        for x in range( self._HIGH_WIDTH ) :
            for y in range( n ) :
                self.VRAM[ x ].pop(-1)
                self.VRAM[ x ].insert(0, 0)

    # Scroll display N pixels up; in low resolution mode, N/2 pixels
    def PPU_ScrollUp( self, n ) :
        for x in range( self._HIGH_WIDTH ) :
            for y in range( n ) :
                self.VRAM[ x ].pop(0)
                self.VRAM[ x ].insert(-1, 0)

                
    # Scroll left by 4 pixels; in low resolution mode, 2 pixels
    def PPU_ScrollLeft( self ) :
        for x in range( 4 ) :
            self.VRAM.pop(0)
            self.VRAM.insert(-1, ([0 for i in range( self._HIGH_HEIGHT )]))

    # Scroll right by 4 pixels; in low resolution mode, 2 pixels
    def PPU_ScrollRight( self ) :
        for x in range( 4 ) :
            self.VRAM.pop(-1)
            self.VRAM.insert(0, ([0 for i in range( self._HIGH_HEIGHT )]))
            
# End of PPU.py
