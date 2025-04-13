from typing import Optional

import tcod.event
import pyxel

from actions import Action, BumpAction, EscapeAction

class EventHandler:
    def dispatch(self) -> Optional[Action]:
        # メモ: 何も押されていない場合はNoneを返却
        action = None
        
        if pyxel.btnp(pyxel.KEY_UP):
            #action = MovementAction(dx=0, dy=-1)
            action = BumpAction(dx=0, dy=-1)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            #action = MovementAction(dx=0, dy=1)
            action = BumpAction(dx=0, dy=1)
        elif pyxel.btnp(pyxel.KEY_LEFT):
            #action = MovementAction(dx=-1, dy=0)
            action = BumpAction(dx=-1, dy=0)
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            #action = MovementAction(dx=1, dy=0)
            action = BumpAction(dx=1, dy=0)
            
        elif pyxel.btnp(pyxel.KEY_ESCAPE):
            action = EscapeAction()

        # No valid key was pressed
        return action

# end of input_handlers.py    
