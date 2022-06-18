# PyxelChip8

## Introduction

PyxelChip8 is a CHIP-8 emulator that runs on Pyxel/Python library.

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/amabie02.gif" width="300">

## How to Play

- (a) Install the Python3.8 (python-3.8.9.exe), which can be obtained from https://www.python.org/downloads/
- (b) Install the Pyxel1.7.0 on Python from the command line:  
  - C> pip install pyxel
- (c) Unzip the Chip8 Game Pack (c8games.zip) archive, which can be obtained from http://www.zophar.net/roms.phtml?op=show&type=chip8
- (d) From the command line, run:
  - C> python PyxelChip8.py \<ROM file name\>
  - Example: C> python PyxelChip8.py c8games/VBRIX
- (e) Click [x] when finished

## How to control
  
The keys are mapped as follows.
  
	Original |1|2|3|C| Mapping to |1|2|3|4|
	         |4|5|6|D|            |Q|W|E|R|
	         |7|8|9|E|            |A|S|D|F|
	         |A|0|B|F|            |Z|X|C|V|

## Specification
### Memory
- RAM (200H - F10H)
- Hexadecimal font (F10H -F60H)

### Registers
- Data Registers (V0 .. VF)
- Address Registers (I)
- Timers (Delay and Sound)
- Stack (16 word length and stack pointer)

### Graphics
- Sprite (CHIP-8 Mode: 8 x 1 .. 15)
- Collision Flag
- Hexadecimal font
  
### Instruction set
- CHIP-8 instructions (assignment, arithmetic, conditional branch, subroutine call, draw sprite, etc.)

### Keyboard
- Hexadecimal keyboard
