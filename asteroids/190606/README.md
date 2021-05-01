# Improved Asteroids

In this section, we present our first complete Haskell program -- a simple *Asteroids* game. The goal of this section is to familiarize ourselves with the basic syntax and constructs in the Haskell. If you want to download the code, it is available here.

In the asteroids game presented in this section, the player controls a starship (drawn as a red circle), with the aim of shooting apart rocks (brown circles). The game ends when a rock hits the starship. The ship is controlled by the mouse: clicking at a rock shoots a bullet and the ship gains momentum in the opposite direction.

## Installation

    cabal update
    cabal install gloss
    ghc --make Asteroids.hs -O3

## Exercise (or TODO)

The marketing department is bit worried about the commercial success of this Asteroids clone, and needs you to perk it up a bit. Specifically, the marketing department has the following complaints:

- Currently, the game must be restarted to play another game after the ship hits a rock. Fix the game so it is possible to play another round after the *Game Over* screen has been shown.
- The marketing department has concerns about a game where a red circle shoots smaller red circles at big brown circles. The rocks needs more personality! (Hint: Check the definitions in the Graphics.Gloss.Data.Picture-module)
- The marketing department had a picture of an UFO in the game advertisement. **There must be an UFO in the game!** A good plan of attack is to:
    - ~~Create an UFO datatype. (You'll need to revise this later.)~~
    - ~~Add the UFO to the game state.~~
    - ~~Adjust the initialWorld function so that the UFO is initialized properly. (Commenting out other functions makes this easier)~~
    - ~~Adjust the drawWorld function so that the UFO is drawn.~~
    - ~~Adjust the simulateWorld function so that the UFO moves around. You'll need to invent some state variables for the UFO to track it's location and direction.~~
