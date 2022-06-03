# Turing Pattern

## Introduction

There was a mathematician named Alan Turing. 
His major achievements include Turing Machine (computational model), Turing Test (artificial intelligence), and Turing Bombe (cryptanalysis). 
And one of the lesser-known achievements of his later years is the Turing Pattern (cellular automaton). 
Numerically solving a certain PDE reveals a pattern found in nature (industrial application is unknown at this time). 
Since there is [a Python implementation](https://ipython-books.github.io/124-simulating-a-partial-differential-equation-reaction-diffusion-systems-and-turing-patterns/), 
I tried to display it with Pyxel as a practice.

![](https://github.com/jay-kumogata/RetroGames/raw/main/pyxel/turing/screenshots/turing01.gif)


## How to Run

Please execute the following from the Pyxel (version 1.7.0) environment.

	> python turing.py

## Remarks

Initially it starts from a random state. 
As time goes by, you can see that an island is formed. 
In the Pyxel, since the palette is fixed, it cannot be displayed like a heat map. 
Here, I devised so that negative values are displayed in dark colors and positive values are displayed in bright colors. 
However, Alan Turing, who calculated by hand when the calculator was slow, is still a genius.

There seem to be various models to display Turing Patterns. 
Here, the "FitzHugh–Nagumo model" devised by Prof. Jinichi Nagumo, a former professor at the University of Tokyo, is used. 
There seems to be other "Gray-Scott models" etc., but since it is a practice of Pyxel, I will not go deeper than this.
