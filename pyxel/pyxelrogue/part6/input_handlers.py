from __future__ import annotations
from typing import Optional, TYPE_CHECKING

import tcod.event
import pyxel

from actions import Action, BumpAction, EscapeAction, WaitAction

if TYPE_CHECKING:
    from engine import Engine

MOVE_KEYS = {
    # Arrow keys.
    pyxel.KEY_UP: (0, -1),
    pyxel.KEY_DOWN: (0, 1),
    pyxel.KEY_LEFT: (-1, 0),
    pyxel.KEY_RIGHT: (1, 0),
    pyxel.KEY_HOME: (-1, -1),
    pyxel.KEY_END: (-1, 1),
    pyxel.KEY_PAGEUP: (1, -1),
    pyxel.KEY_PAGEDOWN: (1, 1),
    # Numpad keys.
    pyxel.KEY_KP_1: (-1, 1),
    pyxel.KEY_KP_2: (0, 1),
    pyxel.KEY_KP_3: (1, 1),
    pyxel.KEY_KP_4: (-1, 0),
    pyxel.KEY_KP_6: (1, 0),
    pyxel.KEY_KP_7: (-1, -1),
    pyxel.KEY_KP_8: (0, -1),
    pyxel.KEY_KP_9: (1, -1),
    # Vi keys.
    pyxel.KEY_H: (-1, 0),
    pyxel.KEY_J: (0, 1),
    pyxel.KEY_K: (0, -1),
    pyxel.KEY_L: (1, 0),
    pyxel.KEY_Y: (-1, -1),
    pyxel.KEY_U: (1, -1),
    pyxel.KEY_B: (-1, 1),
    pyxel.KEY_N: (1, 1),
}

WAIT_KEYS = {
    pyxel.KEY_COLON,
    pyxel.KEY_KP_5,
    pyxel.KEY_CLEAR,
}

class EventHandler:

    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        raise NotImplementedError()

class MainGameEventHandler(EventHandler):    
    def handle_events(self) -> None:
        # メモ: pyxel対応として、直接キーバッファを監視するように変更
        action = self.dispatch() 

        if action is None:
            return
        
        action.perform()

        self.engine.handle_enemy_turns()
        self.engine.update_fov()  # Update the FOV before the players next action.
    
    def dispatch(self) -> Optional[Action]:
        # メモ: 何も押されていない場合はNoneを返却
        action: Optional[Action] = None

        player = self.engine.player
        
        # メモ: 移動キーイベント
        for key in MOVE_KEYS.keys():
            if pyxel.btnp(key):
                dx, dy = MOVE_KEYS[key]
                action = BumpAction(player, dx, dy)

        # メモ: 休止キーイベント
        for key in WAIT_KEYS:
            if pyxel.btnp(key):
                action = WaitAction(player)                
            
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            action = EscapeAction(player)

        # No valid key was pressed
        return action

class GameOverEventHandler(EventHandler):
    def handle_events(self) -> None:
        action = self.dispatch()

        if action is None:
            return

        action.perform()

    def dispatch(self) -> Optional[Action]:
        action: Optional[Action] = None

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            action = EscapeAction(self.engine.player)

        # No valid key was pressed
        return action
    
# end of input_handlers.py    
