#
# 「オートレース(1画面ソフト) 」
# 高橋はるみ氏作の「オートレース(1画面ソフト) 」を参考にしました．
# cf. 高橋はるみ:「FM-7 FM-8 はるみのゲーム・ライブラリー」, 株式会社ナツメ社, 1983年.
#
# Jun 14, 2024 ver.1 (Pyxelによる実装)
#
# -*- coding: utf-8 -*-
import pyxel
import random
import basic 

width = 40
height = 20
chr_x = 4
chr_y = 5

def init():
    global st,s, x, i

    # 0:遊戯中 1:終了
    st = 0
    
    # 画面初期化(10行目)，画面クリア(12行目)
    s = basic.screen(width, height)
    # 車位置初期化(12行目)
    x = 2
    # カウンタ初期化，Beep音初期化(14行目)
    i = 0

# メインループ
def update():
    global st, s, x, i

    # 遊戯中    
    if st == 0:
        # 車消去，Beep音(16行目)
        s.print(x,4," ",7)
        pyxel.play(0,0)
        # キー入力チェック，左移動(17行目)
        if pyxel.btnp(pyxel.KEY_LEFT) and x > 1: x -= 1
        # キー入力チェック，左移動(18行目)
        if pyxel.btnp(pyxel.KEY_RIGHT) and x < 4: x += 1
        # 車衝突チェック(19行目)
        if s.peek(x,5,True) > ord(' '):
            # 終了
            st = 1
            return
        # 道路表示(20行目)
        s.print(0,19,"|    |",1)
        # 最下段に文字が表示されると自動的に縦スクロール(BASIC仕様)
        s.scroll()
        # 車表示(21行目)
        s.print(x,4,"U",2)
        # 障害物表示(22行目)
        s.print(random.randint(1,4),18,"+",3)
        # ゴール表示(23行目)
        if i == 186:
            s.print(0,18,"-GOAL-",4)
        # カウントアップ(24行目)
        i += 1

    # 終了
    elif st == 1:
        # ゲームオーバ，スコア表示(30行目)
        s.print(9,9,"**** GAME OVER ****",8)
        s.print(13,11,f"[:SCORE {i}]",9)
        
        # キー入力チェック，再ゲーム(31行目)  
        if pyxel.btnp(pyxel.KEY_S):
            # 再ゲーム
            init()

# 画面描画            
def draw():
    global st, s, x, i

    pyxel.cls(0)
    for w in range(s.width):
        for h in range(s.height):
            pyxel.text(w*4,h*5,chr(s.peek(w,h,True)), s.peek(w,h,False))

# 初期化
init()            
pyxel.init( width*chr_x, height*chr_y, title="autorace", fps=5 )
pyxel.sounds[0].set("a2","p","6","n",2)
pyxel.run(update, draw)

# end of autorace.py            
