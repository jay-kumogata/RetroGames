import pyxel

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    global player_x, player_y, event_handler

    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    event_handler = EventHandler()

    pyxel.init(
        screen_width,
        screen_height,
        title="Yet Another Roguelike Tutorial",
        fps=30
    )
    pyxel.run(update, draw)

def update():
    global player_x, player_y, event_handler

    action = event_handler.dispatch()

    if action is None:
        return

    if isinstance(action, MovementAction):
        player_x += action.dx
        player_y += action.dy

    elif isinstance(action, MovementAction):
        raise SystemExit()

def draw():
    pyxel.cls(1)
    pyxel.pset(player_x,player_y,7)
    
if __name__ == "__main__":
    main()
