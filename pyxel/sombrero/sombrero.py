#
# 「ソンブレロ(メキシカンハット)デモ」
# 「瞬時に拡散！古いパソコンでメキシカンハットが蘇った日」を参考にしました
# cf. https://togetter.com/li/2390318
#
# Jun 25, 2024 ver.1 (Pyxelによる実装)
# Jun 26, 2024 ver.2 (SuperChip8模擬)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random
import numpy as np

def init():
    global d,dr
    
    d=np.full((160), 100)
    dr = math.pi / 180
    
def update():
    global d,dr
    """ NONE """
    return

# 画面描画            
def draw():
    global d,dr

    for y in range(-180,180,6):
        for x in range(-180,180,4):
            r=dr*math.sqrt(x*x+y*y)
            z=100*math.cos(r)-30*math.cos(3*r)
            sx=int(80+x/3-y/6)
            sy=int(40-y/6-z/4)
            if sx<0 or sx>=160: continue
            if d[sx]<=sy: continue
            zz=int((z+100)*0.035)+1
            c=0
            if zz==1 or zz==3 or zz==5 or zz==7: c += 2
            if zz==2 or zz==3 or zz>=6: c += 4
            if zz>=4: c += 8
            pyxel.pset(sx*2,sy*2,c)
            #pyxel.pset(sx,sy,c)
            #if c>0: pyxel.pset(sx*128/160,sy*64/100,7)
            d[sx]=sy

# 初期化
init()            
pyxel.init( 320, 200, title="sombrero", fps=20 )
#pyxel.init( 160, 100, title="sombrero", fps=20 )
#pyxel.init( 128, 64, title="sombrero", fps=20 )
pyxel.cls(0)
pyxel.run(update, draw)

# end of sombrero.py
