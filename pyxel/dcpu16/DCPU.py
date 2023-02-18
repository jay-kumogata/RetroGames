# cf. https://github.com/gustavla/dcpu16/blob/master/src/dcpu.rs

class DCPU:

    # dummy constructor
    def __init__(self):
        self.init(self)
        self.run(1)
    
    # Note: this can't be changed willy-nilly, since the PC is
    # naturally wrapped around, so it will not wrap around
    # correctly if this is changed.
    MEMORY_SIZE = 0x10000

    # Registers
    REG_A = 0
    REG_B = 1
    REG_C = 2
    REG_X = 3
    REG_Y = 4
    REG_Z = 5
    REG_I = 6
    REG_J = 7

    CYCLE_HZ = 1000000
    SHOW_ROWS_RADIUM = 1

    # References
    parent = None
    
    # ------------------------------------------------------------
    #   DCPU Resources                                             
    # ------------------------------------------------------------
    terminate = False
    reg = [0] * 8
    mem = [0] * MEMORY_SIZE
    pc = 0
    sp = 0
    ex = 0
    ia = 0
    interrupt_queueing = False
    interrupt_queue = [0] * 16
    skip_next = False
    cycle = 0
    overshot_cycles = 0
    inside_run = False
    # devices ???

    # ------------------------------------------------------------
    #   CPU Emulation                                             
    # ------------------------------------------------------------

    # Initialize
    def init( self, p ):
        self.parent = p
        return 0

    # Finaliaze
    def fin( self ):
        return 0;

    # Execute
    def run( self, cycles ):
        # Run multiple ticks until cycles have been met
        # Resets cycle count, so that it won't overflow

        self.inside_run = True
        if self.overshot_cycles > cycles :
            self.overshot_cycles -= cycles
            return 0

        end_cycle = ((self.cycle + cycles) - self.overshot_cycles)

        while self.cycle < end_cycle:
            self.tick()
        self.overshot_cycles = self.cycle - end_cycle

        # Pretend cycle is u16 and let it overflow safely
        while self.cycle > 0xffff:
            self.cycle -= 0xffff
        self.inside_run = False
        

        return 0

    def tick(self):
        self.cycle += 1




        print ("terminate:%01x" %(self.terminate))
        print ("REG_A:%04x,REG_B:%04x,REG_C:%04x,REG_X:%04x"
               %(self.reg[0],self.reg[1],self.reg[2],self.reg[3]))
        print ("REG_Y:%04x,REG_Z:%04x,REG_I:%04x,REG_J:%04x"
               %(self.reg[4],self.reg[5],self.reg[6],self.reg[7]))
        print ("pc:%04x,sp:%04x,ex:%04x,ia:%04x" %(self.pc,self.sp,self.ex,self.ia))
        print ("interrupt_queueing:%01x,skip_next:%01x,cycle:%04x,inside_run:%01x"
               %(self.interrupt_queueing,self.skip_next,self.cycle,self.inside_run))


        return 0
    
#main
DCPU()
