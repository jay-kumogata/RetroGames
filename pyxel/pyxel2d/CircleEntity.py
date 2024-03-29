import math
from Const import *
from Vec import *

# 円オブジェクト
class CircleEntity:
    def __init__(self, x, y, radius, type=BodyDynamic, restitution=0.9, deceleration=1.0):
        self.shape = ShapeCircle
        self.type = type 
        self.x = x
        self.y = y
        self.radius = radius
        self.restitution = restitution
        self.deceleration = deceleration
        self.accel = Vec(0, 0)
        self.velocity = Vec(0, 0)
        self.color = 0
        self.onhit = None
        
    # 円を移動
    def move(self, dx, dy): 
        self.x += dx
        self.y += dy

    def isHit(self, x, y):
        d2 = (x - self.x) ** 2 + (y - self.y) ** 2
        return d2 < self.radius ** 2
        
    # 円と矩形の衝突
    def collidedWithRect(self, r):
        # 矩形の４辺上で最も円に近い座標(nx, ny)を求める
        nx = max(r.x, min(self.x, r.x + r.w))
        ny = max(r.y, min(self.y, r.y + r.h))
        
        if (not self.isHit(nx, ny)):      # 衝突なし→リターン
            return

        if (self.onhit):                  # 衝突時のコールバック
            self.onhit(self, r)
        
        d2 = (nx - self.x) ** 2 + (ny - self.y) ** 2
        overlap = abs(self.radius - math.sqrt(d2))
        mx = 0; my = 0

        if (ny == r.y):		        # 上辺衝突
            my = -overlap
        elif (ny == r.y + r.h): 	# 下辺衝突
            my = overlap
        elif (nx == r.x):		# 左辺衝突
            mx = -overlap
        elif (nx == r.x + r.w):		# 右辺衝突
            mx = overlap
        else:				# 矩形の中
            mx = -self.velocity.x
            my = -self.velocity.y

        self.move(mx, my)
        if (mx):    # X軸方向へ反転
            self.velocity = self.velocity.mul(-1 * self.restitution, 1)
        if (my):    # Y軸方向へ反転
            self.velocity = self.velocity.mul(1, -1 * self.restitution)
    
    # 円と線の衝突
    def collidedWithLine(self, line):
        v0 = Vec(line.x0 - self.x + self.velocity.x, line.y0 - self.y + self.velocity.y)
        v1 = self.velocity
        v2 = Vec(line.x1 - line.x0, line.y1 - line.y0)
        cv1v2 = v1.cross(v2)
        try:
            t1 = v0.cross(v1) / cv1v2
            t2 = v0.cross(v2) / cv1v2
        except:
            crossed = False
        else:
            crossed = (0 <= t1 and t1 <= 1) and (0 <= t2 and t2 <= 1)

        if (crossed):
            self.move(-self.velocity.x, -self.velocity.y)
            dot0 = self.velocity.dot(line.norm)   # 法線と速度の内積
            vec0 = line.norm.mul(-2 * dot0)
            self.velocity = vec0.add(self.velocity)
            self.velocity = self.velocity.mul(line.restitution * self.restitution)

    # 円と円の衝突
    def collidedWithCircle(self, peer):
        d2 = (peer.x - self.x) ** 2 + (peer.y - self.y) ** 2
        if (d2 >= ((self.radius + peer.radius) ** 2)):
            return

        if (self.onhit):                  # 衝突時のコールバック
            self.onhit(self, peer)

        if (peer.onhit):                  # 衝突時のコールバック
            peer.onhit(peer, self)
        
        distance = math.sqrt(d2)
        if (distance < 0.01): distance = 0.01
        overlap = self.radius + peer.radius - distance
        
        v = Vec(self.x - peer.x, self.y - peer.y)
        aNormUnit = v.mul(1 / distance)        # 法線単位ベクトル１
        bNormUnit = aNormUnit.mul(-1)          # 法線単位ベクトル２

        if (self.type == BodyDynamic and peer.type == BodyStatic):
            self.move(aNormUnit.x * overlap, aNormUnit.y * overlap)
            dot0 = self.velocity.dot(aNormUnit)   # 法線と速度の内積
            vec0 = aNormUnit.mul(-2 * dot0)
            self.velocity = vec0.add(self.velocity)
            self.velocity = self.velocity.mul(self.restitution)
        elif (peer.type == BodyDynamic and self.type == BodyStatic):
            peer.move(bNormUnit.x * overlap, bNormUnit.y * overlap)
            dot1 = peer.velocity.dot(bNormUnit)   # 法線と速度の内積
            vec1 = bNormUnit.mul(-2 * dot1)
            peer.velocity = vec1.add(peer.velocity)
            peer.velocity = peer.velocity.mul(peer.restitution)
        else:
            self.move(aNormUnit.x * overlap / 2, aNormUnit.y * overlap / 2)
            peer.move(bNormUnit.x * overlap / 2, bNormUnit.y * overlap / 2)

            aTangUnit = Vec(aNormUnit.y * -1, aNormUnit.x) # 接線ベクトル１
            bTangUnit = Vec(bNormUnit.y * -1, bNormUnit.x) # 接線ベクトル２

            aNorm = aNormUnit.mul(aNormUnit.dot(self.velocity)) # aベクトル法線成分
            aTang = aTangUnit.mul(aTangUnit.dot(self.velocity)) # aベクトル接線成分
            bNorm = bNormUnit.mul(bNormUnit.dot(peer.velocity)) # bベクトル法線成分
            bTang = bTangUnit.mul(bTangUnit.dot(peer.velocity)) # bベクトル接線成分

            self.velocity = Vec(bNorm.x + aTang.x, bNorm.y + aTang.y)
            peer.velocity = Vec(aNorm.x + bTang.x, aNorm.y + bTang.y)

# End of CicleEntity.py
