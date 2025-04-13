import pyxel

# メモ: パレット(pyxel既定)

black = 0
dark_blue = 1
purple = 2
green = 3
brown = 4
blue = 5
light_purple = 6
white = 7
red = 8
amber = 9
yellow = 10
light_green = 11
light_blue = 12
gray = 13
pink = 14
beige = 15

player_atk = light_blue
enemy_atk = gray

player_die = pink
enemy_die = beige
needs_target = blue
status_effect_applied = light_purple
descend = light_purple

invalid = amber
impossible = yellow
error = purple

welcome_text = light_purple
health_recovered = green

bar_text = white
bar_filled = light_green
bar_empty = red

menu_title = yellow
menu_text = white

# メモ: 以下、色(color)とは直接関係ないコード(Pyxel関連)

# メモ: コンソールサイズ(80x50)
width = 80
height = 50

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

# テキストを中央に表示    
def textc(x: int, y: int, s: str, col: int):
    pyxel.text((x - len(s) // 2)*chr_x, y*chr_y, s, col)

# 背景色を指定してテキストを表示
def textbg(x: int, y: int, s: str, fg: int, bg: int):
    rect(x, y, len(s), 1, bg)
    text(x ,y, s, fg)

# 背景色を指定してテキストを中央に表示
def textcbg(x: int, y: int, s: str, fg: int, bg: int):
    rect(x - len(s) // 2, y, len(s), 1, bg)
    textc(x ,y, s, fg)
    
# end of color.py
