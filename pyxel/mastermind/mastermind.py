##################################################################################
#
# 4 Row Mastermind (Robert Lindley, 1978)
# remasterd in pyxel by Jay Kumogata on Mar. 02, 2025
#
# Nov. 06, 2021 (ver.1) Decompiled from binary file[1]
# Nov. 10, 2021 (ver.2) Annotate from information in this article[2]
# Nov. 16, 2021 (ver.3) Changed to fashionable number fonts
# Nov. 17, 2021 (ver.4) Changed to mahjong tile characters
# Mar. 02, 2025 (ver.5) Remastered to pyxel/python 
#
# [1] Mastermind FourRow (Robert Lindley, 1978).ch8
# [2] R. Lindley: 5 Row Mastermind, Viper Vol.1 Issue7, pp.22-26 (Feb. 1978).
# 
##################################################################################

import pyxel
import random
import numpy as np

class Mastermind:
    def __init__(self):
        self.init()

        pyxel.init(98, 80, title="MasterMind", fps=20)
        pyxel.load("mastermind.pyxres")
        pyxel.run(self.update,self.draw)

    def init(self):
        # 状態
        #   0: 初期化
        #   1: プレイ中(キー入力)
        #   2: プレイ中(判定中)
        #   3: プレイ中(正解表示)
        self.st = 0

        # 定数
        self.column = 10
        self.row = 4
        self.pi = random.randint(1,3) # 種類(1:索子, 2:筒子, 3:萬子)

        # 盤面(行×列, 整数型)
        #   0: 空(ダッシュ)
        #   1～6: 数(1～6)
        self.board = np.zeros((self.column, self.row), dtype = int)

        # 判定結果(行×列, 整数型)
        #   0: 数，位置共に，不一致(空白)
        #   1: 数は一致，位置は不一致(ホワイトバー)
        #   2: 数，位置共に，一致(ドットバー)
        self.res = np.zeros((self.column, self.row), dtype = int)

        # 解答(最小: 1, 最大: 6, 個数:列)
        #   1～6: 数(1～6)
        self.ans = np.random.randint(1, 7, self.row)

        # 入力場所
        self.c = 0 # 盤面(列)
        self.r = 0 # 盤面(行)
        self.c2 = 0 # 判定結果(列)

        # 状態遷移
        self.st = 1

    def update( self ):
        # プレイ中(キー入力)
        if self.st == 1:

            # 数字キー入力
            if pyxel.btnp(pyxel.KEY_1): self.board[self.r,self.c] = 1; self.c += 1
            if pyxel.btnp(pyxel.KEY_2): self.board[self.r,self.c] = 2; self.c += 1
            if pyxel.btnp(pyxel.KEY_3): self.board[self.r,self.c] = 3; self.c += 1
            if pyxel.btnp(pyxel.KEY_4): self.board[self.r,self.c] = 4; self.c += 1
            if pyxel.btnp(pyxel.KEY_5): self.board[self.r,self.c] = 5; self.c += 1
            if pyxel.btnp(pyxel.KEY_6): self.board[self.r,self.c] = 6; self.c += 1

            # キャンセル(ENTERキー入力)
            if pyxel.btnp(pyxel.KEY_RETURN) and self.c != 0:
                self.c -= 1; self.board[self.r,self.c] = 0

            # 4個入力されたか
            if self.c == 4: self.c = 0; self.st = 2

        # プレイ中(判定中)
        elif self.st == 2:
            board_cp = self.board[self.r,].copy()
            ans_cp = self.ans.copy()

            # ドットバーテスト
            for i in range(4):
                for j in range(4):
                    # 解答か数字かのいずれかが対象外の場合はスキップ
                    if ans_cp[i] < 0 or board_cp[j] < 0:
                        continue

                    # 数字，位置共に一致
                    if ans_cp[i] == board_cp[j] and i == j:
                        # ドットバー
                        self.res[self.r,self.c2] = 2; self.c2 += 1

                        # 数字，位置共に一致した数字は対象外
                        ans_cp[i] = -1
                        board_cp[j] = -1

                        # 次の数字
                        break

            # ホワイトバーテスト
            for i in range(4):
                for j in range(4):
                    # 解答か数字かのいずれかが対象外の場合はスキップ
                    if ans_cp[i] < 0 or board_cp[j] < 0:
                        continue
                    
                    # 数字，位置共に一致
                    if ans_cp[i] == board_cp[j] and i != j:
                        # ホワイトバー
                        self.res[self.r,self.c2] = 1; self.c2 += 1

                        # 対象外フラグ設定
                        ans_cp[i] = -1
                        board_cp[j] = -1

                        # 次の数字
                        break

            # すべての数字，位置が一致したか
            if self.res[self.r,0] == 2 and \
               self.res[self.r,1] == 2 and \
               self.res[self.r,2] == 2 and \
               self.res[self.r,3] == 2 :
                # 状態遷移
                self.st = 3
            else:
                # 次の行
                self.r += 1; self.c2 = 0

                # 10回以下しか試行していないか
                if self.r < 10:
                    # 状態遷移
                    self.st = 1
                else:
                    # 状態遷移
                    self.st = 3

        # プレイ中(正解表示)
        elif self.st == 3:

            # 再ゲーム
            if pyxel.btnp(pyxel.KEY_RETURN):

                # 初期化
                self.init()

                # 状態遷移
                self.st = 1
                
    def draw(self):
        # 画面消去
        pyxel.cls(1)

        # プレイ中(キー入力 or 判定中 or 結果表示)
        if self.st == 1 or self.st == 2 or self.st == 3:
            # 盤面表示
            for c in range(10):
                for r in range(4):
                    if self.board[c,r] == 0:
                        # 裏牌(裏返しの状態)
                        self.draw_pi(0, 7, c*9, r*11)
                    else:
                
                        # 表牌(表返しの状態)
                        self.draw_pi(self.pi, self.board[c,r]-1, c*9, r*11)

            # 結果表示
            for c in range(10):
                for r in range(4):
                    # 変換テーブル(0:空白，1:ホワイトバー，2:ドットバー)
                    #   索子 0: 白棒，1: 千点棒，2: 1万点棒
                    #   筒子 0: 白棒，1: 5百点棒，2: 5千点棒
                    #   萬子 0: 白棒，1: 百点棒，2: 千点棒
                    tbl = [5, self.pi+1, self.pi-1]

                    # 点棒表示
                    self.draw_bou(4, tbl[self.res[c,r]],c*9,r*4+48)

        # プレイ中(解答表示)
        if self.st == 3:
            if (pyxel.frame_count %480) % 2 == 0:
                # 解答表示
                for r in range(4):
                    self.draw_pi(self.pi,self.ans[r]-1,10*9,r*11)

            # メッセージ表示(適当)
            pyxel.text(0, 68, "Game Over", 7)
            if self.r < 10:
                pyxel.text(0, 74, "You win.", 7)
            else:
                pyxel.text(0, 74, "You lose.", 7)

    # 牌表示
    #   m: 種類(0:字牌,1:索子, 2:筒子, 3:萬子)
    #   n: 順番(字牌: 0～7，数牌：0～8)
    #   x,y: 表示位置(ピクセル)
    def draw_pi(self, m, n, x, y):
        pyxel.blt( x, y, 0, n*8, m*16, 8, 10)

    # 点棒表示
    #   m: 版(4: 第1版)
    #   n: 種類(0:1万点棒, 1:5千点棒, 2:千点棒, 3:5百点棒, 4: 百点棒, 5: 白棒)
    #   x,y: 表示位置(ピクセル)
    def draw_bou(self, m, n, x, y):
        pyxel.blt( x, y, 0, n*8, m*16, 8, 3)

Mastermind()

# End of mastermind.py
