# Vbrix for CHIP-8

## Introduction

Bounce the ball with the paddle to break the blocks. 

<img src="https://github.com/jay-kumogata/Nostalgia/raw/main/octo/screenshots/vbrix04.png" width="300">

## How to Play

You can play [in your browser](https://johnearnest.github.io/Octo/index.html?key=drtrCk7o).

## How to Controll

Press the [A] key to start the game.
The paddle can be moved up and down with the [1] / [Q] keys.

## Revisions

### Ver. 1

The octo version of vbrix has been completed. You can play [here](https://johnearnest.github.io/Octo/index.html?key=drtrCk7o).
In particular, the following processing is interesting.

- When a collision between a ball and a block is detected, the XY coordinates are divided by 3 to obtain the logical coordinates (from line 192 to line 199).
- Furthermore, the logical coordinates are tripled to obtain the physical coordinates, and the block of those coordinates is erased (from line 200 to line 209).

### Ver. 0

I started to port vertical block breakout, named vbirx, for chip8 to octo by notation conversion.
The correspondence between assembly language and octo notation of chip8 is as follows.

| assembly language | octo notation |
|---------------|----------|
| mov v0, v1 | v0 := v1 |
| add v2, v3 | v2 += v3 |
| skne v4, v5 | if v4 == v5 then |
| skeq v6,v7 | if v6 != v7 then |
| jmp label | jump label |
| jsr label | label |

The assembly language of chip8 also seems to have multiple notations, and it differs slightly depending on the source code.
