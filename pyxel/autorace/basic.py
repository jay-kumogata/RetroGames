#
# 「昔のBASICゲームをPythonに移植するためのライブラリ」
#
# Jun 14, 2024 ver.1 (autorace.py対応)
#
# -*- coding: utf-8 -*-
import numpy as np  

# 仮想画面
class screen:
    def __init__(
        self, width: int, height: int
    ):
        # 初期化(仮想画面)
        self.width, self.height = width, height
        self.ch = np.full((width, height), ord(' '))
        self.fg = np.full((width, height), 7)

    # 画面表示(X座標,Y座標,キャラクタ,色属性)
    def poke(self, x: int, y: int, c: int, a: int):
        self.ch[x,y] = c
        self.fg[x,y] = a

    # 画面情報(X座標,Y座標,キャラクタ/色属性)
    def peek(self, x: int, y: int, f: bool):
        if f:
            return self.ch[x,y]
        else:
            return self.fg[x,y]

    # 画面スクロール
    def scroll(self):
        for w in range(self.width):
            for h in range(self.height-1):
                self.ch[w,h] = self.ch[w,h+1]
                self.fg[w,h] = self.fg[w,h+1]

    # 文字列を画面に表示(X座標,Y座標,文字列,色属性)
    def print(self, x:int, y:int, s: str, a:int):
        l = list(s)
        for n in range(len(l)):
            self.poke(x,y,ord(l[n]),a)
            x+=1
                
# end of basic.py            
