from CPU import *
from PPU import *
from IO import *

class System :

    # Resources
    parent = None
    _RAM = [] 
    _CPU = None
    _PPU = None
    _IO = None
    
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
        # print self._RAM
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
            time.sleep( 0.136 )            
#            time.sleep( 0.068 )            
#            time.sleep( 0.034 )
#            time.sleep( 0.017 )
#            time.sleep( 0.0085 )
#            time.sleep( 0.00425 )
                
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

