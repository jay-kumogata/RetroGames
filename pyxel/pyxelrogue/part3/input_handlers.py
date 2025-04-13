from typing import Optional
import pyxel
from actions import Action, EscapeAction, MovementAction

class EventHandler:
    def dispatch(self) -> Optional[Action]:
        action = None
        
        if pyxel.btnp(pyxel.KEY_UP):
            action = MovementAction(dx=0, dy=-1)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            action = MovementAction(dx=0, dy=1)
        elif pyxel.btnp(pyxel.KEY_LEFT):
            action = MovementAction(dx=-1, dy=0)
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            action = MovementAction(dx=1, dy=0)

        elif pyxel.btnp(pyxel.KEY_ESCAPE):
            action = EscapeAction()

        # No valid key was pressed
        return action

# end of input_handlers.py    
