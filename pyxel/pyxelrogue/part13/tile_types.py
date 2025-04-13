from typing import Tuple

import numpy as np  # type: ignore
import color

# Tile graphics structured type 
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.(未使用: キャラクタコード)
        ("fg", np.int32),  # 文字色(Pyxelでの色情報)
        ("bg", np.int32),  # 背景色(Pyxelでの色情報)
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool_),  # True if this tile can be walked over.
        ("transparent", np.bool_),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, int, int],
    light: Tuple[int, int, int]
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), color.white, color.black), dtype=graphic_dt)

# メモ: 床と壁において，光が当たっていない場合(dark)と当たっている場合(light)の情報
floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), color.white, color.light_blue),
    light=(ord(" "), color.white, color.yellow),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), color.white, color.dark_blue),
    light=(ord(" "), color.white, color.amber),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), color.dark_blue, color.blue),
    light=(ord(">"), color.white, color.yellow),
)

# end of tile_types.py
