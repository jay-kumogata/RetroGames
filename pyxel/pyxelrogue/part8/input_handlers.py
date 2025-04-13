from __future__ import annotations
from typing import Optional, TYPE_CHECKING

import tcod.event
import pyxel
import color

import actions
from actions import (
    Action,
    BumpAction,
    PickupAction,    
    WaitAction
)
import color
import exceptions

if TYPE_CHECKING:
    from engine import Engine
    from entity import Item
    
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
        self.handle_action(self.dispatch())

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """
        if action is None:
            return False

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.engine.message_log.add_message(exc.args[0], color.impossible)
            return False  # Skip enemy turn on exceptions.

        self.engine.handle_enemy_turns()

        self.engine.update_fov()
        return True
        
    def on_render(self) -> None:
        self.engine.render()
        
class MainGameEventHandler(EventHandler):    
    
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
            
        # メモ: マウスイベント
        mouse_x = pyxel.mouse_x // color.chr_x
        mouse_y = pyxel.mouse_y // color.chr_y
        if self.engine.game_map.in_bounds(mouse_x, mouse_y):
            self.engine.mouse_location = mouse_x, mouse_y

        # メモ: ログ閲覧窓を表示
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            raise SystemExit()            
        elif pyxel.btnp(pyxel.KEY_V):
            self.engine.event_handler = HistoryViewer(self.engine)

        # メモ: アイテムを拾う(Get)
        elif pyxel.btnp(pyxel.KEY_G):
            action = PickupAction(player)            
        # メモ: アイテム一覧窓を表示(Item)
        elif pyxel.btnp(pyxel.KEY_I):
            self.engine.event_handler = InventoryActivateHandler(self.engine)
        # メモ: アイテムを落とす(Drop)
        elif pyxel.btnp(pyxel.KEY_D):
            self.engine.event_handler = InventoryDropHandler(self.engine)
            
        # No valid key was pressed
        return action

class GameOverEventHandler(EventHandler):

    def dispatch(self) -> None:
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            raise SystemExit()            
    
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
        color.rect(3, 3, log_console_width,log_console_height, 1)
        
        color.text(32, 3, "┤Message history├", 7)
        
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
        elif pyxel.btnp(pyxel.KEY_RETURN):  # Any other key moves back to the main game state.
                                            # メモ: RETURNキーで非表示に仕様変更
            self.engine.event_handler = MainGameEventHandler(self.engine)

        # No valid key was pressed
        return action

class AskUserEventHandler(EventHandler):
    """Handles user input for actions which require special input."""

    def handle_action(self, action: Optional[Action]) -> bool:
        """Return to the main event handler when a valid action was performed."""
        if super().handle_action(action):
            self.engine.event_handler = MainGameEventHandler(self.engine)
            return True
        return False

    def dispatch(self) -> Optional[Action]:
        
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            """By default any key exits this input handler."""
            """メモ: RETURNキーで非表示に仕様変更"""
            """By default any mouse click exits this input handler."""
            """メモ: マウス左ボタンで非表示に仕様変更"""
            return self.on_exit()
        
        return None

    def on_exit(self) -> Optional[Action]:
        """Called when the user is trying to exit or cancel an action.

        By default this returns to the main event handler.
        """
        self.engine.event_handler = MainGameEventHandler(self.engine)
        return None

ITEM_KEYS = {
    pyxel.KEY_A:  0, pyxel.KEY_B:  1,
    pyxel.KEY_C:  2, pyxel.KEY_D:  3,
    pyxel.KEY_E:  4, pyxel.KEY_F:  5,
    pyxel.KEY_G:  6, pyxel.KEY_H:  7,
    pyxel.KEY_I:  8, pyxel.KEY_J:  9,
    pyxel.KEY_K: 10, pyxel.KEY_L: 11,
    pyxel.KEY_M: 12, pyxel.KEY_N: 13,
    pyxel.KEY_O: 14, pyxel.KEY_P: 15,
    pyxel.KEY_Q: 16, pyxel.KEY_R: 17,
    pyxel.KEY_S: 18, pyxel.KEY_T: 19,
    pyxel.KEY_U: 20, pyxel.KEY_V: 21,
    pyxel.KEY_W: 22, pyxel.KEY_X: 23,
    pyxel.KEY_Y: 24, pyxel.KEY_Z: 25,
}

class InventoryEventHandler(AskUserEventHandler):
    """This handler lets the user select an item.

    What happens then depends on the subclass.
    """

    TITLE = "<missing title>"

    def on_render(self) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render()
        number_of_items_in_inventory = len(self.engine.player.inventory.items)

        height = number_of_items_in_inventory + 2

        if height <= 3:
            height = 3

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        y = 0

        width = len(self.TITLE) + 4

        color.rect(x, y, width,height, 1)
        color.text(x, y, self.TITLE, 7)

        if number_of_items_in_inventory > 0:
            for i, item in enumerate(self.engine.player.inventory.items):
                item_key = chr(ord("a") + i)
                color.text(x + 1, y + i + 1, f"({item_key}) {item.name}",7)
        else:
            color.text(x + 1, y + 1, "(Empty)",7)

    def dispatch(self) -> Optional[Action]:
        action: Optional[Action] = None

        player = self.engine.player

        for key in ITEM_KEYS.keys():
            if pyxel.btnp(key):
                index = ITEM_KEYS[key]
                
                if 0 <= index <= 26:
                    try:
                        selected_item = player.inventory.items[index]
                    except IndexError:
                        self.engine.message_log.add_message("Invalid entry.", color.invalid)
                        return None
                    return self.on_item_selected(selected_item)
                
        return super().dispatch()

    def on_item_selected(self, item: Item) -> Optional[Action]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()

class InventoryActivateHandler(InventoryEventHandler):
    """Handle using an inventory item."""

    TITLE = "Select an item to use"

    def on_item_selected(self, item: Item) -> Optional[Action]:
        """Return the action for the selected item."""
        return item.consumable.get_action(self.engine.player)


class InventoryDropHandler(InventoryEventHandler):
    """Handle dropping an inventory item."""

    TITLE = "Select an item to drop"

    def on_item_selected(self, item: Item) -> Optional[Action]:
        """Drop this item."""
        return actions.DropItem(self.engine.player, item)

    
# end of input_handlers.py    
