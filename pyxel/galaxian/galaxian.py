# ランダムな大きさの３種類の敵が回転しながら落ちてくるプログラム

import pyxel

# 敵を表現するクラス
class Enemy:
    def __init__(self, x, y, size, type, rotate_speed, fall_speed, scale):
        self.x = x
        self.y = y
        self.size = size
        self.type  = type
        self.rotate_speed = rotate_speed
        self.fall_speed = fall_speed   
        self.scale  = scale
        self.rotate = 0      
        
    # 敵を動かす
    def update(self):
        self.rotate += self.rotate_speed
        self.y += self.fall_speed
        if self.y > 256:            # 画面外に出たら上に戻る        
            self.x = pyxel.rndi(-self.size//8, 256//8) * 8
            #self.y = pyxel.rndi(-256//8, 0) * 8
            self.y = -self.size

    # 敵を描画
    def draw(self):
        pyxel.blt(
            self.x, self.y,
            # 対応するイメージバンクの番号、x座標、y座標、横サイズ、縦サイズ、透明色
            0, self.type * (self.size+4), 0, self.size, self.size, 0,
            # 回転角度(ラジアンでなく度:Degree)、拡大率(1より小さいときは縮小)
            self.rotate, self.scale)

class App:
    def __init__(self):
        pyxel.init(256, 256, title="Galaxian", capture_scale=1)
        self.enemy_size = 12

        # イメージバンク0の座標 (0, 0)に画像ファイルを読み込む
        pyxel.load("galaxian.pyxres")
        
        # 複数の敵を初期化
        self.enemyflakes = [
            Enemy(
                x = pyxel.rndi(-self.enemy_size//4, 256//4) * 4,
                y = pyxel.rndi(-256//8, 0) * 8,
                size = self.enemy_size,
                type  = pyxel.rndi(0, 2),   # 3種類ある敵のどれか
                fall_speed = pyxel.rndf(0.6, 1.0),
                rotate_speed = pyxel.rndf(-3, 3),
                scale  = pyxel.rndf(1.5, 2.4)   # 画像の表示倍率
            )
            for _ in range(24)
        ]
        
        pyxel.run(self.update, self.draw)

    def update(self):
        # 全ての敵を更新
        for flake in self.enemyflakes:
            flake.update()

    def draw(self):
        pyxel.cls(1)
        # 全ての敵を描画
        for flake in self.enemyflakes:
            flake.draw()

App()
