# PyGmc4

## Introduction

PyGmc4 is a GMC-4 emulator runs on Pyxel/Python library.
[Dev Notes](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pygmc4/doc/091211_DevNotes.md) here.

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pygmc4/screenshots/led03.gif)

## How to Play

- (a) Install the Python3.8 (python-3.8.9.exe), which can be obtained from https://www.python.org/downloads/
- (b) Install the Pyxel1.7.0 on Python from the command line:  
  - C> pip install pyxel
- (c) From the command line, run:
  - C> python PyGmc4.py \<FXP file name\>
  - Example: C> python PyxelChip8.py led/led.fxp
- (d) Click [x] when finished

## How to control
  
The keys are mapped as follows.

	         
	Original |C|D|E|F| Mapping to |1|2|3|4|
	         |8|9|A|B|            |Q|W|E|R|
	         |4|5|6|7|            |A|S|D|F|
	         |0|1|2|3|            |Z|X|C|V|

## Specification
### Memory
- RAM (00H - 5FH)

### Registers
- Data Registers (A,B,A',B')
- Address Registers (X,Y,X',Y')
- Control Registers (PC, Flag)

### Graphics
- Binary LED (No.0 .. No.6)
- 7-segment LED 

### Instruction set
- I/O instructions: Key input, Binary LED control, 7-segment LED control, Sound
- Transfer instructions: Assignment, Exchange
- Arithmetic instructions: Real calculation, Compare
- Conditional Branch: Jump, Timer wait

### Keyboard
- Hexadecimal keyboard
