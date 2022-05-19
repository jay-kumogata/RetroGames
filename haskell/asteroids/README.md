# Asteroids in Haskell

## Introduction

I came up with the mysterious question of whether a game can be made with mathematical formulas. 
In the past, I've researched the haskell implementation of an old game called Asteroids. 
The shape of the meteorite has been slightly improved and left as it is. 
Here, I think that this topic will be done privately. 
And if you get tired of it again, leave it alone.

<img src="https://github.com/jay-kumogata/RetroGames/raw/main/haskell/asteroids/screenshots/asteroids02.png" width="300">

## How to run

    > stack install gloss
    > stack ghc Asteroids.hs
    > ./Asteroids.exe

## How to Play

Left-click to shoot a bullet and split the meteorite. 
Small meteorites are extinguished. 
If you hit a meteorite, the game is over. 
Right click to replay.
If you split the meteorite, you will get 100 points, 
and if you eliminate it, you will get 500 points.
