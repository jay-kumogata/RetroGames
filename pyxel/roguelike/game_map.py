import numpy as np  # type: ignore
import pyxel

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                pyxel.pset(x,y,self.tiles["dark"][x,y]["fg"])
    
# end of game_map.py
