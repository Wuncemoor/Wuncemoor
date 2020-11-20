from abstracts.abstract_tile_component import AbstractTileBlocker, AbstractTileOverhead
from config.image_objects import EXT_LEFT_EDGE_TOP, EXT_LEFT_EDGE_BOT, EXT_EXTEND_BOT, EXT_EXTEND_TOP, \
    EXT_LEFT_DOORFRAME_TOP, EXT_LEFT_DOORFRAME_BOT, EXT_RIGHT_EDGE_BOT, EXT_WINDOW_RIGHT_BOT, EXT_WINDOW_LEFT_BOT, \
    EXT_RIGHT_DOORFRAME_BOT, EXT_RIGHT_DOORFRAME_TOP, EXT_WINDOW_LEFT_TOP, EXT_WINDOW_RIGHT_TOP, EXT_RIGHT_EDGE_TOP, \
    BLUE_ROOF_LEFT, EXT_LEFT_WALL, BLUE_ROOF_RIGHT, EXT_RIGHT_WALL, BLUE_ROOF_FRONT_LEFT_CONNECT, \
    BLUE_ROOF_BACK_LEFT_CONNECT, BLUE_ROOF_FRONT_MID_CONNECT, BLUE_ROOF_BACK_MID_CONNECT, BLUE_ROOF_FRONT_RIGHT_CONNECT, \
    BLUE_ROOF_BACK_RIGHT_CONNECT, BLUE_ROOF_FRONT_LEFT_PEAK, BLUE_ROOF_BACK_LEFT_PEAK, BLUE_ROOF_FRONT_RIGHT_PEAK, \
    BLUE_ROOF_BACK_RIGHT_PEAK, EXT_DOORWAY_TOP, BLUE_ROOF_MID, BLUE_ROOF_FRONT_MID_PEAK, BLUE_ROOF_BACK_MID_PEAK


class MageHouseTileBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True

    def __init__(self, image):
        super().__init__(image)


class MageHouseWallTileOverhead(AbstractTileOverhead):

    name = 'Wooden Wall'

    def __init__(self, distance_overhead, image):
        super().__init__(distance_overhead, image)


class MageHouseRoofTileOverhead(AbstractTileOverhead):

    name = 'Blue Roof'

    def __init__(self, distance_overhead, image):
        super().__init__(distance_overhead, image)


def mage_house_blocker_array():
    fl = MageHouseTileBlocker(EXT_LEFT_EDGE_BOT)
    bl = MageHouseTileBlocker(EXT_LEFT_EDGE_BOT)
    fe = MageHouseTileBlocker(EXT_EXTEND_BOT)
    be = MageHouseTileBlocker(EXT_EXTEND_BOT)
    fldf = MageHouseTileBlocker(EXT_LEFT_DOORFRAME_BOT)
    frdf = MageHouseTileBlocker(EXT_RIGHT_DOORFRAME_BOT)
    bldf = MageHouseTileBlocker(EXT_LEFT_DOORFRAME_BOT)
    brdf = MageHouseTileBlocker(EXT_RIGHT_DOORFRAME_BOT)
    flw = MageHouseTileBlocker(EXT_WINDOW_LEFT_BOT)
    frw = MageHouseTileBlocker(EXT_WINDOW_RIGHT_BOT)
    blw = MageHouseTileBlocker(EXT_WINDOW_LEFT_BOT)
    brw = MageHouseTileBlocker(EXT_WINDOW_RIGHT_BOT)
    fr = MageHouseTileBlocker(EXT_RIGHT_EDGE_BOT)
    br = MageHouseTileBlocker(EXT_RIGHT_EDGE_BOT)
    lw1 = MageHouseTileBlocker(EXT_LEFT_WALL)
    lw2 = MageHouseTileBlocker(EXT_LEFT_WALL)
    lw3 = MageHouseTileBlocker(EXT_LEFT_WALL)
    lw4 = MageHouseTileBlocker(EXT_LEFT_WALL)
    rw1 = MageHouseTileBlocker(EXT_RIGHT_WALL)
    rw2 = MageHouseTileBlocker(EXT_RIGHT_WALL)
    rw3 = MageHouseTileBlocker(EXT_RIGHT_WALL)
    rw4 = MageHouseTileBlocker(EXT_RIGHT_WALL)

    array = [[bl,    be,  bldf, None,  brdf,   blw,   brw, br],
             [lw4, None, None, None, None, None, None, rw4],
             [lw3, None, None, None, None, None, None, rw3],
             [lw2, None, None, None, None, None, None, rw2],
             [lw1, None, None, None, None, None, None, rw1],
             [fl,    fe,  fldf, None,  frdf,   flw,  frw, fr]]
    return array


def mage_house_overhead_array():

    fl = [MageHouseWallTileOverhead(1, EXT_LEFT_EDGE_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_LEFT_CONNECT)]
    bl = [MageHouseWallTileOverhead(1, EXT_LEFT_EDGE_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_LEFT_CONNECT)]
    fe = [MageHouseWallTileOverhead(1, EXT_EXTEND_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_CONNECT)]
    be = [MageHouseWallTileOverhead(1, EXT_EXTEND_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_CONNECT)]
    fldf = [MageHouseWallTileOverhead(1, EXT_LEFT_DOORFRAME_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_CONNECT)]
    frdf = [MageHouseWallTileOverhead(1, EXT_RIGHT_DOORFRAME_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_CONNECT)]
    fdw = [MageHouseWallTileOverhead(1, EXT_DOORWAY_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_CONNECT)]
    bldf = [MageHouseWallTileOverhead(1, EXT_LEFT_DOORFRAME_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_CONNECT)]
    brdf = [MageHouseWallTileOverhead(1, EXT_RIGHT_DOORFRAME_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_CONNECT)]
    bdw = [MageHouseWallTileOverhead(1, EXT_DOORWAY_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_CONNECT)]
    flw = [MageHouseWallTileOverhead(1,EXT_WINDOW_LEFT_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_CONNECT)]
    frw = [MageHouseWallTileOverhead(1, EXT_WINDOW_RIGHT_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_CONNECT)]
    blw = [MageHouseWallTileOverhead(1,EXT_WINDOW_LEFT_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_CONNECT)]
    brw = [MageHouseWallTileOverhead(1, EXT_WINDOW_RIGHT_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_CONNECT)]
    fr = [MageHouseWallTileOverhead(1, EXT_RIGHT_EDGE_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_RIGHT_CONNECT)]
    br = [MageHouseWallTileOverhead(1, EXT_RIGHT_EDGE_TOP), MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_RIGHT_CONNECT)]
    lw1 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_LEFT)]
    lw2 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_LEFT)]
    lw3 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_LEFT_PEAK)]
    lw4 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_LEFT_PEAK)]
    rw1 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_RIGHT)]
    rw2 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_RIGHT)]
    rw3 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_RIGHT_PEAK)]
    rw4 = [MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_RIGHT_PEAK)]
    roof = [MageHouseRoofTileOverhead(2, BLUE_ROOF_MID)]
    rfm = [MageHouseRoofTileOverhead(2, BLUE_ROOF_FRONT_MID_PEAK)]
    rbm = [MageHouseRoofTileOverhead(2, BLUE_ROOF_BACK_MID_PEAK)]

    array = [[bl,    be,  bldf, bdw,  brdf,   blw,   brw, br],
             [lw4,  rbm,  rbm,  rbm,  rbm,  rbm,  rbm, rw4],
             [lw3,  rfm,  rfm,  rfm,  rfm,  rfm,  rfm, rw3],
             [lw2, roof, roof, roof, roof, roof, roof, rw2],
             [lw1, roof, roof, roof, roof, roof, roof, rw1],
             [fl,    fe,  fldf, fdw,  frdf,   flw,  frw, fr]]
    return array