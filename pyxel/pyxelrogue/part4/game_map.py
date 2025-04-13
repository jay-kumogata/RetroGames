import numpy as np  # type: ignore
import pyxel

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")  # Tiles the player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles the player has seen before
        
    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self) -> None:
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """

        # メモ: pyxel対応のため、愚直に表示(現時点では点描)
        for x in range(self.width):
            for y in range(self.height):
                if self.visible[x][y]:
                    pyxel.pset(x,y,self.tiles["light"][x,y]["fg"])
                elif self.explored[x][y]:
                    pyxel.pset(x,y,self.tiles["dark"][x,y]["fg"])
                else:
                    pyxel.pset(x,y,tile_types.SHROUD["fg"])
        
# end of game_map.py
