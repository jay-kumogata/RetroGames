import pyxel

white = 7
black = 0
red = 8

player_atk = 12
enemy_atk = 13

player_die = 14
enemy_die = 15
needs_target = 5
status_effect_applied = 6

invalid = 9
impossible = 10
error = 2

welcome_text = 6
health_recovered = 3

bar_text = white
bar_filled = 11
bar_empty = 8

# メモ: 以下、色(color)とは直接関係ないコード(Pyxel関連)

# メモ: 組込フォントのドット数(4x5)
chr_x = 4
chr_y = 5

# メモ: ヘルパー関数
def rect(x: int, y: int, w: int, h: int, col: int):
    pyxel.rect(x*chr_x, y*chr_y, w*chr_x, h*chr_y, col)

def rectb(x: int, y: int, w: int, h: int, col: int):
    pyxel.rectb(x*chr_x, y*chr_y, w*chr_x, h*chr_y, col)
    
def text(x: int, y: int, s: str, col: int):
    pyxel.text(x*chr_x, y*chr_y, s, col)

# end of color.py
