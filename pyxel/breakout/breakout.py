#########################################################
#
# Breakout (Brix hack) [David Winter, 1997]
# digitally remastered by Jay Kumogata.
#
# Dec. 20, 2021 (ver.1) decompiled from binary file[1]
# Jan. 22, 2022 (ver.2) renamed labels and subroutines
# Mar. 08, 2025 (ver.3) converted to Pyxel/Python with Grok3
# Mar. 09, 2025 (ver.4) debug and refactor
#
# [1] Breakout (Brix hack) [David Winter, 1997].ch
#
##########################################################

# Registers
# --------- 
# v0-v4	are scratch registers
# v5	Score
# v6	X coord. of ball
# v7	Y coord. of ball
# v8	X direction of ball motion
# v9	Y direction of ball motion
# vC	X coord. of paddle
# vD	Y coord. of paddle
# vE	Number of balls
# vF	collision detection

import pyxel
import random

# Pyxelの初期化
pyxel.init(64, 32, title="Breakout (Brix hack)", fps=20)  # CHIP-8の画面サイズに合わせる

# レジスタ（CHIP-8のV0-VFに相当）
V = [0] * 16
V[0xE] = 5  # ボールの数 (vE)
V[5] = 0    # スコア (v5)

# スプライトデータ（CHIP-8のデータに基づくピクセル表現）
SPRITES = {
    "block": [0xF0, 0x00],  # 4x1ピクセル
    "ball": [0x80, 0x00],   # 1x1ピクセル
    "paddle": [0xFC, 0x00], # 6x1ピクセル
    "balls": [0xAA, 0x00]   # ボール数表示用
}

# 画面バッファ（64x32）
display = [[0 for _ in range(64)] for _ in range(32)]

def draw_sprite(x, y, sprite):
    """スプライトを描画し、衝突検出を行う"""
    collision = False
    for i, byte in enumerate(sprite):
        for bit in range(8):
            if byte & (0x80 >> bit):
                px = (x + bit) & 0x3F  # 画面端で折り返し
                py = (y + i) & 0x1F
                if 0 <= py < 32 and 0 <= px < 64:  # 画面範囲内か確認
                    if display[py][px] == 1:
                        collision = True
                        display[py][px] = 0
                    else:
                        display[py][px] = 1
    return collision

def clear_screen():
    """画面をクリア"""
    for y in range(32):
        for x in range(64):
            display[y][x] = 0

def draw_score():
    """スコアを描画"""
    pyxel.text(50, 0, f"{V[5]:02d}", 7)  # 白でスコア表示

def update():
    """ゲームの更新処理"""
    global V

    # パドルの描画（前の位置を消してから）
    draw_sprite(V[0xC], V[0xD], SPRITES["paddle"])  # 消す

    # キー入力（AとDキー）
    if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
        V[0xC] = max(0, V[0xC] - 2)
    if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
        V[0xC] = min(0x3F - 6, V[0xC] + 2)  # パドルの幅を考慮

    # パドルの描画（前の位置を消してから）
    draw_sprite(V[0xC], V[0xD], SPRITES["paddle"])  # 描く

    # ボールの移動と衝突
    if "ball_active" not in globals() or not ball_active:
        V[6] = random.randint(0, 15)  # ボールのX座標 (v6)
        V[7] = 0x1E                   # ボールのY座標 (v7)
        V[8] = 1                      # X方向 (v8)
        V[9] = -1                     # Y方向 (v9)
        globals()["ball_active"] = True
        draw_sprite(V[6], V[7], SPRITES["ball"])  # 描く

    # ボールの移動と描画
    draw_sprite(V[6], V[7], SPRITES["ball"])  # 消す
    V[6] = (V[6] + V[8]) & 0x3F  # X移動
    V[7] = (V[7] + V[9]) & 0x1F  # Y移動
    V[0xF] = draw_sprite(V[6], V[7], SPRITES["ball"])  # 描く

    # 壁との衝突
    if V[6] == 0:
        V[8] = 1
    elif V[6] == 0x3F:
        V[8] = -1
    if V[7] == 0:
        V[9] = 1

    # パドルとの衝突
    if V[7] == 0x1F:
        if V[6] >= V[0xC] and V[6] <= V[0xC] + 6:
            V[9] = -1
            diff = V[6] - V[0xC]
            if diff < 2:
                V[8] = -1  # 左側
            elif diff > 4:
                V[8] = 1   # 右側
            else:
                V[8] = 0   # 中央
            pyxel.play(0, 0)  # ヒット音
        else:
            V[0xE] -= 1  # ミス
            globals()["ball_active"] = False
            pyxel.play(0, 1)  # ミス音
            draw_sprite(V[6], V[7], SPRITES["ball"])  # ボールを消す
            draw_sprite((V[0xE]-1)*2, 0, SPRITES["ball"])  # ボール数を減らす

    # ブロックとの衝突
    if V[7] < 0x12 and V[0xF]:
        V[5] += 1  # スコア加算
        V[9] = -V[9]  # Y方向反転
        block_x = (V[6] & 0xFC)  # ブロックの位置を調整
        draw_sprite(block_x, V[7], SPRITES["block"])  # ブロック消去
        pyxel.play(0, 0)  # ブロック破壊音

    # ゲーム終了判定
    if V[5] >= 0x60:
        print("Game Clear!")
        pyxel.quit()
    if V[0xE] <= 0:
        print("Game Over!")
        pyxel.quit()

def draw():
    """画面の描画処理"""
    pyxel.cls(0)  # 黒でクリア
    for y in range(32):
        for x in range(64):
            if display[y][x]:
                pyxel.pset(x, y, 7)  # 白でピクセル描画
    draw_score()

def main():
    # 初期化
    clear_screen()

    # ブロックの描画
    V[0xB] = 0x06  # Y座標
    while V[0xB] != 0x12:
        V[0xA] = 0x00  # X座標
        while V[0xA] != 0x40:
            draw_sprite(V[0xA], V[0xB], SPRITES["block"])
            V[0xA] += 0x04
        V[0xB] += 0x02

    # パドルの初期位置
    V[0xC] = 0x20  # X座標
    V[0xD] = 0x1F  # Y座標
    draw_sprite(V[0xC], V[0xD], SPRITES["paddle"])

    # ボール数の表示（簡略化）
    draw_sprite(0, 0, SPRITES["balls"])

    # サウンド設定（簡易的なビープ音）
    pyxel.sounds[0].set("c3", "t", "7", "n", 5)  # ヒット音
    pyxel.sounds[1].set("c2", "s", "7", "n", 10) # ミス音

    # Pyxelゲームループ開始
    pyxel.run(update, draw)

if __name__ == "__main__":
    main()

# End of breakout.py    
