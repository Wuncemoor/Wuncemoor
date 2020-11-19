from abstracts.abstract_tile_component import AbstractTileBlocker
from config.image_objects import EXT_LEFT_EDGE_TOP, BLUE_ROOF_LEFT_CONNECT, EXT_LEFT_EDGE_BOT, EXT_EXTEND_BOT, \
    EXT_EXTEND_TOP, BLUE_ROOF_MID_CONNECT, EXT_LEFT_DOORFRAME_TOP, EXT_LEFT_DOORFRAME_BOT, EXT_RIGHT_EDGE_BOT, \
    EXT_WINDOW_RIGHT_BOT, EXT_WINDOW_LEFT_BOT, EXT_RIGHT_DOORFRAME_BOT


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
    overshadow = None

    def __init__(self):
        self.image = EXT_RIGHT_DOORFRAME_BOT


class MageHouseWindowLeftTileBLocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = None

    def __init__(self):
        self.image = EXT_WINDOW_LEFT_BOT


class MageHouseWindowRightTileBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = None

    def __init__(self):
        self.image = EXT_WINDOW_RIGHT_BOT


class MageHouseBotRightWallBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True
    overshadow = None

    def __init__(self):
        self.image = EXT_RIGHT_EDGE_BOT


def mage_house_blocker_array():
    bl = MageHouseBotLeftWallBlocker()
    e = MageHouseExtendWallBlocker()
    ldf = MageHouseLeftDoorframeWallBlocker()
    rdf = MageHouseRightDoorframeWallBlocker()
    lw = MageHouseWindowLeftTileBLocker()
    rw = MageHouseWindowRightTileBlocker()
    br = MageHouseBotRightWallBlocker()
    array = [[bl, e, ldf, None, rdf, lw, rw, br],
             [bl, None, None, None, None, None, None, br],
             [bl, None, None, None, None, None, None, br],
             [bl, None, None, None, None, None, None, br],
             [bl, None, None, None, None, None, None, br],
             [bl, e, ldf, None, rdf, lw, rw, br]]
    return array