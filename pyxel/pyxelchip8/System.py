from CPU import *
from PPU import *
from IO import *
from Profile import *

class System :

    # Compatibility Profile
    profile = Profile.SCHIP

    # Resources
    parent = None
    _RAM = [] 
    _CPU = None
    _PPU = None
    _IO = None
    
    # Constants
    _FONT_TOP = 0x0F10
    _HIGH_FONT_TOP = 0x0F60

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

    HIGH_HEXFONT = [ 0xFF, 0xFF, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xFF, 0xFF,  # 0
                     0x0C, 0x0C, 0x3C, 0x3C, 0x0C, 0x0C, 0x0C, 0x0C, 0x3F, 0x3F,  # 1
                     0xFF, 0xFF, 0x03, 0x03, 0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF,  # 2
                     0xFF, 0xFF, 0x07, 0x07, 0xFF, 0xFF, 0x07, 0x07, 0xFF, 0xFF,  # 3
                     0xC3, 0xC3, 0xC3, 0xC3, 0xFF, 0xFF, 0x03, 0x03, 0x03, 0x03,  # 4
                     0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF, 0x03, 0x03, 0xFF, 0xFF,  # 5
                     0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF, 0xC3, 0xC3, 0xFF, 0xFF,  # 6
                     0xFF, 0xFF, 0x03, 0x03, 0x0C, 0x0C, 0x30, 0x30, 0x30, 0x30,  # 7
                     0xFF, 0xFF, 0xC3, 0xC3, 0xFF, 0xFF, 0xC3, 0xC3, 0xFF, 0xFF,  # 8
                     0xFF, 0xFF, 0xC3, 0xC3, 0xFF, 0xFF, 0x03, 0x03, 0xFF, 0xFF,  # 9
                     0xFF, 0xFF, 0xC3, 0xC3, 0xFF, 0xFF, 0xC3, 0xC3, 0xC3, 0xC3,  # A
                     0xFC, 0xFC, 0xC3, 0xC3, 0xFC, 0xFC, 0xC3, 0xC3, 0xFC, 0xFC,  # B
                     0xFF, 0xFF, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xFF, 0xFF,  # C
                     0xFC, 0xFC, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xC3, 0xFC, 0xFC,  # D
                     0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF,  # E
                     0xFF, 0xFF, 0xC0, 0xC0, 0xFF, 0xFF, 0xC0, 0xC0, 0xC0, 0xC0 ] # F

    # ------------------------------------------------------------
    #   Initialize Resources
    # ------------------------------------------------------------
    def Init( self, p, FileName ) :

        self.parent = p
        
        # Initialize CPU
        self._CPU = CPU()
        self._CPU.CPU_Init( self )

        # Initialize PPU
        self._PPU = PPU()
        self._PPU.PPU_Init( self )

        # Initialize I/O
        self._IO = IO()
        self._IO.IO_Init( self )

        # Initialize RAM
        for _n in range ( 0x800 ) :
            self._RAM.append( 0x00 )

        # Load ROM image
        if ( self.LoadRom( FileName ) < 0 ) :
            # Failed
            return -1

        # Successful
        return 0

    def Run( self ) :

        # Main loop
        while ( 1 ) :
            # telmac 1800 runs at 3.2MHz and 1 instrution takes 10 clocks in average.
            # 1 chip8 operation takes 320 instructions in average.
            # so chip8 runs at 1kHz ( = 3.2MHz / (10 * 320) ).
            # this function will be called per 1/60 second.
            # so 16.67 chip8 operations will be executed per 1/60 second.
            self._CPU.CPU_Step( 17 )

            # VSYNC occurs per 1/60 second
            if ( self._IO.Delay ) :
                self._IO.Delay -= 1
            if ( self._IO.Sound ) :
                self._IO.Sound -= 1

            # Wait
            time.sleep( 0.017 )
                
    # ------------------------------------------------------------
    #   Finalize Resources
    # ------------------------------------------------------------
    def Fin( self ) :
        print (self._IO.IO_Fin())
        print (self._PPU.PPU_Fin())       
        print (self._CPU.CPU_Fin())

    # ------------------------------------------------------------
    #   Load ROM image
    # ------------------------------------------------------------
    def LoadRom( self, FileName ) :
        try:
            # Open ROM file
            _fp = open( FileName, 'rb' )

            # Allocate Memory for ROM Image
            _n = 0
            while ( 1 ) :
                _b = _fp.read( 1 )
                if ( len(_b) == 0 ) :
                    break
                self._RAM[ _n ] = ord( _b )
                _n += 1
                
            # File close
            _fp.close()

            # Successful
            return 0
            
        except:
            # Failed
            return -1
            
# End of System.py
