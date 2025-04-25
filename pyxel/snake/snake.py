# Note: this source has been ported to Octo by Jay Kumogata on 14 Aug 2021.
#       (only the notation changed: it has been converted manually.)
#       And has been converted to Pyxel/Python with Grok3(beta) on 17 Apr 2025.
# 
#---------------------------------------------------------------------------
# This is a simple version of the game Snake for the CHIP-8.
#
# Coded by Jeffrey Massung as an example of the
# CHIP-8 assembler.
#
# Have fun!
#

import pyxel
import random

# ゲームの基本設定
SCREEN_WIDTH = 64   # CHIP-8の64ピクセルを1倍にスケール
SCREEN_HEIGHT = 32  # CHIP-8の32ピクセルを1倍にスケール
PIXEL_SCALE = 1     # CHIP-8の1ピクセルを1x1ピクセルに変換

class SnakeGame:
    def __init__(self):
        # Pyxelの初期化
        pyxel.init(SCREEN_WIDTH * PIXEL_SCALE, SCREEN_HEIGHT * PIXEL_SCALE, title="Neon Snake", fps=20)
        
        # 変数の初期化（CHIP-8のレジスタを模倣）
        self.head_x = 12    # v4: ヘッドのX座標
        self.head_y = 10    # v5: ヘッドのY座標
        self.score = 0      # v6: スコア
        self.direction = 4  # v7: 初期方向（右）
        self.head = 4       # va: ヘッドのメモリオフセット
        self.tail = 2       # vb: テールのメモリオフセット
        self.food_x = 0     # v8: 食料のX座標
        self.food_y = 0     # v9: 食料のY座標
        
        # 方向定数
        self.UP = 0
        self.RIGHT = 4
        self.DOWN = 8
        self.LEFT = 12
        
        # スネークのメモリ（CHIP-8のsnake_tailをリストで再現）
        # 初期値: [(0,0), (0,0), (10,10), (11,10), (12,10)]
        self.snake_tail = [(0, 0), (0, 0), (10, 10), (11, 10), (12, 10)]
        
        # サウンド設定（簡易ビープ音）
        pyxel.sound(0).set("c3e3g3", "t", "7", "v", 10)  # 食料取得時の音
        pyxel.sound(1).set("c2", "s", "4", "v", 30)      # ゲームオーバー時の音
        
        # ゲームの初期化
        self.draw_score()
        self.spawn_food()
        
        # Pyxelのゲームループ開始
        pyxel.run(self.update, self.draw)

    def update(self):
        # ゲームループ（CHIP-8のgame_loop）
        self.user_input()
        self.move()
        self.check_bounds()
        self.write_head()
        self.erase_tail()

    def user_input(self):
        # キー入力処理（CHIP-8のuser_input）
        if pyxel.btn(pyxel.KEY_UP):     # v0=5: 上
            self.direction = self.UP
        if pyxel.btn(pyxel.KEY_LEFT):   # v0=7: 左
            self.direction = self.LEFT
        if pyxel.btn(pyxel.KEY_DOWN):   # v0=8: 下
            self.direction = self.DOWN
        if pyxel.btn(pyxel.KEY_RIGHT):  # v0=9: 右
            self.direction = self.RIGHT

    def move(self):
        # 移動処理（CHIP-8のmove）
        if self.direction == self.UP:
            self.head_y -= 1
        elif self.direction == self.RIGHT:
            self.head_x += 1
        elif self.direction == self.DOWN:
            self.head_y += 1
        elif self.direction == self.LEFT:
            self.head_x -= 1

    def write_head(self):
        # ヘッドの書き込み（CHIP-8のwrite_head）
        self.head += 1
        if self.head >= len(self.snake_tail):
            self.snake_tail.append((0, 0))  # メモリ拡張
        self.snake_tail[self.head] = (self.head_x, self.head_y)
        
        # 衝突判定（食料との衝突）
        if self.head_x == self.food_x and self.head_y == self.food_y:
            pyxel.play(0, 0)  # ビープ音
            self.score += 1
            self.draw_score()
            # テールを伸ばす（CHIP-8のダミー位置追加を再現）
            self.tail -= 2
            if self.tail < 0:
                self.tail = 0
            self.spawn_food()
            
        # 自己衝突
        for x, y in self.snake_tail[self.tail:self.head]:
            if self.head_x == x and self.head_y == y:
                pyxel.play(1, 1)  # ゲームオーバー音
                pyxel.quit()      # ゲーム終了

    def erase_tail(self):
        # テールの消去（CHIP-8のerase_tail）
        self.tail += 1

    def check_bounds(self):
        # 境界チェック（CHIP-8のcheck_bounds）
        if self.head_x < 0 or self.head_x >= 64 or self.head_y < 0 or self.head_y >= 32:
            pyxel.play(1, 1)  # ゲームオーバー音
            pyxel.quit()      # ゲーム終了

    def spawn_food(self):
        # 食料の生成（CHIP-8のspawn_food）
        while True:
            self.food_x = random.randint(1, 62)
            self.food_y = random.randint(1, 30)
            if self.food_y > 7 or self.food_x < 54:  # スコア領域を避ける
                break

    # 画面の描画
    def draw(self):
        # 画面のクリア
        pyxel.cls(1)
        
        # 壁の描画
        for x in range(1, SCREEN_WIDTH-1):
            pyxel.circ( x * PIXEL_SCALE,                 1 * PIXEL_SCALE, PIXEL_SCALE, 3)
            pyxel.circ( x * PIXEL_SCALE, (SCREEN_HEIGHT-2) * PIXEL_SCALE, PIXEL_SCALE, 3)

        for y in range(1, SCREEN_HEIGHT-1):
            pyxel.circ(                1 * PIXEL_SCALE, y * PIXEL_SCALE,  PIXEL_SCALE, 3)
            pyxel.circ( (SCREEN_WIDTH-2) * PIXEL_SCALE, y * PIXEL_SCALE,  PIXEL_SCALE, 3)

        for x in range(1, SCREEN_WIDTH-1):
            pyxel.pset( x * PIXEL_SCALE,                 1 * PIXEL_SCALE, 11)
            pyxel.pset( x * PIXEL_SCALE, (SCREEN_HEIGHT-2) * PIXEL_SCALE, 11)

        for y in range(1, SCREEN_HEIGHT-1):
            pyxel.pset(                1 * PIXEL_SCALE, y * PIXEL_SCALE, 11)
            pyxel.pset( (SCREEN_WIDTH-2) * PIXEL_SCALE, y * PIXEL_SCALE, 11)

        # スネークの描画
        for x, y in self.snake_tail[self.tail:self.head + 1]:
            pyxel.circ(x * PIXEL_SCALE, y * PIXEL_SCALE, PIXEL_SCALE+1, 5)
        for x, y in self.snake_tail[self.tail:self.head + 1]:
            pyxel.circ(x * PIXEL_SCALE, y * PIXEL_SCALE, PIXEL_SCALE, 12)
        for x, y in self.snake_tail[self.tail:self.head + 1]:
            pyxel.pset(x * PIXEL_SCALE, y * PIXEL_SCALE, 6)
        
        # 食料の描画
        pyxel.circ(self.food_x * PIXEL_SCALE, self.food_y * PIXEL_SCALE, PIXEL_SCALE+1, 2)
        pyxel.circ(self.food_x * PIXEL_SCALE, self.food_y * PIXEL_SCALE, PIXEL_SCALE, 8)
        pyxel.pset(self.food_x * PIXEL_SCALE, self.food_y * PIXEL_SCALE, 14)
        
        # スコアの描画
        self.draw_score()

    def draw_score(self):
        # スコアの描画（CHIP-8のdraw_score）
        tens = self.score // 10
        ones = self.score % 10
        pyxel.text(54 * PIXEL_SCALE, 1 * PIXEL_SCALE, f"{tens}{ones}", 9)
        pyxel.text(55 * PIXEL_SCALE, 0 * PIXEL_SCALE, f"{tens}{ones}", 10)

# ゲームの実行
SnakeGame()

# End of snake.py
