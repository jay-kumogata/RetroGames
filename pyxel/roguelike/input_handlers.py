from __future__ import annotations

import os
from typing import Callable, Optional, Tuple, TYPE_CHECKING, Union

import pyxel

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

CONFIRM_KEYS = {
    pyxel.KEY_RETURN,
    pyxel.KEY_KP_ENTER,
}

CURSOR_Y_KEYS = {
    pyxel.KEY_UP: -1,
    pyxel.KEY_DOWN: 1,
    pyxel.KEY_PAGEUP: -10,
    pyxel.KEY_PAGEDOWN: 10,
}

# メモ: アイテム番号への変換表    
ITEM_KEYS = {
    pyxel.KEY_A:  0, pyxel.KEY_B:  1, pyxel.KEY_C:  2, pyxel.KEY_D:  3,
    pyxel.KEY_E:  4, pyxel.KEY_F:  5, pyxel.KEY_G:  6, pyxel.KEY_H:  7,
    pyxel.KEY_I:  8, pyxel.KEY_J:  9, pyxel.KEY_K: 10, pyxel.KEY_L: 11,
    pyxel.KEY_M: 12, pyxel.KEY_N: 13, pyxel.KEY_O: 14, pyxel.KEY_P: 15,
    pyxel.KEY_Q: 16, pyxel.KEY_R: 17, pyxel.KEY_S: 18, pyxel.KEY_T: 19,
    pyxel.KEY_U: 20, pyxel.KEY_V: 21, pyxel.KEY_W: 22, pyxel.KEY_X: 23,
    pyxel.KEY_Y: 24, pyxel.KEY_Z: 25,
}

ActionOrHandler = Union[Action, "BaseEventHandler"]
"""An event handler return value which can trigger an action or switch active handlers.

If a handler is returned then it will become the active handler for future events.
If an action is returned it will be attempted and if it's valid then
MainGameEventHandler will become the active handler.
"""

class BaseEventHandler:
    def handle_events(self) -> BaseEventHandler:
        """Handle an event and return the next active event handler."""
        state = self.dispatch()
        if isinstance(state, BaseEventHandler):
            return state
        assert not isinstance(state, Action), f"{self!r} can not handle actions."
        return self

    def on_render(self) -> None:
        raise NotImplementedError()

    def ev_quit(self) -> Optional[Action]:
        raise SystemExit()

    # メモ: イベントハンドラとしての基本動作
    def ev_keydown(self) -> Optional[Action]:
        return None

    def ev_mousebuttondown(self) -> Optional[Action]:
        return None

    def ev_mousemotion(self) -> Optional[Action]:
        return None
    
    def dispatch(self) -> Optional[Action]:
        action = self.ev_keydown()
        if action is not None:
            return action
        action = self.ev_mousebuttondown()
        if action is not None:
            return action
        #メモ: マウスを利用する場合
        #return self.ev_mousemotion()
        return None
        
class PopupMessage(BaseEventHandler):
    """Display a popup text window."""

    def __init__(self, parent_handler: BaseEventHandler, text: str):
        self.parent = parent_handler
        self.text = text

    def on_render(self) -> None:
        """Render the parent and dim the result, then print the message on top."""
        self.parent.on_render()
        #メモ: 格子模様を表示(全体的に色を暗くする演出)
        for x in range(0, color.width * color.chr_x, 2):
            for y in range(0, color.height * color.chr_y, 2):
                pyxel.pset(x,y,0)
                pyxel.pset(x+1,y+1,0)

        #メモ: 文字の背景を黒くして、文字を白で表示する(文字を読みやすくするため)
        color.textcbg(
            color.width // 2,
            color.height // 2,
            self.text,
            color.white,
            color.black,
        )

    def ev_keydown(self) -> Optional[BaseEventHandler]:
        """Any key returns to the parent handler."""
        """メモ: SPACEキーで親ハンドラに戻るに仕様変更"""
        if pyxel.btnp(pyxel.KEY_SPACE):
            return self.parent
    
class EventHandler(BaseEventHandler):

    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> BaseEventHandler:
        """Handle events for input handlers with an engine."""
        action_or_state = self.dispatch()
        if isinstance(action_or_state, BaseEventHandler):
            return action_or_state
        if self.handle_action(action_or_state):
            # A valid action was performed.
            if not self.engine.player.is_alive:
                # The player was killed sometime during or after the action.
                return GameOverEventHandler(self.engine)
            elif self.engine.player.level.requires_level_up:
                return LevelUpEventHandler(self.engine)            
            return MainGameEventHandler(self.engine)  # Return to the main handler.
        return self
    
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

    def ev_mousemotion(self) -> None:    
        # メモ: マウス移動イベント
        mouse_x = pyxel.mouse_x // color.chr_x
        mouse_y = pyxel.mouse_y // color.chr_y
        if self.engine.game_map.in_bounds(mouse_x, mouse_y):
            self.engine.mouse_location = mouse_x, mouse_y
        return None

    def on_render(self) -> None:
        self.engine.render()

class MainGameEventHandler(EventHandler):    
    
    def ev_keydown(self) -> Optional[ActionOrHandler]:
        # メモ: 何も押されていない場合はNoneを返却
        action: Optional[Action] = None

        player = self.engine.player

        # メモ: 階段キーイベント
        if pyxel.btnp(pyxel.KEY_PERIOD) and (
            pyxel.btn(pyxel.KEY_LSHIFT) or pyxel.btn(pyxel.KEY_RSHIFT)
        ):
            return actions.TakeStairsAction(player)                
        
        # メモ: 移動キーイベント
        for key in MOVE_KEYS.keys():
            if pyxel.btnp(key):
                dx, dy = MOVE_KEYS[key]
                action = BumpAction(player, dx, dy)

        # メモ: 休止キーイベント
        for key in WAIT_KEYS:
            if pyxel.btnp(key):
                action = WaitAction(player)                

        # メモ: PyxelではESCAPEで終了となるため、Qに変更
        if pyxel.btnp(pyxel.KEY_Q): 
            raise SystemExit()

        # メモ: ログ閲覧窓を表示
        elif pyxel.btnp(pyxel.KEY_V):
            return HistoryViewer(self.engine)

        # メモ: アイテムを拾う(Get)
        elif pyxel.btnp(pyxel.KEY_G):
            action = PickupAction(player)            

        # メモ: アイテム一覧窓を表示(Item)
        elif pyxel.btnp(pyxel.KEY_I):
            return InventoryActivateHandler(self.engine)
            
        # メモ: アイテムを落とす(Drop)
        elif pyxel.btnp(pyxel.KEY_D):
            return InventoryDropHandler(self.engine)
        # メモ: キャラクタ情報を表示(Character)
        elif pyxel.btnp(pyxel.KEY_C):
            return CharacterScreenEventHandler(self.engine)            
        # メモ: マウスがない場合にキーボードで代替する(Look)
        elif pyxel.btnp(pyxel.KEY_SLASH):
            return LookHandler(self.engine)
        
        # No valid key was pressed
        return action

class GameOverEventHandler(EventHandler):

    def on_quit(self) -> None:
        """Handle exiting out of a finished game."""
        if os.path.exists("savegame.sav"):
            os.remove("savegame.sav")  # Deletes the active save file.
        raise exceptions.QuitWithoutSaving()  # Avoid saving a finished game.

    def ev_quit(self) -> None:
        self.on_quit()
    
    def ev_keydown(self) -> None:
        # メモ: PyxelではESCAPEで終了となるため、Qに変更
        if pyxel.btnp(pyxel.KEY_Q):
            self.on_quit()
    

class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self) -> None:
        super().on_render()  # Draw the main state as the background.

        # Draw a frame with a custom banner title.
        color.rect(3, 3, (color.width - 6), (color.height - 6), color.dark_blue)
        color.rectb(3, 3, (color.width - 6), (color.height - 6), color.white)
        color.textcbg(3 + (color.width - 6) // 2, 3, "Message history",
                      color.white, color.dark_blue)
        
        # Render the message log using the cursor parameter.
        self.engine.message_log.render_messages(
            1+3, # メモ: 補正
            1+3, # メモ: 補正
            (color.width - 6) - 2,
            (color.height - 6) - 2,
            self.engine.message_log.messages[: self.cursor + 1],
        )

    def ev_keydown(self) -> Optional[MainGameEventHandler]:
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
        elif pyxel.btnp(pyxel.KEY_SPACE):  # Any other key moves back to the main game state.
                                           # メモ: SPACEキーで非表示に仕様変更
            return MainGameEventHandler(self.engine)

        # No valid key was pressed
        return None

class AskUserEventHandler(EventHandler):
    """Handles user input for actions which require special input."""
    def ev_keydown(self) -> Optional[ActionOrHandler]:
        
        """By default any key exits this input handler."""
        """メモ: SPACEキーで非表示に仕様変更"""
        if pyxel.btnp(pyxel.KEY_SPACE): 
            return self.on_exit()

        return None

    def ev_mousebuttondown(self) -> Optional[ActionOrHandler]:
        """By default any mouse click exits this input handler."""
        """メモ: マウス右ボタンで非表示に仕様変更"""
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            return self.on_exit()
        
        return None

    def on_exit(self) -> Optional[ActionOrHandler]:
        """Called when the user is trying to exit or cancel an action.

        By default this returns to the main event handler.
        """
        return MainGameEventHandler(self.engine)        

class CharacterScreenEventHandler(AskUserEventHandler):
    TITLE = "Character Information"

    def on_render(self) -> None:
        super().on_render()

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        y = 0

        width = len(self.TITLE) + 4

        color.rect(x, y, width, 7, color.dark_blue)
        color.rectb(x, y, width, 7, color.white)
        color.textcbg(x + width // 2, y, self.TITLE, color.white, color.dark_blue )

        color.text(
            x + 1, y + 1, f"Level: {self.engine.player.level.current_level}",
            color.white
        )
        color.text(
            x + 1, y + 2, f"XP: {self.engine.player.level.current_xp}",
            color.white
        )
        color.text(
            x + 1,
            y + 3,
            f"XP for next Level: {self.engine.player.level.experience_to_next_level}",
            color.white
        )

        color.text(
            x + 1, y + 4, f"Attack: {self.engine.player.fighter.power}",
            color.white
        )
        color.text(
            x + 1, y + 5, f"Defense: {self.engine.player.fighter.defense}",
            color.white
        )

class LevelUpEventHandler(AskUserEventHandler):
    TITLE = "Level Up"

    def on_render(self) -> None:
        super().on_render()

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        color.rect(x, 0, 35, 8, color.dark_blue)
        color.rectb(x, 0, 35, 8, color.white)
        color.textcbg(x + 35 // 2, 0, self.TITLE, color.white, color.dark_blue)

        color.text(x + 1, 1, "Congratulations! You level up!", color.white)
        color.text(x + 1, 2, "Select an attribute to increase.", color.white)
        
        color.text(
            x + 1,
            4,
            f"a) Constitution (+20 HP, from {self.engine.player.fighter.max_hp})",
            color.white,
        )
        color.text(
            x + 1,
            5,
            f"b) Strength (+1 attack, from {self.engine.player.fighter.power})",
            color.white,
        )
        color.text(
            x + 1,
            6,
            f"c) Agility (+1 defense, from {self.engine.player.fighter.defense})",
            color.white,
        )

    def ev_keydown(self) -> Optional[ActionOrHandler]:
        player = self.engine.player
        
        for key in ITEM_KEYS.keys():
            if pyxel.btnp(key):
                index = ITEM_KEYS[key]
        
                if 0 <= index <= 2:
                    if index == 0:
                        player.level.increase_max_hp()
                    elif index == 1:
                        player.level.increase_power()
                    else:
                        player.level.increase_defense()
                    # メモ: 1度選択したら、窓を閉じる(無限に選択できるのを防止)
                    return self.on_exit()
                else:
                    self.engine.message_log.add_message("Invalid entry.", color.invalid)
                    return None

        return super().ev_keydown()

    def ev_mousebuttondown(
        self
    ) -> Optional[ActionOrHandler]:
        """
        Don't allow the player to click to exit the menu, like normal.
        """
        return None
    
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

        color.rect(x, y, width, height, color.dark_blue)
        color.rectb(x, y, width, height, color.white)
        color.textcbg(x + width // 2, y, self.TITLE, color.white, color.dark_blue)

        if number_of_items_in_inventory > 0:
            for i, item in enumerate(self.engine.player.inventory.items):
                item_key = chr(ord("a") + i)

                is_equipped = self.engine.player.equipment.item_is_equipped(item)

                item_string = f"({item_key}) {item.name}"

                if is_equipped:
                    item_string = f"{item_string} (E)"

                color.text(x + 1, y + i + 1, item_string, color.white)
        else:
            color.text(x + 1, y + 1, "(Empty)", color.white)

    def ev_keydown(self) -> Optional[ActionOrHandler]:
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
                
        return super().ev_keydown()

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()

class InventoryActivateHandler(InventoryEventHandler):
    """Handle using an inventory item."""

    TITLE = "Select an item to use"

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        if item.consumable:
            # Return the action for the selected item.
            return item.consumable.get_action(self.engine.player)
        elif item.equippable:
            return actions.EquipAction(self.engine.player, item)
        else:
            return None

class InventoryDropHandler(InventoryEventHandler):
    """Handle dropping an inventory item."""

    TITLE = "Select an item to drop"

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Drop this item."""
        return actions.DropItem(self.engine.player, item)

class SelectIndexHandler(AskUserEventHandler):
    """Handles asking the user for an index on the map."""

    def __init__(self, engine: Engine):
        """Sets the cursor to the player when this handler is constructed."""
        super().__init__(engine)
        player = self.engine.player
        engine.mouse_location = player.x, player.y

    def on_render(self) -> None:
        """Highlight the tile under the cursor."""
        super().on_render()
        x, y = self.engine.mouse_location

        # メモ: マウスカーソルをハイライト(4x5ピクセルの矩形を表示)
        color.rect(x , y, 1, 1, color.black)
        color.rect(x , y, 1, 1, color.white)

    def ev_keydown(self) -> Optional[ActionOrHandler]:
        action: Optional[Action] = None

        """Check for key movement or confirmation keys."""
        for key in MOVE_KEYS.keys():
            if pyxel.btnp(key):
                modifier = 1  # Holding modifier keys will speed up key movement.

                if pyxel.btn(pyxel.KEY_LSHIFT) or pyxel.btn(pyxel.KEY_RSHIFT): 
                    modifier *= 5
                if pyxel.btn(pyxel.KEY_LCTRL) or pyxel.btn(pyxel.KEY_RCTRL): 
                    modifier *= 10
                if pyxel.btn(pyxel.KEY_LALT) or pyxel.btn(pyxel.KEY_RALT): 
                    modifier *= 20

                x, y = self.engine.mouse_location
                dx, dy = MOVE_KEYS[key]
                x += dx * modifier
                y += dy * modifier

                # Clamp the cursor index to the map size.
                x = max(0, min(x, self.engine.game_map.width - 1))
                y = max(0, min(y, self.engine.game_map.height - 1))
                self.engine.mouse_location = x, y
                return None

        # メモ: 確定キー
        for key in CONFIRM_KEYS:
            if pyxel.btnp(key):
                return self.on_index_selected(*self.engine.mouse_location)

        return super().ev_keydown()                

    def ev_mousebuttondown(self) -> Optional[ActionOrHandler]:
        # メモ: マウスイベント
        """Left click confirms a selection."""
        mouse_x = pyxel.mouse_x // color.chr_x
        mouse_y = pyxel.mouse_y // color.chr_y
        if self.engine.game_map.in_bounds(mouse_x, mouse_y):
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                return self.on_index_selected(mouse_x, mouse_y)
        return super().ev_mousebuttondown()

    def on_index_selected(self, x: int, y: int) -> Optional[ActionOrHandler]:
        """Called when an index is selected."""
        raise NotImplementedError()

class LookHandler(SelectIndexHandler):
    """Lets the player look around using the keyboard."""

    def on_index_selected(self, x: int, y: int) -> MainGameEventHandler:
        """Return to main handler."""
        return MainGameEventHandler(self.engine)        

class SingleRangedAttackHandler(SelectIndexHandler):
    """Handles targeting a single enemy. Only the enemy selected will be affected."""

    def __init__(
        self, engine: Engine, callback: Callable[[Tuple[int, int]], Optional[Action]]
    ):
        super().__init__(engine)

        self.callback = callback

    def on_index_selected(self, x: int, y: int) -> Optional[Action]:
        return self.callback((x, y))

class AreaRangedAttackHandler(SelectIndexHandler):
    """Handles targeting an area within a given radius. Any entity within the area will be affected."""

    def __init__(
        self,
        engine: Engine,
        radius: int,
        callback: Callable[[Tuple[int, int]], Optional[Action]],
    ):
        super().__init__(engine)

        self.radius = radius
        self.callback = callback

    def on_render(self) -> None:
        """Highlight the tile under the cursor."""
        super().on_render()

        x, y = self.engine.mouse_location

        # Draw a rectangle around the targeted area, so the player can see the affected tiles.
        color.rectb(
            x - self.radius - 1,
            y - self.radius - 1,
            self.radius ** 2,
            self.radius ** 2,
            color.red,
        )
        
    def on_index_selected(self, x: int, y: int) -> Optional[Action]:
        return self.callback((x, y))
    
# end of input_handlers.py    
