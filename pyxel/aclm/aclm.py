#
# ミサイル対決ゲーム「ACLM」
# ウィングマン氏作の「ACLM」を参考にしました．
# cf. 電波新聞社:「マイコン BASIC Magazine」, 1983年10月号, p.77.
#
# Sep 18, 2023 ver.1 (Pyxelによる実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel

def init():
    global st,w,h,x,y,r,a,b,pa,pb

    # 0:開始 1:遊戯中 2:自機勝利 3:敵機勝利 4:引分 5:終了
    st = 0

    # 画面サイズ
    w=128
    h=128
    
    # 自機
    x=1
    y=h-2
    r=0.7
    
    # 敵機
    a=w-2
    b=h-2
    pa=-1
    pb=-1

# 初期化    
init()
pyxel.init(w, h, title="alcm",fps=20)

def update():
    """NONE"""
    global st,r,pa,pb

    # 遊戯中
    if st == 1:
        # 自機の移動
        if pyxel.btn(pyxel.KEY_LEFT):
            r+=0.08
        if pyxel.btn(pyxel.KEY_RIGHT):
            r-=0.08

        # 自機が場外
        if x < 1 or x > w-1 or y < 1 or y > h-1:
            st=3; return
            
        # 敵機の移動
        if x > a : pa+=0.1
        if x < a : pa-=0.1
        if y > b : pb+=0.1
        if y < b : pb-=0.1
    
        if pa < -1.0 : pa+=0.1
        if pa >  1.0 : pa-=0.1
        if pb < -1.0 : pb+=0.1
        if pb >  1.0 : pb-=0.1

        # 敵機が場外
        if a < 1 or a > w-1 or b < 1 or b > h-1:
            st=2; return

        # 自機と敵機が衝突
        if int(x) == int(a) and int(y) == int(b):
            st=4; return
            
def draw():
    global st,x,y,a,b,pa,pb

    # 開始処理
    if st == 0:
    
        # 地面
        pyxel.cls(1)
        pyxel.line(0,h-1,w-1,h-1,7)

        # 状態遷移
        st = 1

    # 遊戯中
    elif st == 1:
        # 自機表示
        px=math.cos(r)
        py=math.sin(r)
        pyxel.pset(x,y,14)
        x+=px
        y-=py
        pyxel.pset(x,y,8)

        # 敵機表示
        pyxel.pset(a,b,11)
        a+=pa
        b+=pb
        pyxel.pset(a,b,3)

    # 自機の勝利
    elif st == 2:
        pyxel.text(16,16,"Very nice play!!",7)

        # 爆発アニメ
        for n in range(16):
            pyxel.circ(a,b,n,3)

        # 状態遷移
        st = 5
            
    # 敵機の勝利
    elif st == 3:
        pyxel.text(16,16,"Crash! Good luck.",7)

        # 爆発アニメ
        for n in range(16):
            pyxel.circ(x,y,n,8)

        # 状態遷移
        st = 5
            
    # 引分け
    elif st == 4:
        pyxel.text(16,16,"It's a draw. ",7)

        # 爆発アニメ
        for n in range(16):
            pyxel.circ(x,y,n,9)

        # 状態遷移
        st = 5

    # 終了
    elif st == 5:
        pyxel.text(16,24,"Hit space key to replay.",7)

        if pyxel.btn(pyxel.KEY_SPACE):
            init()
        
# メイン            
pyxel.run(update, draw)

# End of aclm.py
