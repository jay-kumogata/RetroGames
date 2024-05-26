import traceback

import pyxel

import color
import exceptions
import input_handlers
import setup_game


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")

def main() -> None:
    global engine, handler
    
    screen_width = 80
    screen_height = 50

    # メモ: "SyntaxError: annotated name 'handler' can't be global"発生(言語仕様)
    #handler = input_handlers.MainGameEventHandler(engine)
    handler = setup_game.MainMenu()
    
    # メモ: 初期化(Pyxel)
    pyxel.init(
        screen_width * color.chr_x,
        screen_height * color.chr_y,
        title="Yet Another Roguelike Tutorial",
        fps=30
    )
    
    pyxel.mouse(True) # メモ: マウスを表示

    # メモ: 背景画像読み込み
    # Load the background image and remove the alpha channel.
    pyxel.images[0].load(0, 0, "menu_background.png") 
    pyxel.run(update, draw)
    
def draw():
    global engine, handler

    try:
        #メモ: オリジナルでは無限ループを構成(Pyxelではライブラリで実装)
        #while True:
        
        # メモ: 画面描画処理を呼ぶ
        pyxel.cls(0)
        handler.on_render()

        # メモ: イベントハンドラを呼ぶ
        try:
            handler = handler.handle_events()
        except Exception:  # Handle exceptions in game.
            traceback.print_exc()  # Print error to stderr.
            # Then print the error to the message log.
            if isinstance(handler, input_handlers.EventHandler):
                handler.engine.message_log.add_message(
                    traceback.format_exc(), color.error
                )

    except exceptions.QuitWithoutSaving:
        raise
    except SystemExit:  # Save and quit.
        save_game(handler, "savegame.sav")
        raise
    except BaseException:  # Save on any other unexpected exception.
        save_game(handler, "savegame.sav")
        raise

def update():
    global engine, handler
    # メモ: 更新処理(update())に記載すべき事項も、描画処理(draw())に統合
    
if __name__ == "__main__":
    main()

# end of main.py
