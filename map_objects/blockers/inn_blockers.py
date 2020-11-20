from abstracts.abstract_tile_component import AbstractTileBlocker
from config.image_objects import PILLAR_MID, PILLAR_TOP, PILLAR_BOT, WALL_MID, WALL_TOP_H, WALL_BOT, WALL_TOP_V


class PillarTileBlocker(AbstractTileBlocker):

    name = 'Pillar'
    opaque = True
    overshadow = [PILLAR_MID, PILLAR_TOP]

    def __init__(self):
        self.image = PILLAR_BOT


class HWallTileBlocker(AbstractTileBlocker):

    name = 'Wall'
    opaque = True
    overshadow = [WALL_MID, WALL_TOP_H]

    def __init__(self):
        self.image = WALL_BOT


class VWallTileBlocker(AbstractTileBlocker):

    name = 'Wall'
    opaque = True
    overshadow = None

    def __init__(self):
        self.image = WALL_TOP_V


def inn_blocker_array():
    pil = PillarTileBlocker()
    hw = HWallTileBlocker()
    vw = VWallTileBlocker()
    array = [[pil,  hw,   hw,   hw, None,   hw,   hw,  hw, pil],
             [vw, None, None, None, None, None, None, None, vw],
             [vw, None, None, None, None, None, None, None, vw],
             [vw, None, None, None, None, None, None, None, vw],
             [vw, None, None, None, None, None, None, None, vw],
             [vw, None, None, None, None, None, None, None, vw],
             [pil,  hw,   hw,   hw,   hw,   hw,   hw,  hw, pil]]
    return array


def inn_overhead_array():
    array = [[None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None]]
    return array
