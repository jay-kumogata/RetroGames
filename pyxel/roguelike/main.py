import copy

import pyxel

from engine import Engine
import entity_factories
from procgen import generate_dungeon

def main() -> None:
    global engine
    
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 2

    player = copy.deepcopy(entity_factories.player)    
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,        
    )
    engine.update_fov()    
    
    
    # Pyxel初期化
    pyxel.init(
        screen_width,
        screen_height,
        title="Yet Another Roguelike Tutorial",
        fps=30
    )
    pyxel.run(update, draw)
    
def update():
    # メモ: イベントハンドラを呼ぶ
    global engine
    engine.event_handler.handle_events()

def draw():
    # メモ: 画面描画ルーチンを呼ぶ
    global engine
    engine.render()
    
if __name__ == "__main__":
    main()

# end of main.py
