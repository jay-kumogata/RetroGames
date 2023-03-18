import re
from CPU import *
from IO import *

class System :

    # Resources
    parent = None
    _RAM = []
    _CPU = None
    _IO = None
    
    # ------------------------------------------------------------
    #   Initialize Resources
    # ------------------------------------------------------------
    def Init( self, p, FileName ):

        self.parent = p
        
        # Initialize CPU
        self._CPU = CPU()
        self._CPU.CPU_Init( self )

        # Initialize IO
        self._IO = IO()
        self._IO.IO_Init( self )
        
        # Initialize RAM
        for _n in range ( 0x60 ) :
            self._RAM.append( 0x00 )

        # Load FXP image
        if ( self.LoadFxp( FileName ) < 0 ) :
            # Failed
            return -1
        
        print (self._RAM)

        # Successful
        return 0

    def Run( self ) :

        # Main loop
        while ( 1 ) :
            self._CPU.CPU_Step( 1 )

    # ------------------------------------------------------------
    #   Finalize Resources
    # ------------------------------------------------------------
    def Fin( self ) :
        print (self._IO.IO_Fin())
        print (self._CPU.CPU_Fin())

    # ------------------------------------------------------------
    #   Load FXP image
    # ------------------------------------------------------------
    def LoadFxp( self, FileName ) :
        print (FileName)
        try:
            # Open ROM file
            _fp = open( FileName, 'r' ) 
            print (_fp)
                
            # Allocate Memory for FXP Image
            _n = 0
            _ln = _fp.readline()

            while ( _ln ):
                _ln = _fp.readline()
                try:
                    _nb = re.search(r'<string>(\w+)</string>', _ln )
                    print (_nb.groups()[0])
                    self._RAM[ _n ] = int( _nb.groups()[0], 16 )
                    _n += 1

                except:
                    pass

            # File close
            _fp.close()

            # Successful
            return 0

        except:
            # Failed
            return -1
                
# End of System.py
