# Pyxelを使ってMandelbrot集合を表示(2022.09.11)
# 「morikomorou’s blog
# 【python】matplotlibでフラクタル図形(マンデルブロ集合)を描く」を参考にしました．
# https://mori-memo.hateblo.jp/entry/2022/02/08/012422

# -*- coding: utf-8 -*-
import numpy as np
import pyxel

re_min = -2.0
re_max = 2.0
im_max = 2.0
im_min = -2.0

re_v = .1
im_v = .1

def mandelbrot(max, comp):
    re, im = comp[0], comp[1]
    #実部がre，虚部がimの複素数を作成
    c = complex(re, im)

    #Z_nの初項は0
    z = complex(0, 0)

    for i in range(max):
        z = z*z + c
        #zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z) >= 2:
            return i
    
    return max     #無限大に発散しない場合にはmaxを返す

# Pyxel初期化
pyxel.init(128, 128, title="mandelbrot")

def update():
    global re_min,re_max,im_max,im_min,re_v,im_v

    if pyxel.btn(pyxel.KEY_LEFT):
        re_min -= re_v
        re_max -= re_v
    if pyxel.btn(pyxel.KEY_RIGHT):
        re_min += re_v
        re_max += re_v
    if pyxel.btn(pyxel.KEY_DOWN):
        im_max -= im_v
        im_min -= im_v
    if pyxel.btn(pyxel.KEY_UP):
        im_max += im_v
        im_min += im_v
    if pyxel.btn(pyxel.KEY_Z):
        re_min *= .99
        re_max *= .99
        im_max *= .99
        im_min *= .99
        re_v   *= .99
        im_v   *= .99
    if pyxel.btn(pyxel.KEY_X):
        re_min *= 1.01
        re_max *= 1.01
        im_max *= 1.01
        im_min *= 1.01
        re_v   *= 1.01
        im_v   *= 1.01
        
def draw():

    global re_min,re_max,im_max,im_min
    
    re = np.linspace(re_min, re_max, 128)
    im = np.linspace(im_max, im_min, 128)

    #実部と虚部の組み合わせを作成
    Re, Im = np.meshgrid(re, im)
    comp = np.c_[Re.ravel(), Im.ravel()]

    Mandelbrot = np.zeros(len(comp))

    #マンデルブロ集合に属するかの計算
    for i, c_point in enumerate(comp):
        Mandelbrot[i] = mandelbrot(100, c_point)

    Mandelbrot = Mandelbrot.reshape((128, 128))

    pyxel.cls(0)

    for x in range(128):
        for y in range(128):
            c = int(Mandelbrot[x,y]) % 16
            pyxel.pset(y, x, c)

    # 時間表示
    # s = ( f"t = {pyxel.frame_count :.2f}\n" )
    # pyxel.text(0,0,s,1)

# メイン
pyxel.run(update, draw)

# end of mandelbrot.py
