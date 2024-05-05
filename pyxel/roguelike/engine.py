from typing import Set, Iterable, Any

import pyxel

from actions import EscapeAction, MovementAction
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self) -> None:
        action = self.event_handler.dispatch()

        if action is None:
            return

        if isinstance(action, MovementAction):
            if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
                self.player.move(dx=action.dx, dy=action.dy)

        elif isinstance(action, EscapeAction):
            raise SystemExit()

    def render(self) -> None:
        pyxel.cls(1)
        self.game_map.render()
        for entity in self.entities:
            pyxel.pset(entity.x, entity.y, entity.color)

# end of engine.py        
