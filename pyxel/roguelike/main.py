import pyxel

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
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
    
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", 7)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", 10)
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )
    
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    
    pyxel.init(
        screen_width,
        screen_height,
        title="Yet Another Roguelike Tutorial",
        fps=30
    )
    pyxel.run(update, draw)
    
def update():
    # メモ: イベントハンドラ(キー操作)を呼ぶ
    global engine
    engine.handle_events()

def draw():
    # メモ: 画面描画ルーチンを呼ぶ
    global engine
    engine.render()
    
if __name__ == "__main__":
    main()

# end of main.py    
