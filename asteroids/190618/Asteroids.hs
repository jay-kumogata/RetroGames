-- | Improved Asteroids Game
-- | Authors: Niko Heikkilä, Katri Passi, AP Väisänen

module Main where
import Graphics.Gloss
import Graphics.Gloss.Interface.Pure.Game
import Graphics.Gloss.Interface.Pure.Simulate
import Graphics.Gloss.Interface.Pure.Display

-- Define base game area --
data AsteroidWorld = Play [Rock] Ship UFO [Bullet]
                   | GameOver
                   deriving (Eq,Show)

type Velocity     = (Float, Float)  -- Velocity is a pair with two floats
type Size         = Float           -- Size is Float
type Age          = Float           -- Age is Float

-- Define Ship, Bullet and Rock --
data Ship   = Ship   PointInSpace Velocity
    deriving (Eq,Show)
data Bullet = Bullet PointInSpace Velocity Age
    deriving (Eq,Show)
data Rock   = Rock   PointInSpace Size Velocity
    deriving (Eq,Show)
-- Our UFO --
data UFO    = UFO  PointInSpace Velocity
    deriving (Eq, Show)

initialWorld :: AsteroidWorld
initialWorld = Play
                   [Rock (150,150)  45 (2,6)
                   ,Rock (-45,201)  45 (13,-8)
                   ,Rock (45,22)    25 (-2,8)
                   ,Rock (-210,-15) 30 (-2,-8)
                   ,Rock (-45,-201) 25 (8,2)
                   ] -- The default rocks
                   (Ship (0,0) (0,0)) -- The initial ship
                   (UFO  (75, 75) (2, 5)) -- The initial UFO
                   [] -- The initial bullets (none)


simulateWorld :: Float -> (AsteroidWorld -> AsteroidWorld)

simulateWorld _        GameOver          = GameOver

simulateWorld timeStep (Play rocks (Ship shipPos shipV) (UFO ufoPos ufoV) bullets)
  | any (collidesWith shipPos) rocks = GameOver
  -- | (collidesWithUFO shipPos) UFO = GameOver
  | otherwise = Play (concatMap updateRock rocks)
                              (Ship newShipPos shipV)
                              (UFO newUFOPos ufoV)
                              (concat (map updateBullet bullets))
  where
      collidesWith :: PointInSpace -> Rock -> Bool
      collidesWith p (Rock rp s _)
       = magV (rp .- p) < s

      collidesWithBullet :: Rock -> Bool
      collidesWithBullet r
       = any (\(Bullet bp _ _) -> collidesWith bp r) bullets

      -- collidesWithUFO :: PointInSpace -> UFO -> Bool
      -- collidesWithUFO p (UFO up _)
       -- = magV (up .- p) < 10

      updateRock :: Rock -> [Rock]
      updateRock r@(Rock p s v)
       | collidesWithBullet r && s < 7
            = []
       | collidesWithBullet r && s > 7
            = splitRock r
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
--      newShipPos = restoreToScreen (shipPos .+ timeStep .* shipV)
      newShipPos = restoreToScreen (shipPos)
  
      newUFOPos :: PointInSpace
      newUFOPos = restoreToScreen (ufoPos .+ timeStep .* (ufoV .+ (rotateV (pi/3) shipPos)))
  
splitRock :: Rock -> [Rock]
splitRock (Rock p s v) = [Rock p (s/2) (3 .* rotateV (pi/3)  v)
                         ,Rock p (s/2) (3 .* rotateV (-pi/3) v) ]
 
destroyUFO :: UFO -> Maybe a
destroyUFO (UFO p v) = Nothing

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

drawWorld (Play rocks (Ship (x,y) (vx,vy)) (UFO (ux,uy) (uvx, uvy)) bullets)
--  = pictures [ship, asteroids, ufo, shots]
  = pictures [ship, asteroids, shots]
   where
    ship      = color white (pictures [translate x y (circle 10)])
--    ship      = color white (pictures [translate x y (rotate (180*(atan (vx/vy))/pi) (line (shipShape)))])
    asteroids = pictures [(color white (line (asteroidShape x y s)))
                         | Rock   (x,y) s _ <- rocks]
--    ufo       = color green (pictures [translate ux uy (circle 10)])
    shots     = pictures [translate x y (color white (circle 2))
                         | Bullet (x,y) _ _ <- bullets]

-- 2019-06-05
shipShape :: [Point]
shipShape = [(0, -10), (-5, 10), (5, 10), (0, -10)]
                
-- 2019-05-29
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
             (Play rocks (Ship shipPos shipVel) ufo bullets)
             = Play rocks (Ship shipPos newVel) ufo
                          (newBullet : bullets)
 where
     newBullet = Bullet shipPos
                        ((-150) .* norm (shipPos .- clickPos))
                        0
--     newVel    = shipVel .+ (50 .* norm (shipPos .- clickPos))
     newVel    = (50 .* norm (shipPos .- clickPos))

handleEvents _ w = w

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
