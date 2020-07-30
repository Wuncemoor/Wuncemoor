from abstracts.abstract_tile_component import TileBlocker
from config.image_objects import LIGHT_ROCK_WALL, DARK_ROCK_WALL


class RockTileBlocker(TileBlocker):

    name = 'Rock Wall'
    image = LIGHT_ROCK_WALL
    image2 = DARK_ROCK_WALL
    opaque = False
