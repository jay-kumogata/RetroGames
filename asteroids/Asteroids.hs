-- 2019-05-29
-- Asteroids Game 解析

-- 下記URLの実装を解析した．
-- https://github.com/nikoheikkila/asteroids

-- 2021-04-27
-- 数式でゲームが作れるのかという問いで，このコードを思い出す
-- 自機と点数表示を修正した

-- Glossライブラリベースで設計されている．
module Main where
import Graphics.Gloss
import Graphics.Gloss.Interface.Pure.Game
import Graphics.Gloss.Interface.Pure.Simulate
import Graphics.Gloss.Interface.Pure.Display

-- AsteroidWorldというゲーム世界の定義．
-- data AsteroidWorld = Play [Rock] Ship UFO [Bullet] 
data AsteroidWorld = Play [Rock] Ship [Bullet] Score
                   | GameOver
                   deriving (Eq,Show)

-- Playは，Glossライブラリの構築子．
-- [Rock]は岩情報のリスト．
-- Shipは船情報．
-- [Bullet]は弾情報のリスト．

type Velocity     = (Float, Float)  -- 速度Velocityは，単精度Floatのペア．
type Size         = Float           -- Size is Float
type Age          = Float           -- Age is Float
type Score       = Integer        -- Score is Integer

-- 船情報Shipは，座標PointInSpace，速度Velocityから構成．
data Ship   = Ship   PointInSpace Velocity
    deriving (Eq,Show)
-- 弾情報Bulletは，座標PointInSpace，速度Velocity，年齢Ageから構成．
data Bullet = Bullet PointInSpace Velocity Age
    deriving (Eq,Show)
-- 岩情報Rockは，座標PointInSpace，サイズSize，速度Velocityから構成．
data Rock   = Rock   PointInSpace Size Velocity
    deriving (Eq,Show)

-- 初期化されたゲーム世界を返却する関数initialWorldを定義．
initialWorld :: AsteroidWorld
initialWorld = Play
                   [Rock (150,150)  45 (2,6)
                   ,Rock (-45,201)  45 (13,-8)
                   ,Rock (45,22)    25 (-2,8)
                   ,Rock (-210,-15) 30 (-2,-8)
                   ,Rock (-45,-201) 25 (8,2)
                   ] -- The default rocks
                   (Ship (0,0) (0,0)) -- The initial ship
                   [] -- The initial bullets (none)
                   0

-- ゲーム世界をシミュレートする関数simulateWorldを定義．
-- 第1引数Floatは，経過時間timeStepを指定．
-- 第2引数AsteroidWorldは，現時点でのゲーム世界を指定．
-- 第3引数AsteroidWorldは，時間経過した後のゲーム世界が返却．

simulateWorld :: Float -> (AsteroidWorld -> AsteroidWorld)

-- ゲームオーバーの場合は，ゲームオーバを返却．
simulateWorld _        GameOver          = GameOver

simulateWorld timeStep (Play rocks (Ship shipPos shipV) bullets score)
  | any (collidesWith shipPos) rocks = GameOver
  | otherwise = Play (concatMap updateRock rocks)
                              (Ship newShipPos shipV)
                              (concat (map updateBullet bullets))
                              (score + sum (map updateScore rocks))
  where
    -- 座標pが，岩Rockに衝突したか否かを返却．
    -- 岩座標rpから岩サイズsだけ離れた領域（円）に，座標pが含まれるか否かを返却．
      collidesWith :: PointInSpace -> Rock -> Bool
      collidesWith p (Rock rp s _)
       = magV (rp .- p) < s

    -- いずれかの弾座標bpが，岩rに衝突したか否かを返却．
      collidesWithBullet :: Rock -> Bool
      collidesWithBullet r
       = any (\(Bullet bp _ _) -> collidesWith bp r) bullets

      updateRock :: Rock -> [Rock]
      updateRock r@(Rock p s v)
      -- 岩に弾が当たって，岩のサイズが7より小さい場合には消滅．
       | collidesWithBullet r && s < 7
            = []
      -- 岩に弾が当たって，岩のサイズが7より大きい場合には分裂．
       | collidesWithBullet r && s > 7
            = splitRock r
      -- 上記以外の場合，時間timeStep分だけ位置を更新．
      -- 岩に弾が当たって，岩のサイズが7の場合は，ここに含まれる．
       | otherwise
            = [Rock (restoreToScreen (p .+ timeStep .* v)) s v]

      updateBullet :: Bullet -> [Bullet]
      updateBullet (Bullet p v a)
        | a > 5
             = []
        | any (collidesWith p) rocks
             = []
        | otherwise
             = [Bullet (restoreToScreen (p .+ timeStep .* v)) v
                       (a + timeStep)]

      newShipPos :: PointInSpace
--      弾を発射しても反動で動かない
--      newShipPos = restoreToScreen (shipPos .+ timeStep .* shipV)
      newShipPos = restoreToScreen (shipPos)
  
      updateScore :: Rock -> Integer
      updateScore r@(Rock p s v)
      -- 岩に弾が当たって，岩のサイズが7より小さい場合には消滅．
       | collidesWithBullet r && s < 7
            = 500
      -- 岩に弾が当たって，岩のサイズが7より大きい場合には分裂．
       | collidesWithBullet r && s > 7
            = 100
      -- 上記以外の場合，時間timeStep分だけ位置を更新．
      -- 岩に弾が当たって，岩のサイズが7の場合は，ここに含まれる．
       | otherwise
            = 0

splitRock :: Rock -> [Rock]
splitRock (Rock p s v) = [Rock p (s/2) (3 .* rotateV (pi/3)  v)
                         ,Rock p (s/2) (3 .* rotateV (-pi/3) v) ]
 
restoreToScreen :: PointInSpace -> PointInSpace
restoreToScreen (x,y) = (cycleCoordinates x, cycleCoordinates y)

cycleCoordinates :: (Ord a, Num a) => a -> a
cycleCoordinates x
    | x < (-400) = 800+x
    | x > 400    = x-800
    | otherwise  = x

drawWorld :: AsteroidWorld -> Picture

drawWorld GameOver 
   = pictures [scale 0.3 0.3 . translate (-400) 0 
               . color white . text $ "Game Over!",
           scale 0.1 0.1 . translate (-1150) (-550)
           . color white . text $ 
           "Click right mousebutton to restart"]

drawWorld (Play rocks (Ship (x,y) (vx,vy)) bullets score)
  = pictures [ship, asteroids, shots, pts]
   where
--    ship      = color white (pictures [translate x y (circle 10)])
    ship      = color white (pictures [translate x y (rotate (180*(atan2 vx vy)/pi) (line (shipShape)))])
    asteroids = pictures [(color white (line (asteroidShape x y s)))
                         | Rock   (x,y) s _ <- rocks]
    shots     = pictures [translate x y (color white (circle 2))
                         | Bullet (x,y) _ _ <- bullets]
    pts          = pictures [ translate (-200) (200) (scale 0.3 0.3 (color white  (text $ (show score)))) ]

-- 2019-06-05: 自機キャラクタ
shipShape :: [Point]
shipShape = [(0, -10), (-5, 10), (5, 10), (0, -10)]
                
-- 2019-05-29: 岩キャラクタ
asteroidShape :: Float -> Float -> Float -> [Point]
asteroidShape x y s = [(x+0.7*s,y+0.5*s), (x-0.1*s,y+0.8*s),
                       (x-0.7*s,y+0.6*s), (x-0.9*s,y-0.1*s),
                       (x-0.7*s,y-0.9*s), (x+0.0*s,y-0.7*s),
                       (x+0.6*s,y-0.8*s), (x+0.9*s,y-0.2*s),
                       (x+0.5*s,y+0.1*s), (x+0.7*s,y+0.5*s)]

handleEvents :: Event -> AsteroidWorld -> AsteroidWorld

-- new eventhandler for restarting --
handleEvents (EventKey (MouseButton RightButton) Down _ _) GameOver
          = initialWorld


handleEvents (EventKey (MouseButton LeftButton) Down _ clickPos)
             (Play rocks (Ship shipPos shipVel) bullets score)
             = Play rocks (Ship shipPos newVel) 
                          (newBullet : bullets)
                          (score+10)
 where
     newBullet = Bullet shipPos
                        ((-150) .* norm (shipPos .- clickPos))
                        0
     -- 慣性の法則で弾の速度にも自機の速度が影響
     -- newVel    = shipVel .+ (50 .* norm (shipPos .- clickPos))
     newVel    = (50 .* norm (shipPos .- clickPos))

handleEvents _ w = w

-- 2D座標を扱う関数ライブラリ
type PointInSpace = (Float, Float)

(.-) , (.+) :: PointInSpace -> PointInSpace -> PointInSpace
(x,y) .- (u,v) = (x-u,y-v)
(x,y) .+ (u,v) = (x+u,y+v)

(.*) :: Float -> PointInSpace -> PointInSpace
s .* (u,v) = (s*u,s*v)

infixl 6 .- , .+
infixl 7 .*

norm :: PointInSpace -> PointInSpace
norm (x,y) = let m = magV (x,y) in (x/m,y/m)

magV :: PointInSpace -> Float
magV (x,y) = sqrt (x**2 + y**2)

limitMag :: Float -> PointInSpace -> PointInSpace
limitMag n pt = if (magV pt > n)
                  then n .* (norm pt)
                  else pt

rotateV :: Float -> PointInSpace -> PointInSpace
rotateV r (x,y) = (x * cos r - y * sin r
                  ,x * sin r + y * cos r)

-- Main function that launches the game --
main = play
         (InWindow "Asteroids!" (550,550) (20,20))
         black
         24
         initialWorld
         drawWorld
         handleEvents
         simulateWorld

-- Graphics.Gloss.Interface.
-- Pure.Game: ワールドを制御/描画する関数が純粋な場合
-- IO.Game: ワールドを制御/描画する関数がIOモナドの場合

         
