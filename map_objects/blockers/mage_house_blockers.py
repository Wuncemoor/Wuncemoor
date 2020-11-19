from abstracts.abstract_tile_component import AbstractTileBlocker
from config.image_objects import EXT_LEFT_EDGE_TOP, BLUE_ROOF_LEFT_CONNECT, EXT_LEFT_EDGE_BOT, EXT_EXTEND_BOT, \
    EXT_EXTEND_TOP, BLUE_ROOF_MID_CONNECT, EXT_LEFT_DOORFRAME_TOP, EXT_LEFT_DOORFRAME_BOT, EXT_RIGHT_EDGE_BOT, \
    EXT_WINDOW_RIGHT_BOT, EXT_WINDOW_LEFT_BOT, EXT_RIGHT_DOORFRAME_BOT, EXT_RIGHT_DOORFRAME_TOP, EXT_WINDOW_LEFT_TOP, \
    EXT_WINDOW_RIGHT_TOP, EXT_RIGHT_EDGE_TOP, BLUE_ROOF_RIGHT_CONNECT, BLUE_ROOF_LEFT, EXT_LEFT_WALL, BLUE_ROOF_RIGHT, \
    EXT_RIGHT_WALL


class MageHouseBotLeftWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_LEFT_EDGE_TOP, BLUE_ROOF_LEFT_CONNECT]

    def __init__(self):
        self.image = EXT_LEFT_EDGE_BOT


class MageHouseExtendWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_EXTEND_TOP, BLUE_ROOF_MID_CONNECT]

    def __init__(self):
        self.image = EXT_EXTEND_BOT


class MageHouseLeftDoorframeWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_LEFT_DOORFRAME_TOP, BLUE_ROOF_MID_CONNECT]

    def __init__(self):
        self.image = EXT_LEFT_DOORFRAME_BOT


class MageHouseRightDoorframeWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_RIGHT_DOORFRAME_TOP, BLUE_ROOF_MID_CONNECT]

    def __init__(self):
        self.image = EXT_RIGHT_DOORFRAME_BOT


class MageHouseWindowLeftTileBLocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_WINDOW_LEFT_TOP, BLUE_ROOF_MID_CONNECT]

    def __init__(self):
        self.image = EXT_WINDOW_LEFT_BOT


class MageHouseWindowRightTileBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_WINDOW_RIGHT_TOP, BLUE_ROOF_MID_CONNECT]

    def __init__(self):
        self.image = EXT_WINDOW_RIGHT_BOT


class MageHouseBotRightWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [EXT_RIGHT_EDGE_TOP, BLUE_ROOF_RIGHT_CONNECT]

    def __init__(self):
        self.image = EXT_RIGHT_EDGE_BOT


class MageHouseLeftWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [None, BLUE_ROOF_LEFT]

    def __init__(self):
        self.image = EXT_LEFT_WALL


class MageHouseRightWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = [None, BLUE_ROOF_RIGHT]

    def __init__(self):
        self.image = EXT_RIGHT_WALL


def mage_house_blocker_array():
    bl = MageHouseBotLeftWallBlocker()
    e = MageHouseExtendWallBlocker()
    ldf = MageHouseLeftDoorframeWallBlocker()
    rdf = MageHouseRightDoorframeWallBlocker()
    lw = MageHouseWindowLeftTileBLocker()
    rw = MageHouseWindowRightTileBlocker()
    br = MageHouseBotRightWallBlocker()
    lwb = MageHouseLeftWallBlocker()
    rwb = MageHouseRightWallBlocker()
    array = [[bl,    e,  ldf, None,  rdf,   lw,   rw, br],
             [lwb, None, None, None, None, None, None, rwb],
             [lwb, None, None, None, None, None, None, rwb],
             [lwb, None, None, None, None, None, None, rwb],
             [lwb, None, None, None, None, None, None, rwb],
             [bl,    e,  ldf, None,  rdf,   lw,   rw, br]]
    return array