###########################################
# 
# Amabie(*1) for Pyxel/Python
#
# Move amabie left and right with LEFT/RIGHT
# Press DOWN to drop a ofuda(*2) and  
# release DOWN to rupture it. Defeat 
# incoming plagues they land in Japan.
#
# (*1) https://en.wikipedia.org/wiki/Amabie
# (*2) https://en.wikipedia.org/wiki/Ofuda
#
# Mar 10, 2021 ver.1 changed characters and titles
# Mar 11, 2021 ver.2 changed small
# Mar 15, 2021 ver.3 translated into English
# Mar 20, 2021 ver.4 changed characters and titles
# Mar 11, 2025 ver.5 converted to Pyxel/Python with Grok3
# Mar 12, 2025 ver.6 debug and refactor
# Mar 20, 2025 ver.7 colorize
#
###########################################

import pyxel
import random

# Pyxelの初期化
pyxel.init(64, 32, title="Amabie", fps=10)
pyxel.load("amabie.pyxres")

# ゲームの状態を管理するクラス
class Game:
    def __init__(self):
        self.state = "title"  # ゲームの状態（title, playing, game_over, sinking）
        self.reset()
        self.sink_y = 0       # 落下時のY座標
        self.sink_timer = 0   # 落下アニメーションのタイマー

    def reset(self):
        self.score = 0
        self.player_x = 32
        self.player_y = 1
        self.bomb_x = 0
        self.bomb_y = 0
        self.bomb_state = 0
        self.enemies = []
        self.enemy_timer = 0
        self.game_over = False
        self.sink_y = 8
        self.sink_timer = 0

    def draw_waves(self):
        for x in range(0, 64, 8):
            for y in range(8, 32, 8):
                pyxel.blt(x, y, 0, 32, 8, 8, 8)

        for x in range(0, 64, 8):
            pyxel.blt(x, 7, 0, 0, 0, 8, 2)

    def draw_score(self):
        pyxel.text(49, 1, f"{self.score:03d}", 14)

    def draw_title(self):
        pyxel.cls(1)
        self.draw_waves()
        pyxel.blt(16, 12, 0, 0, 8, 8, 7)  # AM
        pyxel.blt(24, 12, 0, 8, 8, 8, 7)  # MA
        pyxel.blt(32, 12, 0, 16, 8, 8, 7)  # AB
        pyxel.blt(40, 12, 0, 24, 8, 8, 7)  # IE

    def update_player(self):
        old_x = self.player_x
        if pyxel.btn(pyxel.KEY_LEFT):   # LEFTキーで左移動
            self.player_x -= 3
        if pyxel.btn(pyxel.KEY_RIGHT):  # RIGHTキーで右移動
            self.player_x += 3
        if self.player_x < 0:
            self.player_x = 0
        if self.player_x > 56:
            self.player_x = 56
        if pyxel.btn(pyxel.KEY_DOWN) and self.bomb_state == 0:  # DOWNキーでボム発射
            self.bomb_x = self.player_x
            self.bomb_y = 10
            self.bomb_state = 1

    def update_bomb(self):
        if self.bomb_state == 1:     # 落下中
            self.bomb_y += 1
            if self.bomb_y >= 25 or not pyxel.btn(pyxel.KEY_DOWN): 
                self.bomb_state = 2  # 爆発開始
        elif self.bomb_state >= 2:   # 爆発中
            self.bomb_state += 1
            if self.bomb_state >= 4:
                self.bomb_state = 0  # 爆発終了

    def spawn_enemy(self):
        x = random.randint(0, 63 - 8)
        self.enemies.append([x, 28])

    def update_enemies(self):
        self.enemy_timer += 1
        if self.enemy_timer > 40:
            self.spawn_enemy()
            self.enemy_timer = random.randint(10, 20)

        if self.enemy_timer % 2 == 0:
            for enemy in self.enemies[:]:
                enemy[1] -= 1
                if enemy[1] <= 8:
                    self.game_over = True
                    self.state = "sinking"  # 落下アニメーションへ移行
                if (self.bomb_state >= 2 and 
                    abs(enemy[0] - self.bomb_x) < 8 and 
                    abs(enemy[1] - self.bomb_y) < 8):
                    self.enemies.remove(enemy)
                    self.score += 1

    def update_sinking(self):
        self.sink_timer += 1
        if self.sink_timer % 1 == 0:  # 1フレームごとに落下
            self.sink_y += 1
        if self.sink_y >= 26:  # 落下完了
            self.state = "game_over"

    def draw(self):
        if self.state == "title":
            self.draw_title()
        elif self.state == "playing":
            pyxel.cls(1)
            self.draw_score()
            self.draw_waves()
            pyxel.blt(self.player_x, self.player_y, 0, 8, 0, 8, 5, 1)  # プレイヤー描画
            if self.bomb_state == 1:
                pyxel.blt(self.bomb_x, self.bomb_y, 0, 24, 0, 8, 6, 1)  # ボム描画
            elif self.bomb_state >= 2:
                pyxel.blt(self.bomb_x, self.bomb_y, 0, 48, 0, 8, 7, 1)  # 爆発描画
            for enemy in self.enemies:
                frame = enemy[1] % 2
                pyxel.blt(enemy[0], enemy[1], 0, 32 + frame * 8, 0, 8, 4, 1)  # 敵描画
        elif self.state == "sinking":
            pyxel.cls(1)
            pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 8, 5, 1)  # 墓描画
            self.draw_waves()
            pyxel.blt(self.player_x, self.sink_y, 0, 56, 0, 8, 6, 1)  # 落下中のアマビエ
        elif self.state == "game_over":
            pyxel.cls(1)
            self.draw_waves()
            pyxel.blt(self.player_x, self.sink_y, 0, 56, 0, 8, 6, 1)  # 落下後のアマビエ
            pyxel.text(20, 14, "THE END", 14)

    def update(self):
        if self.state == "title":
            if pyxel.btnp(pyxel.KEY_DOWN):  # DOWNキーでゲーム開始
                self.state = "playing"
                self.reset()
        elif self.state == "playing":
            self.update_player()
            self.update_bomb()
            self.update_enemies()
        elif self.state == "sinking":
            self.update_sinking()
        elif self.state == "game_over":
            if pyxel.btnp(pyxel.KEY_DOWN):  # DOWNキーでリスタート
                self.state = "title"
        if pyxel.btnp(pyxel.KEY_Q):  # Qキーで終了
            pyxel.quit()

# ゲームのインスタンスを作成して実行
game = Game()

def update():
    game.update()

def draw():
    game.draw()

pyxel.run(update, draw)

# End of amabie.py
