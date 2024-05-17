from __future__ import annotations
from typing import Optional, TYPE_CHECKING

import tcod.event
import pyxel
import color

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
        self.dispatch()

    def on_render(self) -> None:
        self.engine.render()
        
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
        elif pyxel.btnp(pyxel.KEY_V):
            self.engine.event_handler = HistoryViewer(self.engine)
            
        # メモ: マウスイベント
        mouse_x = pyxel.mouse_x // color.chr_x
        mouse_y = pyxel.mouse_y // color.chr_y
        if self.engine.game_map.in_bounds(mouse_x, mouse_y):
            self.engine.mouse_location = mouse_x, mouse_y
            
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

CURSOR_Y_KEYS = {
    pyxel.KEY_UP: -1,
    pyxel.KEY_DOWN: 1,
    pyxel.KEY_PAGEUP: -10,
    pyxel.KEY_PAGEDOWN: 10,
}

class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self) -> None:
        super().on_render()  # Draw the main state as the background.

        # メモ: ログコンソールサイズ(定数)
        log_console_width = 80 - 6 # console.width - 6
        log_console_height = 50 - 6 # console.height - 6

        # Draw a frame with a custom banner title.
        pyxel.rect(3*color.chr_x,3*color.chr_y,
                   log_console_width*color.chr_x,log_console_height*color.chr_y, 1)
        pyxel.text(
            32*color.chr_x,3*color.chr_y, "┤Message history├", 7
        )
        
        # Render the message log using the cursor parameter.
        self.engine.message_log.render_messages(
            1+3, # メモ: 補正
            1+3, # メモ: 補正
            log_console_width - 2,
            log_console_height - 2,
            self.engine.message_log.messages[: self.cursor + 1],
        )

    def dispatch(self) -> Optional[Action]:
        action: Optional[Action] = None

        # Fancy conditional movement to make it feel right.
        for key in CURSOR_Y_KEYS.keys():
            if pyxel.btnp(key):
                adjust = CURSOR_Y_KEYS[key]
                if adjust < 0 and self.cursor == 0:
                    # Only move from the top to the bottom when you're on the edge.
                    self.cursor = self.log_length - 1
                elif adjust > 0 and self.cursor == self.log_length - 1:
                    # Same with bottom to top movement.
                    self.cursor = 0
                else:
                    # Otherwise move while staying clamped to the bounds of the history log.
                    self.cursor = max(0, min(self.cursor + adjust, self.log_length - 1))

        if pyxel.btnp(pyxel.KEY_HOME):
            self.cursor = 0  # Move directly to the top message.
        elif pyxel.btnp(pyxel.KEY_END):
            self.cursor = self.log_length - 1  # Move directly to the last message.
        elif pyxel.btnp(pyxel.KEY_V):  # Any other key moves back to the main game state.
                                       # メモ: Vキーで表示/非表示に仕様変更
            self.engine.event_handler = MainGameEventHandler(self.engine)

        # No valid key was pressed
        return action
        
# end of input_handlers.py    
