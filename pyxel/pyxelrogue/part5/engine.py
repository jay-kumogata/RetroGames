from typing import Iterable, Any

import pyxel 
from tcod.map import compute_fov

from actions import EscapeAction, MovementAction
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.update_fov()

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            print(f'The {entity.name} wonders when it will get to take a real turn.')
        
    def handle_events(self) -> None:
        # メモ: pyxel対応として、直接キーバッファを監視するように変更
        action = self.event_handler.dispatch() 

        if action is None:
            return
        
        action.perform(self, self.player)
        self.handle_enemy_turns()
        self.update_fov()  # Update the FOV before the players next action.

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
        
# end of engine.py        
