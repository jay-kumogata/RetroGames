class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 加算
    def add(self, v):
        return Vec(self.x + v.x, self.y + v.y)

    # 掛算
    def mul(self, *args):
        if len(args) == 1: x = args[0]; y = args[0]
        if len(args) == 2: x = args[0]; y = args[1]
        return Vec(self.x * x, self.y * y)

    # 内積
    def dot(self, v):
        return self.x * v.x + self.y * v.y

    # 外積
    def cross(self, v):
        return self.x * v.y - v.x * self.y

    # 移動
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# End of Vec.py
