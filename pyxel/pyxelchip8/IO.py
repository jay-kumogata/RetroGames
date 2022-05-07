class IO :

    # References
    parent = None
    
    # ------------------------------------------------------------
    #   I/O Resources                                             
    # ------------------------------------------------------------

    # Delay Timer
    Delay = 0

    # Sound Timer
    Sound = 0

    # Key State : FEDCBA9876543210
    Key = 0
    Esc = 0

    # ------------------------------------------------------------
    #   I/O Emulation
    # ------------------------------------------------------------

    # I/O Initialize
    def IO_Init( self, p ) :
        self.parent = p

        # Delay Timer
        self.Delay = 0

        # Sound Timer
        self.Sound = 0

        # Key State : FEDCBA9876543210 */
        self.Key = 0
        self.Esc = 0

        return 0

    # I/O Finalialize
    def IO_Fin( self ) :

        return 0

# End of IO.py
