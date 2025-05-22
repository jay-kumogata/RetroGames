#
# Basic Frogger for Pyxel/Python
# cf. https://gist.github.com/straker/82a4368849cbd441b05bd6a044f2b2d3
#
# May 21, 2025 ver.1 converted to Pyxel/Python with Grok3
# May 22, 2025 ver.2 debug and refactor
# 
import pyxel

class Frogger:
    def __init__(self):
        # キャンバスサイズ
        pyxel.init(208, 240, title="Frogger")
        self.grid = 16  # グリッドサイズ
        self.grid_gap = 3  # グリッド間の隙間

        # Froggerの初期化
        self.frogger = {
            "x": self.grid * 6,
            "y": self.grid * 13,
            "color": 11,  # 黄緑（11）
            "size": self.grid,
            "shape": "circle",
            "speed": 0
        }
        self.scored_froggers = []

        # パターンの移植
        self.patterns = [
            None,  # ゴールバンク
            # 丸太
            {
                "spacing": [2],
                "color": 4,  # 赤茶色（4）
                "size": self.grid * 4,
                "shape": "rect",
                "speed": 0.75
            },
            # カメ
            {
                "spacing": [0, 2, 0, 2, 0, 2, 0, 4],
                "color": 8,  # 赤（8）
                "size": self.grid,
                "shape": "circle",
                "speed": -1
            },
            # 長い丸太
            {
                "spacing": [2],
                "color": 4,  # 赤茶色（4）
                "size": self.grid * 7,
                "shape": "rect",
                "speed": 1.5
            },
            # 丸太
            {
                "spacing": [3],
                "color": 4,  # 赤茶色（4）
                "size": self.grid * 3,
                "shape": "rect",
                "speed": 0.5
            },
            # カメ
            {
                "spacing": [0, 0, 1],
                "color": 8,  # 赤（8）
                "size": self.grid,
                "shape": "circle",
                "speed": -1
            },
            None,  # ビーチ
            # トラック
            {
                "spacing": [3, 8],
                "color": 13,  # 薄いグレー（13)
                "size": self.grid * 2,
                "shape": "rect",
                "speed": -1
            },
            # 速い車
            {
                "spacing": [14],
                "color": 12,  # 薄い青（12)
                "size": self.grid,
                "shape": "rect",
                "speed": 0.75
            },
            # 車
            {
                "spacing": [3, 3, 7],
                "color": 2,  # 紫（2）
                "size": self.grid,
                "shape": "rect",
                "speed": -0.75
            },
            # ブルドーザー
            {
                "spacing": [3, 3, 7],
                "color": 3,  # 緑（3）
                "size": self.grid,
                "shape": "rect",
                "speed": 0.5
            },
            # 車
            {
                "spacing": [4],
                "color": 10,  # 黄色（10）
                "size": self.grid,
                "shape": "rect",
                "speed": -0.5
            },
            None  # スタートゾーン（安全）
        ]

        # スプライトの初期化
        self.rows = []
        self.init_rows()

        # ゲーム開始
        pyxel.run(self.update, self.draw)

    def init_rows(self):
        # 各行のスプライトを初期化
        for i in range(len(self.patterns)):
            self.rows.append([])
            if not self.patterns[i]:
                continue
            x, index = 0, 0
            pattern = self.patterns[i]
            # パターンの合計幅を計算
            total_pattern_width = sum(pattern["spacing"]) * self.grid \
                                + len(pattern["spacing"]) * pattern["size"]
            end_x = pyxel.width + total_pattern_width  # 画面外まで含める
            while x < end_x:
                self.rows[i].append({
                    "x": x,
                    "y": self.grid * (i + 1),
                    "index": index,
                    **pattern
                })
                x += pattern["size"] + pattern["spacing"][index] * self.grid
                index = (index + 1) % len(pattern["spacing"])

    def update(self):
        # キー入力処理
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.frogger["x"] -= self.grid
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.frogger["x"] += self.grid
        elif pyxel.btnp(pyxel.KEY_UP):
            self.frogger["y"] -= self.grid
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.frogger["y"] += self.grid

        # Froggerの位置を画面内に制限
        self.frogger["x"] = max(0, min(self.frogger["x"], pyxel.width - self.grid))
        self.frogger["y"] = max(self.grid, min(self.frogger["y"],
                                               pyxel.height - self.grid * 2))

        # Froggerの移動（障害物に乗っている場合）
        self.frogger["x"] += self.frogger["speed"]

        # スプライトの更新
        for r in range(len(self.rows)):
            for sprite in self.rows[r]:
                sprite["x"] += sprite["speed"]
                # 左方向に移動し，画面外に出た場合
                if sprite["speed"] < 0 and sprite["x"] < -sprite["size"]:
                    rightmost = max(self.rows[r], key=lambda s: s["x"])
                    spacing = self.patterns[r]["spacing"]
                    sprite["x"] = rightmost["x"] + rightmost["size"] \
                                + spacing[rightmost["index"]] * self.grid
                    sprite["index"] = (rightmost["index"] + 1) % len(spacing)
                # 右方向に移動し，画面外に出た場合
                elif sprite["speed"] > 0 and sprite["x"] > pyxel.width:
                    leftmost = min(self.rows[r], key=lambda s: s["x"])
                    spacing = self.patterns[r]["spacing"]
                    index = leftmost["index"] - 1
                    index = index if index >= 0 else len(spacing) - 1
                    sprite["x"] = leftmost["x"] - spacing[index] * self.grid \
                                - sprite["size"]
                    sprite["index"] = index

        # 衝突判定
        frogger_row = int(self.frogger["y"] / self.grid - 1)
        collision = False
        for sprite in self.rows[frogger_row]:
            if (self.frogger["x"] < sprite["x"] + sprite["size"] - self.grid_gap and
                self.frogger["x"] + self.grid - self.grid_gap > sprite["x"] and
                self.frogger["y"] < sprite["y"] + self.grid and
                self.frogger["y"] + self.grid > sprite["y"]):
                collision = True
                if frogger_row > len(self.rows) / 2:  # 道路エリア（車やトラック）
                    self.frogger["x"] = self.grid * 6
                    self.frogger["y"] = self.grid * 13
                    self.frogger["speed"] = 0
                else:  # 川エリア（丸太やカメ）
                    self.frogger["speed"] = sprite["speed"]

        if not collision:
            self.frogger["speed"] = 0
            # 川エリアで障害物に乗っていない場合，リセット
            if 1 <= frogger_row < len(self.rows) / 2 - 1:
                self.frogger["x"] = self.grid * 6
                self.frogger["y"] = self.grid * 13
            # ゴール処理
            elif frogger_row == 0:
                col = int((self.frogger["x"] + self.grid / 2) / self.grid)
                if col % 3 == 0 and not any(frog["x"] == col * self.grid \
                                            for frog in self.scored_froggers):
                    self.scored_froggers.append({
                        **self.frogger,
                        "x": col * self.grid,
                        "y": self.frogger["y"] + 1
                    })
                    self.frogger["x"] = self.grid * 6
                    self.frogger["y"] = self.grid * 13

    def draw(self):
        pyxel.cls(0)  # 画面クリア（黒）

        # 背景描画
        # 水
        pyxel.rect(0, self.grid, pyxel.width, self.grid * 6, 1)  # 青（1）
        # ゴールバンク
        pyxel.rect(0, self.grid, pyxel.width, 2, 3)  # 緑（3）
        pyxel.rect(0, self.grid, 1, self.grid, 3)
        pyxel.rect(pyxel.width - 1, self.grid, 1, self.grid, 3)
        for i in range(4):
            pyxel.rect(self.grid + self.grid * 3 * i, self.grid,
                       self.grid * 2, self.grid, 3)
        # ビーチ
        pyxel.rect(0, 7 * self.grid, pyxel.width, self.grid, 2)  # 紫（2）
        # スタートゾーン
        pyxel.rect(0, pyxel.height - self.grid * 2,
                   pyxel.width, self.grid, 2)  # 紫（2）

        # スプライト描画
        for r in range(len(self.rows)):
            for sprite in self.rows[r]:
                if sprite["shape"] == "rect":
                    pyxel.rect(sprite["x"], sprite["y"] + self.grid_gap / 2,
                               sprite["size"], self.grid - self.grid_gap,
                               sprite["color"])
                else:
                    pyxel.circ(sprite["x"] + sprite["size"] / 2,
                               sprite["y"] + sprite["size"] / 2,
                               sprite["size"] / 2 - self.grid_gap / 2,
                               sprite["color"])

        # Froggerの描画
        pyxel.circ(self.frogger["x"] + self.frogger["size"] / 2,
                   self.frogger["y"] + self.frogger["size"] / 2,
                   self.frogger["size"] / 2 - self.grid_gap / 2,
                   self.frogger["color"])

        # ゴールしたFroggerの描画
        for frog in self.scored_froggers:
            pyxel.circ(frog["x"] + frog["size"] / 2, frog["y"] + frog["size"] / 2,
                       frog["size"] / 2 - self.grid_gap / 2, frog["color"])

Frogger()

# End of frogger.py
