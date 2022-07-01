import time
from random import *

class CPU:

    # References
    parent = None

    # ------------------------------------------------------------
    #   CPU Resources                                             
    # ------------------------------------------------------------

    # Registers
    PC = 0
    I = 0
    V = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
    INST = 0
    
    # Stack
    STACK = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
    SP = 0

    # ------------------------------------------------------------
    #   CPU Emulation                                             
    # ------------------------------------------------------------

    # Initialize
    def CPU_Init( self, p ):
        self.parent = p
        self.PC = 0x0200
        self.SP = 0xF
        return 0

    # Finaliaze
    def CPU_Fin( self ):
        return 0;

    # Execute
    def CPU_Step( self, cycle ):
        while cycle > 0 :
            cycle -= 1
            self.INST = self.CPU_ReadW( self.PC )
            self.PC += 2

           # Macros
            _I = self.INST & 0xF000
            _NNN = self.INST & 0x0FFF
            _KK = self.INST & 0x00FF
            _X = ( self.INST & 0x0F00 ) >> 8
            _Y = ( self.INST & 0x00F0 ) >> 4
            _N = self.INST & 0x000F

            # Instructions
            if ( _I == 0x0000 ) :
                if ( self.INST == 0x00E0 ) :
                    # 0x00E0 : Erase the Screen
                    self.parent._PPU.PPU_Erase()

                elif ( self.INST == 0x00EE ) :
                    # 0x00EE : Return from a CHIP-8 subroutine
                    self.SP += 1;
                    self.PC = self.STACK[ self.SP & 0xF ]

            elif ( _I == 0x1000 ):
                # 0x1NNN : Jump to NNN
                self.PC = _NNN

            elif ( _I == 0x2000 ):
                # 0x2NNN : Call CHIP-8 sub-routine at NNN
                #          ( 16 successive calls max)    
                self.STACK[ self.SP & 0xF ] = self.PC
                self.SP -= 1
                self.PC = _NNN
                
            elif ( _I == 0x3000 ) :
                # 0x3XKK : Skip next instruction if VX == KK
                if ( self.V[ _X ] == _KK ):
                    self.PC += 2
                    
            elif ( _I == 0x4000 ) :
                # 0x4XKK : Skip next instruction if VX != KK
                if ( self.V[ _X ] != _KK ):
                    self.PC += 2
                        
            elif ( _I == 0x5000 ) :
                # 0x5XY0 : Skip next instruction if VX == VY
                if ( self.V[ _X ] == self.V[ _Y ] ):
                    self.PC += 2

            elif ( _I == 0x6000 ) :
               # 0x6XKK : VX = KK
               self.V[ _X ] = _KK
                
            elif ( _I == 0x7000 ) :
                # 0x7XKK : VX = VX + KK
                self.V[ _X ] += _KK
                self.V[ _X ] &= 0xFF

            elif ( _I == 0x8000 ) :
                _Z = self.INST & 0x000F

                # 0x8XY0 : VX = VY
                if ( _Z == 0x0 ) :
                    self.V[ _X ] = self.V[ _Y ]

                # 0x8XY1 : VX = VX OR VY
                elif ( _Z == 0x1 ) :
                    self.V[ _X ] |= self.V[ _Y ]

                # 0x8XY2 : VX = VX AND VY
                elif ( _Z == 0x2 ) :
                    self.V[ _X ] &= self.V[ _Y ]

                # 0x8XY3 : VX = VX XOR VY
                elif ( _Z == 0x3 ) :
                    self.V[ _X ] ^= self.V[ _Y ]

                # 0x8XY4 : VX = VX + VY, VF = Carry
                elif ( _Z == 0x4 ) :
                    self.V[ _X ] += self.V[ _Y ]
                    if ( self.V[ _X ] & 0x100 ) :
                        self.V[ _X ] &= 0xFF
                        self.V[ 0xF ] = 1
                    else:
                        self.V[ 0xF ] = 0

                # 0x8XY5 : VX = VX - VY, VF = Not Borrow
                elif ( _Z == 0x5 ) :
                    self.V[ _X ] -= self.V[ _Y ]
                    if ( self.V[ _X ] < 0 ) :
                        self.V[ _X ] += 0x100
                        self.V[ 0xF ] = 0
                    else:
                        self.V[ 0xF ] = 1

                # 0x8XY6 : VX = VX SHR 1 ( VX = VX / 2 ), VF = Carry
                elif ( _Z == 0x6 ) :
                    if ( _X == 0xF ) :
                        self.V[ 0xF ] = self.V[ _X ] & 0x01
                    else :
                        self.V[ 0xF ] = self.V[ _X ] & 0x01
                        self.V[ _X ] >>= 1
                        
                # 0x8XY7 : VX = VY - VX, VF = Not Borrow
                elif ( _Z == 0x7 ) :
                    self.V[ _X ] = self.V[ _Y ] - self.V[ _X ]
                    if ( self.V[ _X ] < 0 ) :
                        self.V[ _X ] += 0x100
                        self.V[ 0xF ] = 0
                    else:
                        self.V[ 0xF ] = 1

                # 0x8XYE : VX = VX SHL 1 ( VX = VX * 2 ), VF = Carry
                elif ( _Z == 0xE ) :
                    self.V[ _X ] <<= 1
                    if ( self.V[ _X ] & 0x100 ) :
                        self.V[ _X ] &= 0xFF
                        self.V[ 0xF ] = 1
                    else:
                        self.V[ 0xF ] = 0

            elif ( _I == 0x9000 ) :
                # 0x9XY0 : Skip next instruction if VX != VY
                if ( self.V[ _X ] != self.V[ _Y ] ) :
                    self.PC += 2

            elif ( _I == 0xA000 ) :
                # 0xANNN : I = NNN
                self.I = _NNN

            elif ( _I == 0xB000 ) :
                #  0xBNNN : Jump to NNN + V0 */
                self.PC = _NNN + self.V[ 0x0 ] 

            elif ( _I == 0xC000 ) :
                # 0xCXKK : VX = Random number AND KK

                # TETRIS
                self.V[ _X ] = randint( 0, _KK )

                # VBRIX
                #self.V[ _X ] = randint( 0, _KK - 1 )                

            elif ( _I == 0xD000 ) :
                # 0xDXYN : Draws a sprite (VX,VY) starting at M(I).
                #          VF = collision.
                self.parent._PPU.PPU_Draw( self.V[ _X ], self.V[ _Y ], _N, self.I )
                # self.parent._PPU.PPU_Blit()

            elif ( _I == 0xE000 ) :
                _ZZ = self.INST & 0x00FF
                if ( _ZZ == 0x9E ) :
                    # 0xEX9E : Skip next instruction if key VX pressed
                    if ( self.parent._IO.Key & ( 1 << self.V[ _X ] ) ) :
                        self.PC += 2

                if ( _ZZ == 0xA1 ) :
                    # 0xEXA1 : Skip next instruction if key VX not pressed
                    if ( not ( self.parent._IO.Key & ( 1 << self.V[ _X ] ) ) ):
                        self.PC += 2

            elif ( _I == 0xF000 ) :
                _ZZ = self.INST & 0x00FF
                if ( _ZZ == 0x07 ) :
                    # 0xFX07 : VX = Delay timer
                    self.V[ _X ] = self.parent._IO.Delay 

                elif ( _ZZ == 0x0A ) :
                    # 0xFX0A : Waits a keypress and stores it in VX
                    while ( self.parent._IO.Key == 0x00 ) :
                        time.sleep( 0.001 )
                    for n in range( 0x10 ) :
                        if ( self.parent._IO.Key & ( 1 << n ) ) :
                            self.V[ _X ] = n
                            break

                elif ( _ZZ == 0x15 ) :
                    # 0xFX15 : Delay timer = VX
                    self.parent._IO.Delay = self.V[ _X ]

                elif ( _ZZ == 0x18 ) :
                    # 0xFX18 : Sound timer = VX
                    self.parent._IO.Sound = self.V[ _X ]

                elif ( _ZZ == 0x1E ) :
                    # 0xFX1E : I = I + VX
                    self.I += self.V[ _X ]

                elif ( _ZZ == 0x29 ) :
                    # 0xFX29 : I points to the 4 x 5 font sprite of hex
                    #          char in VX
                    self.I = self.parent._PPU._FONT_TOP + self.V[ _X ] * 5

                elif ( _ZZ == 0x33 ) :
                    # 0xFX33 : Store BCD representation of VX in M(I)..M(I+2)
                    _A = self.V[ _X ]
                    self.CPU_Write( self.I,     int( _A / 100 ) )
                    self.CPU_Write( self.I + 1, int( ( _A % 100 ) / 10 ) )
                    self.CPU_Write( self.I + 2, int( _A % 10 ) )

                elif ( _ZZ == 0x55 ) :
                    # 0xFX55 : Save V0..VX in memory starting at M(I)
                    for _T in range( _X + 1 ) :
                        self.CPU_Write( self.I, self.V[ _T ] )
                        self.I += 1
                        
                elif ( _ZZ == 0x65 ) :
                    # 0xFX65 : Load V0..VX from memory starting at M(I)
                    for _T in range( _X + 1 ) :
                        self.V[ _T ] = self.CPU_Read( self.I )
                        self.I += 1
                        
            #print ("PC:%04x,I:%04x,INST:%04x,SP:%04x" %(self.PC,self.I,self.INST,self.SP))
            #print ("V0:%02x,V1:%02x,V2:%02x,V3:%02x" %(self.V[0],self.V[1],self.V[2],self.V[3]))
            #print ("V4:%02x,V5:%02x,V6:%02x,V7:%02x" %(self.V[4],self.V[5],self.V[6],self.V[7]))
            #print ("V8:%02x,V9:%02x,VA:%02x,VB:%02x" %(self.V[8],self.V[9],self.V[10],self.V[11]))
            #print ("VC:%02x,VD:%02x,VE:%02x,VF:%02x\n" %(self.V[12],self.V[13],self.V[14],self.V[15]))

        return 0

    # ------------------------------------------------------------
    #   Memory Emulation                                          
    # ------------------------------------------------------------
    def CPU_Read( self, wAddr ) :
        if ( wAddr < 0x200 ) :
            return 0
        elif ( wAddr < self.parent._PPU._FONT_TOP ) :
            return self.parent._RAM[ wAddr - 0x200 ]
        else :
            return self.parent._PPU.HEXFONT[ wAddr - self.parent._PPU._FONT_TOP ]

    def CPU_ReadW( self, wAddr ) :
        return ( self.CPU_Read( wAddr ) << 8 ) | self.CPU_Read( wAddr + 1 )

    def CPU_Write( self, wAddr, byData ) :
        if ( wAddr < 0x200 ) :
            return
        elif ( wAddr < self.parent._PPU._FONT_TOP ) :
            self.parent._RAM[ wAddr - 0x200 ] = byData
            return
        else :
            return

# End of CPU.py
