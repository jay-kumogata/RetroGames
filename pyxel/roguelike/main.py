import pyxel

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main() -> None:
    global engine
    
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 50
    
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", 7)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", 10)
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)
    
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    
    pyxel.init(
        screen_width,
        screen_height,
        title="Yet Another Roguelike Tutorial",
        fps=30
    )
    pyxel.run(update, draw)

def update():
    global engine
    engine.handle_events()

def draw():
    global engine
    engine.render()
    
if __name__ == "__main__":
    main()

# end of main.py    
