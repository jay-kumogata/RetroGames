# Mastermind (4 row) for CHIP-8

## Introduction

The 4 row version of mastermind is a game where you can guess 4 numbers from 1 to 6. 
You can try 10 times. 
If both the value and position of the number match, a "dotted bar" is displayed at the bottom, 
and if only the value matches, a "white bar" is displayed at the bottom. 
Please guess the 4 numbers referring to the hint.

## How to Play

Please execute the following from the Pyxel (version 2.2.10) environment.
Or you can play [here](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.RetroGames.pyxel.mastermind.mastermind).

	> python mastermind.py

## How to Controll

Enter each numbers with the [1] / [2] / [3] / [4] / [5] / [6] keys. 
You can cancel the input with the [Enter] key. 

## Revisions

### Ver. 4

I remastered to Pyxel/Python.
Each number, white bar, and dotted bar are displayed randomly in 3 patterns.

|Pattern|Number|White bar|Dotted bar|
|-------|------|---------|----------|
|1|Bamboos|1,000 point bar|10,000 point bar|
|2|Circles|500 point bar|5,000 point bar|
|3|Characters|100 point bar|1,000 point bar|

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/mastermind/screenshots/mastermind01.gif" width="196">
