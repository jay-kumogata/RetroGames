import time

class CPU:

    # References
    parent = None

    # ------------------------------------------------------------
    #   CPU Resources                                             
    # ------------------------------------------------------------

    # Registers
    PC = INST = 0
    A  = B  = Y  = Z  = 0
    _A = _B = _Y = _Z = 0

    # Flags
    F = 0

    # ------------------------------------------------------------
    #   CPU Emulation                                             
    # ------------------------------------------------------------

    # Initialize
    def CPU_Init( self, p ):
        self.parent = p
        return 0

    # Finaliaze
    def CPU_Fin( self ):
        return 0;

    # Execute
    def CPU_Step( self, cycle ):
        while cycle > 0 :
            cycle -= 1
            self.INST = self.CPU_Read( self.PC )
            self.PC += 1

            # Instructions
            if ( self.INST == 0x0 ) :
                # 0x0 : KA : Key->A
                if ( self.parent._IO.Key_F ) : 
                    self.A = self.parent._IO.Key
                    self.F = 0x0
                else:
                    self.F = 0x1
                    
            elif ( self.INST == 0x1 ) :
                # 0x1 : AO : A->7Seg.
                self.parent._IO.LED_7Seg = self.parent._IO.LED_Fig[ self.A ]
                self.F = 0x1
                
            elif ( self.INST == 0x2 ) :
                # 0x2 : CH : A<->B, Y<->Z, 1->F
                self.A, self.B = self.B, self.A
                self.Y, self.Z = self.Z, self.Y
                self.F = 0x1

            elif ( self.INST == 0x3 ) :            
                # 0x3 : CY : A<->Y, 1->F
                self.A, self.Y = self.Y, self.A
                self.F = 0x1

            elif ( self.INST == 0x4 ) :
                # 0x4 : AM : A->M(50+Y), 1->F
                self.CPU_Write( 0x50+self.Y, self.A )
                self.F = 0x1

            elif ( self.INST == 0x5 ) :
                # 0x5 : MA : M(50+Y)->A, 1->F
                self.A = self.CPU_Read( 0x50+self.Y )
                self.F = 0x1

            elif ( self.INST == 0x6 ) :
                # 0x6 : M+ : M(50+Y)+A->A, F<-Carry
                self.A = self.CPU_Read( 0x50+self.Y ) + self.A 
                if ( self.A & 0x10 ) :
                    self.A &= 0xF
                    self.F = 0x1
                else :
                    self.F = 0x0

            elif ( self.INST == 0x7 ) :
                # 0x7 : M- : M(50+Y)-A->A, F<-Borrow
                self.A = self.CPU_Read( 0x50+self.Y ) - self.A 
                if ( self.A < 0 ) :
                    self.A += 0x10
                    self.F = 0x1    
                else :
                    self.F = 0x0

            elif ( self.INST == 0x8 ) :
                # 0x8 : TIA n : n->A, 1->F
                self.A = self.CPU_Read( self.PC )
                self.PC += 1 
                self.F = 0x1

            elif ( self.INST == 0x9 ) :
                # 0x9 : AIA n : A+n->A, Carry->F
                self.A += self.CPU_Read( self.PC )
                self.PC += 1
                self.F = 0x1 if ( self.A & 0x10 ) else 0x0
                self.A &= 0xF

            elif ( self.INST == 0xA ) :
                # 0xA : TIY n : n->Y, 1->F
                self.Y = self.CPU_Read( self.PC )
                self.PC += 1
                self.F = 0x1
                
            elif ( self.INST == 0xB ) :
                # 0xB : AIY n : Y+n->Y, Carry->F
                self.Y += self.CPU_Read( self.PC )
                self.PC += 1
                self.F = 0x1 if ( self.Y & 0x10 ) else 0x0
                self.Y &= 0xF

            elif ( self.INST == 0xC ) :
                # 0xC : CIA n : A!=n, (A!=n)->F
                self.F = 0x1 if ( self.A != self.CPU_Read( self.PC ) ) else 0x0
                self.PC += 1

            elif ( self.INST == 0xD ) :
                # 0xD : CIY n : Y!=n, (Y!=n)->F
                self.F = 0x1 if ( self.Y != self.CPU_Read( self.PC ) ) else 0x0
                self.PC += 1

            elif ( self.INST == 0xE ) :
                # 0xE : CAL XXXX
                self.INST = self.CPU_Read( self.PC )
                self.PC += 1

                # Execute only if Flag=1
                if ( self.F == 0x1 ) :
                    if ( self.INST == 0x0 ) :
                        # 0xE0: CAL RSTO : 7Seg. off
                        self.parent._IO.LED_7Seg = [ 0,0,0,0,0,0,0,0 ]
                        self.F = 0x1

                    elif ( self.INST == 0x1 ) :
                        # 0xE1: CAL SETR : LED(Y) on
                        self.parent._IO.LED[ self.Y % 7 ] = 1
                        self.F = 0x1

                    elif ( self.INST == 0x2 ) :
                        # 0xE2: CAL RSTR : LED(Y) off
                        self.parent._IO.LED[ self.Y % 7 ] = 0
                        self.F = 0x1

                    elif ( self.INST == 0x4 ) :
                        # 0xE4: CAL CMPL : NOT(Ar)->Ar
                        self.A = ~self.A & 0xF
                        self.F = 0x1

                    elif ( self.INST == 0x5 ) :
                        # 0xE5: CAL CHNG : A,B,Y,Z <-> A',B',Y',Z'
                        self.A, self._A = self._A, self.A
                        self.B, self._B = self._B, self.B
                        self.Y, self._Y = self._Y, self.Y
                        self.Z, self._Z = self._Z, self.Z
                        self.F = 0x1

                    elif ( self.INST == 0x6 ) :
                        # 0xE6: CAL SIFT : Ar%2->Flag,Ar/2->Ar 
                        self.F = self.A & 0x1
                        self.A >>= 1
                        
                    elif ( self.INST == 0x7 ) :
                        # 0xE7: CAL ENDS
                        print ("sound(end)")
                        self.parent.parent.play( 0 ) 
                        self.F = 0x1

                    elif ( self.INST == 0x8 ) :
                        # 0xE8: CAL ERRS
                        print ("sound(error)")
                        self.parent.parent.play( 1 ) 
                        self.F = 0x1
                        
                    elif ( self.INST == 0x9 ) :
                        # 0xE9: CAL SHTS
                        print ("sound(short)")
                        self.parent.parent.play( 2 )
                        self.F = 0x1

                    elif ( self.INST == 0xA ) :
                        # 0xEA: CAL LONS
                        print ("sound(long)")
                        self.parent.parent.play( 3 )
                        self.F = 0x1

                    elif ( self.INST == 0xB ) :
                        # 0xEB: CAL SUND
                        print ("sound(A)")
                        self.parent.parent.play( self.A )
                        self.F = 0x1
                        
                    elif ( self.INST == 0xC ) :
                        # 0xEC: CAL TIMR
                        time.sleep(0.1*( self.A + 1 ))
                        self.F = 0x1

                    elif ( self.INST == 0xD ) :
                        # 0xED: CAL DSPR : M (5F/5E)→LED
                        m5e = self.CPU_Read( 0x5E )
                        m5f = self.CPU_Read( 0x5F )

                        # M(5E)->LED[0:3]
                        self.parent._IO.LED[ 0 ] = (m5e & 0x1)
                        self.parent._IO.LED[ 1 ] = (m5e & 0x2) >> 1
                        self.parent._IO.LED[ 2 ] = (m5e & 0x4) >> 2
                        self.parent._IO.LED[ 3 ] = (m5e & 0x8) >> 3
                        # M(5F)->LED[4:6]
                        self.parent._IO.LED[ 4 ] = (m5f & 0x1) 
                        self.parent._IO.LED[ 5 ] = (m5f & 0x2) >> 1
                        self.parent._IO.LED[ 6 ] = (m5f & 0x4) >> 2
                        self.F = 0x1

                    elif ( self.INST == 0xE ) :
                        # 0xEE: CAL DEM- : bcd(M(50+Y)-A)->M(50+Y), Y-1->Y
                        #                  assuming that borrow does not occur
                        _D = self.CPU_Read( 0x50+self.Y ) - self.A
                        self.CPU_Write( self.Y, _D % 10 )
                        self.Y -= 1
                        self.F = 0x1

                    elif ( self.INST == 0xF ) :
                        # 0xEF: CAL DEM+ : bcd(M(50+Y)+A)->M(50+Y), Y-1->Y
                        #                  assuming that carry occurs
                        _D = self.CPU_Read( 0x50+self.Y ) + self.A 
                        self.CPU_Write( 0x50+self.Y, _D % 10 )
                        if ( _D & 0x10 ) :
                            # If carry occurs, (Y-1)+1 -> (Y-1)
                            _C = self.CPU_Read( 0x50+self.Y-1 ) + 1
                            self.CPU_Write( 0x50+self.Y-1, _C )  
                        self.Y -= 1
                        self.F = 0x1
                        
            elif ( self.INST == 0xF ) :
                # 0xF : JUMP xy, 1->F
                if ( self.F == 0x1 ) :
                    self.PC = ( self.CPU_Read( self.PC ) << 4 ) + self.CPU_Read( self.PC + 1 )
                else :
                    self.PC += 2

                self.F = 0x1

        # debug messages
#        print ("PC:%02x,INST:%01x,F:%01x,A:%01x,B:%01x,Y:%01x,Z:%01x,A':%01x,B':%01x,Y':%01x,Z':%01x"
#               %(self.PC,self.INST,self.F,self.A,self.B,self.Y,self.Z,self._A,self._B,self._Y,self._Z))

#        print ("LED :%01x %01x %01x %01x %01x %01x %01x"
#               %(self.parent._IO.LED[0],self.parent._IO.LED[1],self.parent._IO.LED[2],
#                 self.parent._IO.LED[3],self.parent._IO.LED[4],self.parent._IO.LED[5],
#                 self.parent._IO.LED[6]))

#        print ("LED 7Seg.:%01x %01x %01x %01x %01x %01x %01x"
#               %(self.parent._IO.LED_7Seg[0],self.parent._IO.LED_7Seg[1],self.parent._IO.LED_7Seg[2],
#                 self.parent._IO.LED_7Seg[3],self.parent._IO.LED_7Seg[4],self.parent._IO.LED_7Seg[5],
#                 self.parent._IO.LED_7Seg[6]))

#        print ("Key_F:%01x,Key:%01x" %(self.parent._IO.Key_F,self.parent._IO.Key))
#        print ("A:%01x,M(50+Y):%01x,Y:%01x" %(self.A,self.CPU_Read( 0x50+self.Y ),self.Y))
#        print ("A:%01x,M(50+Y):%01x,Y:%01x" %(self.A,self.CPU_Read( 0x50+self.Y ),self.Y))

        return 0
                
    # ------------------------------------------------------------
    #   Memory Emulation                                          
    # ------------------------------------------------------------
    def CPU_Read( self, byAddr ) :
        return self.parent._RAM[ byAddr ]

    def CPU_Write( self, byAddr, niData ) :
        self.parent._RAM[ byAddr ] = niData
        return

# End of CPU.py
