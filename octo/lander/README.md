# Lunar Lander for CHIP-8

## Introduction

[Lunar Lander](https://github.com/massung/CHIP-8/blob/master/games/sources/lander.c8) was also reprinted in octo assembly language. 
This is a game where you operate a lunar module and land on the moon. 
Lunar Lander (1979 / Atari) is a famous implementation, 
but the Apollo program's lunar lander simulator seems to be the original. 

<img src="https://github.com/jay-kumogata/Nostalgia/raw/main/octo/screenshots/lander03.png" width="300">

## How to play


You can play [in your browser](https://johnearnest.github.io/Octo/index.html?key=jQyyYdGT).

## How to Controll

Use the [W] / [A] / [D] keys or [up-arrow] / [left-arrow] / [right-arrow] keys to move up / left / right.  
Operate the lunar module and land on the surface of the moon.

## Explanation

I found an article that summarizes [the history](https://www.pcmag.com/news/50-years-on-the-moon-the-evolution-of-lunar-lander-games).
The first implementation was Moonlander (1973 / DEC GT-40), and it seems that it has been implemented on various platforms since then.

The original of this work is an implementation by Mr. Jeffrey Massung. 
The source described in Chip8 assembler is converted to Octo notation. 
So I haven't changed the logic. 
Sometimes difficult terrain appears, but I imagine this is also a specification, not a bug.

Occasionally difficult terrain will appear. 
It appears randomly regardless of the level. 
The difficulty level may not have been adjusted sufficiently. 
Lunar Lander also has [an implementation](https://github.com/yupferris/Uno8/blob/master/GamesPreprocessor/Games/Lunar%20Lander%20(Udo%20Pernisz,%201979).ch8) by Mr. Udo Pernisz in 1979. 
I am currently working on a reprint, so we will publish it in the near future.
