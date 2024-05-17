from __future__ import annotations

from typing import TYPE_CHECKING

import color
import pyxel

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()
    
def render_bar(
    current_value: int, maximum_value: int, total_width: int        
) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    pyxel.rect(0*color.chr_x, 45*color.chr_y, total_width*color.chr_x, 1*color.chr_y, color.bar_empty)

    if bar_width > 0:
        pyxel.rect(
            0*color.chr_x, 45*color.chr_y, bar_width*color.chr_x, 1*color.chr_y, color.bar_filled
        )

    pyxel.text(1*color.chr_x, 45*color.chr_y, f"HP: {current_value}/{maximum_value}", color.bar_text)

def render_names_at_mouse_location(
    x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x, y=mouse_y, game_map=engine.game_map
    )

    pyxel.text(x*color.chr_x, y*color.chr_y, names_at_mouse_location, 7)
    
# end of render_functions.py    
