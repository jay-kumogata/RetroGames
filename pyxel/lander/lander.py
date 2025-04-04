# Lunar lander clone for the CHIP-8
#
# Coded by Jeffrey Massung as an example of the
# CHIP-8 assembler.
#
# Have fun!
#---------------------------------------------------------------------------
# Note: this source has been ported to Octo by Jay Kumogata on 05 Dec 2021.
#       (only the notation changed: it has been converted manually.)
#       And has been converted to Pyxel/Python with Grok3(beta) on 12 Mar 2025.

import pyxel
import random as rnd

class LunarLander:
    def __init__(self):
        pyxel.init(128, 64, title="Lunar Lander")
        pyxel.sounds[0].set("c3", "s", "7", "f", 5)   # 推力音
        pyxel.sounds[1].set("e2", "n", "5", "f", 20)  # 爆発音

        # 乱択パレット
        #self.pal = [1,6,8,7,9,10,5,3]
        self.pal = [1,rnd.randint(6,7),rnd.randint(10,11),rnd.randint(14,15),\
                    rnd.randint(8,9),rnd.randint(12,13),rnd.randint(4,5),\
                    rnd.randint(2,3)]
         
        
        # 変数初期化
        self.x = 64
        self.y = 0
        self.vx = 0
        self.vy = 8
        self.thrust = 0x80
        self.tilt = 0x80
        self.fuel = 64
        self.fuel_use = 0
        self.level = 0
        self.score = 0
        self.plat_x = 0
        self.elevation = [0] * 16
        self.gravity_timer = 10
        self.thrust_visible = False
        self.game_over = False
        self.landed = False
        self.explosion_frame = -1

        self.init_level()
        pyxel.run(self.update, self.draw)

    def init_level(self):
        self.level += 1
        self.x = rnd.randint(32, 96)
        self.y = 0
        self.vx = rnd.randint(-15, 15)
        self.vy = 8
        self.thrust = 0x80
        self.tilt = 0x80
        self.fuel = 64
        self.fuel_use = 0
        self.thrust_visible = False
        self.landed = False
        self.explosion_frame = -1
        self.init_ground()
        self.init_platform()

    def init_ground(self):
        elev = rnd.randint(20, 40)
        self.elevation = [elev] * 15
        for i in range(3):
            delta = rnd.randint(-8, 8)
            for j in range(5):
                idx = i * 5 + j
                if idx < 15:
                    self.elevation[idx] = max(10, min(50, elev + delta))
                    elev = self.elevation[idx]

    def init_platform(self):
        lowest = min(self.elevation)
        candidates = [i for i, e in enumerate(self.elevation) if e == lowest]
        self.plat_x = rnd.choice(candidates) * 8

    def update(self):
        if self.game_over:
            if self.explosion_frame < 4:
                self.explosion_frame += 1
            elif pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        if pyxel.btn(pyxel.KEY_UP) and self.fuel > 0:
            self.vy -= 2
            self.fuel_use -= 0xC0
            self.thrust_visible = True
            pyxel.play(0, 0)
        if pyxel.btn(pyxel.KEY_LEFT) and self.fuel > 0:
            if self.vx > -60:
                self.vx -= 2
            self.fuel_use -= 0x60
        if pyxel.btn(pyxel.KEY_RIGHT) and self.fuel > 0:
            if self.vx < 60:
                self.vx += 2
            self.fuel_use -= 0x60

        if self.fuel_use < 0:
            self.fuel -= 1
            self.fuel_use = 0
            if self.fuel < 0:
                self.fuel = 0

        self.gravity_timer -= 1
        if self.gravity_timer <= 0:
            self.vy += 1
            self.gravity_timer = 10
            self.thrust_visible = False

        self.thrust += self.vy
        self.tilt += self.vx

        if self.thrust >= 0xC0:
            self.y += 1
            self.thrust = 0x80
        elif self.thrust <= 0x40:
            self.y -= 1
            self.thrust = 0x80

        if self.tilt <= 0x40:
            self.x -= 1
            self.tilt = 0x80
        elif self.tilt >= 0xC0:
            self.x += 1
            self.tilt = 0x80

        self.x = max(0, min(127, self.x))

        ground_y = self.elevation[self.x // 8]
        if self.y + 5 >= 64 - ground_y:
            self.y = 64 - ground_y - 5
            if (self.plat_x <= self.x <= self.plat_x + 8 and 
                self.vy < 24 and abs(self.vx) < 16):
                self.score += 25 + self.fuel * 2
                self.landed = True
                self.init_level()
            else:
                self.game_over = True
                self.explosion_frame = 0
                pyxel.play(1, 1)

    def draw(self):
        pyxel.cls(self.pal[0])

        # 格子状の地形描画
        for i, elev in enumerate(self.elevation):
            if elev % 2 == 1: elev -= 1
            for y in range(64 - elev, 64, 2):
                for x in range(i * 8, i * 8 + 8, 2):
                    pyxel.pset(x, y, self.pal[1])

        # プラットフォーム描画
        pyxel.rect(self.plat_x, 64 - self.elevation[self.plat_x // 8], 8, 1, self.pal[2])

        # 着陸船描画
        if not self.game_over or self.explosion_frame == -1:
            for y, row in enumerate([0b01110000, 0b11111000, 0b11111000, 0b01010000, 0b11011000]):
                for x in range(8):
                    if row & (1 << (7 - x)):
                        pyxel.pset(self.x + x, self.y + y, self.pal[3])
            if self.thrust_visible and self.fuel > 0:
                for y, row in enumerate([0b01010000, 0b00100000, 0b00100000]):
                    for x in range(8):
                        if row & (1 << (7 - x)):
                            pyxel.pset(self.x + x, self.y + 5 + y, self.pal[4])

        # 爆発アニメーション
        if self.explosion_frame >= 0:
            explosion_data = [
                [0b00000, 0b00100, 0b01010, 0b00100, 0b00000],
                [0b00000, 0b01010, 0b00100, 0b01010, 0b00000],
                [0b00000, 0b01010, 0b10001, 0b01010, 0b00000],
                [0b01010, 0b10001, 0b00000, 0b10001, 0b01010],
                [0b10101, 0b00000, 0b10001, 0b00000, 0b10101]
            ]
            for y, row in enumerate(explosion_data[self.explosion_frame]):
                for x in range(5):
                    if row & (1 << (4 - x)):
                        pyxel.pset(self.x + x + 1, self.y + y, self.pal[5])
                    
        # 燃料ゲージ
        pyxel.rect(120, 0, 8, 64, self.pal[6])  # 枠
        pyxel.rect(121, 64 - self.fuel, 6, self.fuel, self.pal[7])  # 燃料バー
        self.draw_vertical_text(122, 2, "FUEL", self.pal[3])  # 「FUEL」を縦書き

        # スコアとレベル
        pyxel.text(2, 2, f"LEVEL {self.level}", self.pal[3])
        pyxel.text(2, 10, f"SCORE {self.score}", self.pal[3])

        if self.game_over and self.explosion_frame >= 4:
            pyxel.text(40,25,"GAME OVER", self.pal[2])

    # 縦書きテキスト描画（「FUEL」用）
    def draw_vertical_text(self, x, y, text, col):
        for i, char in enumerate(text.upper()):
            pyxel.text(x, y+i*6, char, col)

# ゲーム開始
LunarLander()

# End of lander.py
