from __future__ import annotations

from typing import TYPE_CHECKING

import pyxel

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from input_handlers import MainGameEventHandler

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap
    from input_handlers import EventHandler

class Engine:
    game_map: GameMap

    def __init__(self, player: Entity):
        self.event_handler: EventHandler = MainGameEventHandler(self)
        self.player = player
    
    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                entity.ai.perform()

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible
        
    def render(self) -> None:
        pyxel.cls(0)
        self.game_map.render()

        #console.print(
        #    x=1,
        #    y=47,
        #    string=f"HP: {self.player.fighter.hp}/{self.player.fighter.max_hp}",
        #)
        pyxel.line(1,47,6,47,7) # TODO: HitPoint表示(キャラ表示に変更時に)
        
# end of engine.py        
