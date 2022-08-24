#
# Pyxelを使ってGray-Scottモデルを表示
# 「作って動かすALife - 実装を通した人工生命モデル理論入門」サンプルコード を参考にしました．
# https://github.com/alifelab/alife_book_src/blob/master/chap02/gray_scott.py
#
# May 03, 2022 ver.1 (changed graphics library to pyxel)
# Aug 24, 2022 ver.2 (code refactoring)
#

# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# シミュレーションの各パラメタ
SPACE_GRID_SIZE = 256
dx = 0.01
dt = 1

# 何ステップごとに画面を更新するか
# VISUALIZATION_STEP = 5  # amorphous
# VISUALIZATION_STEP = 20  # spots 
VISUALIZATION_STEP = 10  # wandering bubbles 
# VISUALIZATION_STEP = 5  # waves

# モデルの各パラメタ
Du = 2e-5
Dv = 1e-5
# f, k = 0.04, 0.06  # amorphous
# f, k = 0.035, 0.065  # spots
f, k = 0.012, 0.05  # wandering bubbles
# f, k = 0.025, 0.05  # waves
# f, k = 0.022, 0.051 # stripe

# 初期化
u = np.ones((SPACE_GRID_SIZE, SPACE_GRID_SIZE))
v = np.zeros((SPACE_GRID_SIZE, SPACE_GRID_SIZE))
# 中央にSQUARE_SIZE四方の正方形を置く
SQUARE_SIZE = 20
u[SPACE_GRID_SIZE//2-SQUARE_SIZE//2:SPACE_GRID_SIZE//2+SQUARE_SIZE//2,
  SPACE_GRID_SIZE//2-SQUARE_SIZE//2:SPACE_GRID_SIZE//2+SQUARE_SIZE//2] = 0.5
v[SPACE_GRID_SIZE//2-SQUARE_SIZE//2:SPACE_GRID_SIZE//2+SQUARE_SIZE//2,
  SPACE_GRID_SIZE//2-SQUARE_SIZE//2:SPACE_GRID_SIZE//2+SQUARE_SIZE//2] = 0.25
# 対称性を壊すために、少しノイズを入れる
u += np.random.rand(SPACE_GRID_SIZE, SPACE_GRID_SIZE)*0.1
v += np.random.rand(SPACE_GRID_SIZE, SPACE_GRID_SIZE)*0.1

# Pyxel初期化
pyxel.init(SPACE_GRID_SIZE, SPACE_GRID_SIZE, title="grayscott")

def update():
    for i in range(VISUALIZATION_STEP):    
        # ラプラシアンの計算
        laplacian_u = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) +
                       np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 4*u) / (dx*dx)
        laplacian_v = (np.roll(v, 1, axis=0) + np.roll(v, -1, axis=0) +
                       np.roll(v, 1, axis=1) + np.roll(v, -1, axis=1) - 4*v) / (dx*dx)
        # Gray-Scottモデル方程式
        dudt = Du*laplacian_u - u*v*v + f*(1.0-u)
        dvdt = Dv*laplacian_v + u*v*v - (f+k)*v
        
        # 変数を更新
        u[0:SPACE_GRID_SIZE, 0:SPACE_GRID_SIZE] +=  dt * dudt
        v[0:SPACE_GRID_SIZE, 0:SPACE_GRID_SIZE] +=  dt * dvdt

def draw():
    pyxel.cls(0)
    for x in range(SPACE_GRID_SIZE):
        for y in range(SPACE_GRID_SIZE):
#            c = int((u[x, y]+0.5) * 8.0) # 明色
            c = 15 - int((u[x, y]+0.5) * 8.0) # 暗色
            pyxel.pset(x, y, c)
    # 時間表示
    s = ( f"t = {VISUALIZATION_STEP * pyxel.frame_count * dt:.2f}\n" )
    pyxel.text(0,0,s,0)
            
# メイン
pyxel.run(update, draw)

# end of grayscott.py
