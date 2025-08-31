import pyxel

SCREEN = 30  # Scaled down from 80
R_WIDTH = 260  # Scaled down from 780
R_DEPTH = 10

class MyLine:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._w = 0
        self._c = 0
        self._b = 0

    def project(self, x, y, z):
        if z <= 0:
            return
        s = SCREEN / z
        self._x = x * s + pyxel.width / 2
        self._y = y * s + pyxel.height / 2
        self._w = R_WIDTH * s

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def w(self):
        return self._w

    @property
    def curve(self):
        return self._c

    @curve.setter
    def curve(self, n):
        self._c = n

    @property
    def bank(self):
        return self._b

    @bank.setter
    def bank(self, n):
        self._b = n

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Simple OutRun", fps=60)
        self.lines = []
        self.eyeX = 0
        self.eyeY = 200  # Scaled down from 400
        self.eyeZ = 0

        for i in range(100):
            line = MyLine()
            if 20 < i < 40:
                line.curve = 0.8
                line.bank = 0.8
            if 40 < i < 60:
                line.curve = -0.5
                line.bank = -0.2
            line.project(self.eyeX, self.eyeY, R_DEPTH * i - self.eyeZ)
            self.lines.append(line)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.eyeZ += 2

    def draw(self):
        pyxel.cls(0)  # Black background

        oX = 0
        dX = 0
        oY = 0
        dY = 0

        start = int(self.eyeZ // R_DEPTH) + 1
        for i in range(start, start + 40):
            iA = i % len(self.lines)
            iB = iA - 1 if iA > 0 else len(self.lines) - 1
            lA = self.lines[iA]
            lB = self.lines[iB]

            oX += dX
            dX += lA.curve
            oY += dY
            dY += lA.bank

            lA.project(self.eyeX - oX, self.eyeY - oY, R_DEPTH * i - self.eyeZ)

            if lB.y < lA.y:
                continue

            cGrass = 11 if i % 2 == 0 else 3  # Green / Dark green
            cSide = 5 if i % 2 == 0 else 7   # Dark gray / White
            cRoad = 6 if i % 2 == 0 else 7   # Light gray / White (approximate)

            # Grass (wide to cover screen)
            self.draw_shape(lA.x, lA.y, pyxel.width * 4, lB.x, lB.y, pyxel.width * 4, cGrass)
            # Side
            self.draw_shape(lA.x, lA.y, lA.w * 1.2, lB.x, lB.y, lB.w * 1.2, cSide)
            # Road
            self.draw_shape(lA.x, lA.y, lA.w, lB.x, lB.y, lB.w, cRoad)

    def draw_shape(self, x1, y1, w1, x2, y2, w2, c):
        # Simple scanline fill for trapezoid
        if y1 == y2:
            return  # Skip flat

        min_y = min(y1, y2)
        max_y = max(y1, y2)
        dy = y2 - y1

        for yy in range(max(0, int(min_y)), min(pyxel.height, int(max_y) + 1)):
            t = (yy - y1) / dy if dy != 0 else 0
            left_x = (x1 - w1 / 2) + t * ((x2 - w2 / 2) - (x1 - w1 / 2))
            right_x = (x1 + w1 / 2) + t * ((x2 + w2 / 2) - (x1 + w1 / 2))

            # Clip to screen
            left_x = max(0, min(pyxel.width - 1, left_x))
            right_x = max(0, min(pyxel.width - 1, right_x))

            if left_x < right_x:
                pyxel.line(int(left_x), yy, int(right_x), yy, c)

App()
