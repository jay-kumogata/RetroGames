# ****************************************************************************
# ***               Vertical Brix v1.0 (C) Paul Robson 1996                ***
# ****************************************************************************
# ****************************************************************************
#
# May 20, 2025 ver.1 converted to Pyxel/Python with Grok3 
# May 29, 2025 ver.2 debug and refactor
# May 30, 2025 ver.3 debug
#
# ****************************************************************************

import pyxel
import random

# Constants  (scaled from Chip8's 64x32 to Pyxel's 64x32)
TOP_LINE = 0
BOTTOM_LINE = 31  # 31 * 1
LEFT_SIDE = 0
RIGHT_SIDE = 63  # 63 * 1
BRICK_X = 34      # 34 * 1
BRICK_X_COUNT = 7
BRICK_Y_COUNT = 10
BAT_X = 2         # 2 * 1
KEY_UP = pyxel.KEY_UP
KEY_DOWN = pyxel.KEY_DOWN
KEY_START = pyxel.KEY_SPACE

# Game state
lives = 5
score = 0
bat_y = 16  # 16 * 1
ball_x = 0
ball_y = 0
ball_dx = 1
ball_dy = 1
bricks_remaining = BRICK_X_COUNT * BRICK_Y_COUNT

class Vbrix:
    def __init__(self):
        pyxel.init(64, 32, title="Vertical Brix", fps=30)
        pyxel.sounds[0].set("c3", "s", "7", "n", 10)  # Ball bounce
        pyxel.sounds[1].set("e3", "t", "7", "n", 5)   # Brick hit
        # Initialize brick state array
        self.bricks = [[True for _ in range(BRICK_X_COUNT)] for _ in range(BRICK_Y_COUNT)]
        self.game_state = "title"
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_state == "title":
            if pyxel.btnp(KEY_START):
                self.game_state = "game"
                self.init_game()
        elif self.game_state == "game":
            self.move_bat()
            self.move_ball()
            self.check_collision()
            if ball_x <= 0:  # Ball lost
                global lives
                lives -= 1
                if lives > 0:
                    self.init_ball()
                else:
                    self.game_state = "game_over"
                    pyxel.frame_count = 0
        elif self.game_state == "game_over":
            if pyxel.frame_count > 120 and pyxel.btnp(KEY_START):
                self.game_state = "game"
                self.init_game()

    def init_game(self):
        global lives, score, bricks_remaining
        lives = 5
        score = 0
        bricks_remaining = BRICK_X_COUNT * BRICK_Y_COUNT
        # Reset brick state
        self.bricks = [[True for _ in range(BRICK_X_COUNT)] for _ in range(BRICK_Y_COUNT)]
        self.init_bat()
        self.init_ball()

    def init_bat(self):
        global bat_y
        bat_y = 16  # 16 * 1

    def init_ball(self):
        global ball_x, ball_y, ball_dx, ball_dy
        ball_y = random.randint(1, 30)  # Random y in [1, 30] * 1
        ball_x = 4  # 4 * 1
        ball_dx = 1
        ball_dy = 1

    def move_bat(self):
        global bat_y
        if pyxel.btn(KEY_UP) and bat_y > TOP_LINE:
            bat_y -= 1
        if pyxel.btn(KEY_DOWN) and bat_y < BOTTOM_LINE - 4:
            bat_y += 1

    def move_ball(self):
        global ball_x, ball_y, ball_dx, ball_dy
        ball_x += ball_dx
        ball_y += ball_dy
        # Bounce off walls
        if ball_y <= 1:  # TOP_LINE + 1
            ball_y = 1
            ball_dy = 1
            pyxel.play(0, 0)
        if ball_y >= BOTTOM_LINE - 1:  # BOTTOM_LINE - 1
            ball_y = BOTTOM_LINE - 1
            ball_dy = -1
            pyxel.play(0, 0)
        if ball_x >= RIGHT_SIDE - 1:  # RIGHT_SIDE - 1
            ball_x = RIGHT_SIDE - 1
            ball_dx = -1
            pyxel.play(0, 0)

    def check_collision(self):
        global ball_x, ball_y, ball_dx, ball_dy, score, bricks_remaining
        # Bat collision
        if ball_x == BAT_X and bat_y <= ball_y < bat_y + 5:
            offset = ball_y - bat_y
            ball_dx = 1
            ball_dy = [-2, -1, 0, 1, 2][offset // 1]  # Direction table
            pyxel.play(0, 0)
        # Brick collision
        if ball_x >= BRICK_X - 1:
            bx = (ball_x - BRICK_X) // 3  # Brick x (logical)
            by = (ball_y - 1) // 3        # Brick y (logical)
            if 0 <= bx < BRICK_X_COUNT and 0 <= by < BRICK_Y_COUNT and self.bricks[by][bx]:
                # Brick exists; mark it as destroyed
                self.bricks[by][bx] = False
                score += 1
                bricks_remaining -= 1
                ball_dx = -ball_dx
                pyxel.play(0, 1)
                if bricks_remaining == 0:
                    # Reset bricks when all are cleared
                    self.bricks = [[True for _ in range(BRICK_X_COUNT)] for _ in range(BRICK_Y_COUNT)]
                    bricks_remaining = BRICK_X_COUNT * BRICK_Y_COUNT

    def draw(self):
        if self.game_state == "title":
            pyxel.cls(1)
            pyxel.text(6, 12, "Vertical Brix", 7)
        else:
            pyxel.cls(1)
            # Draw border
            for x in range(LEFT_SIDE, RIGHT_SIDE, 1):
                pyxel.rect(x, TOP_LINE, 1, 1, 13)
                pyxel.rect(x, BOTTOM_LINE, 1, 1, 13)
            for y in range(TOP_LINE, BOTTOM_LINE + 1, 1):
                pyxel.rect(RIGHT_SIDE, y, 1, 1, 13)
            # Draw bat
            pyxel.rect(BAT_X, bat_y, 1, 5, 13)
            pyxel.rect(BAT_X, bat_y, 1, 1, 8)
            pyxel.rect(BAT_X, bat_y + 4, 1, 1, 8)
            # Draw ball
            pyxel.rect(ball_x, ball_y, 1, 1, 8)
            # Draw bricks
            self.draw_bricks()
            # Draw score
            pyxel.text(5, 2, f"{score:03d}", 7)
            # Draw lives
            pyxel.text(20, 2, str(lives), 7)

    def draw_bricks(self):
        rainbow = [2, 5, 12, 3, 10, 9, 8]
        for y in range(BRICK_Y_COUNT):
            for x in range(BRICK_X_COUNT):
                if self.bricks[y][x]:  # Only draw if brick exists
                    pyxel.rect(BRICK_X + x * 3, 1 + y * 3, 3, 3, rainbow[x])
                    #pyxel.rect(BRICK_X + x * 3 + 1, 1 + y * 3 + 1, 1, 1, 0) 

Vbrix()

# End of vbrix.py
