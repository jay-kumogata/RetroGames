#
# Pyxelを使った「食事をする羊のプログラム」
# 書籍「Pythonではじめる数学の冒険―プログラミングで図解する代数、幾何学、三角関数」を参考にしました．
# https://www.oreilly.co.jp/books/9784873119304/
#
# Apr 19, 2024 ver.1 (Pyxelへ移植)
#
# -*- coding: utf-8 -*-
import random
import pyxel
from Sheep import *
from Grass import *

class SheepAndGrass:

    def __init__( self ):

        # ウィンドウサイズ
        self.width = 128
        self.height = 128
        
        self.sheepList = []  # 羊用のリスト
        self.grassList = []  # 牧草用のリスト
        self.patchSize = 4   # 牧草の1区画の大きさ
        self.rows_of_grass = int( self.height / self.patchSize)

        # 羊を作る
        for n in range(20):
            sheep = Sheep(random.randint(0, self.width),random.randint(0, self.height))
            sheep.p = self
            self.sheepList.append(sheep)

        # 牧草を作る
        for x in range(0, self.width, self.patchSize):
            for y in range(0, self.height, self.patchSize):
                self.grassList.append(Grass(x, y, self.patchSize))

        # Pyxel初期化
        pyxel.init( self.width, self.height, title="SheepAndGrass", fps=10)
        pyxel.run(self.update, self.draw)

    def update(self):
        """NONE"""
    def draw(self):
        pyxel.cls(1)

        # 先に牧草を更新
        for grass in self.grassList:
            grass.update()

        # 続いて羊を更新
        for sheep in self.sheepList:
            sheep.update()

# Main
SheepAndGrass()

# End of SheepAndGrass.py            
                                  
