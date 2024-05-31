"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import copy
import lzma
import pickle
import traceback
from typing import Optional

import tcod
import pyxel

import color
from engine import Engine
import entity_factories
from game_map import GameWorld
import input_handlers


def new_game() -> Engine:

    """Return a brand new game session as an Engine instance."""
    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_world = GameWorld(
        engine=engine,
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
    )

    engine.game_world.generate_floor()    
    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
    )
    return engine

def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine


class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self) -> None:
        """Render the main menu on a background image."""
        pyxel.blt(80, 75, 0, 0, 0, 160, 100)

        color.textc(
            color.width // 2,
            color.height // 2 - 4,
            "TOMBS OF THE ANCIENT KINGS",
            color.menu_title,
        )
            
        color.textc(
            color.width // 2,
            color.height - 2,
            "By Kumogata Jay",
            color.menu_title,
        )

        menu_width = 24
        for i, text in enumerate(
            ["[N] Play a new game", "[C] Continue last game", "[Q] Quit"]
        ):
            color.textc(
                color.width // 2,
                color.height // 2 - 2 + i,
                text.ljust(menu_width),
                color.menu_text,
            )            

    def ev_keydown(
        self
    ) -> Optional[input_handlers.BaseEventHandler]:
        # メモ: PyxelではESCAPEで終了となるため、Qに変更
        if pyxel.btnp(pyxel.KEY_Q): 
            raise SystemExit()
        elif pyxel.btnp(pyxel.KEY_C):
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
        elif pyxel.btnp(pyxel.KEY_N):
            return input_handlers.MainGameEventHandler(new_game())

        return None

# end of setup_game.py    
