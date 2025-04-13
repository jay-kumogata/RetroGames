import copy
import traceback

import pyxel

import color
from engine import Engine
import entity_factories
from procgen import generate_dungeon

def main() -> None:
    global engine
    
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 2
    max_items_per_room = 2
    
    player = copy.deepcopy(entity_factories.player)    
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,        
        engine=engine,        
    )
    engine.update_fov()    

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
    )
    
    # Pyxel初期化
    pyxel.init(
        screen_width * color.chr_x,
        screen_height * color.chr_y,
        title="Yet Another Roguelike Tutorial",
        fps=30
    )
    pyxel.mouse(True) # メモ: マウスを表示
    pyxel.run(update, draw)
    
def draw():
    # メモ: 画面描画ルーチンを呼ぶ
    global engine
    pyxel.cls(0)
    engine.event_handler.on_render()

def update():
    # メモ: イベントハンドラを呼ぶ
    global engine

    try:
        engine.event_handler.handle_events()
    except Exception:  # Handle exceptions in game.
        traceback.print_exc()  # Print error to stderr.
        # Then print the error to the message log.
        engine.message_log.add_message(traceback.format_exc(), color.error)    

if __name__ == "__main__":
    main()

# end of main.py
