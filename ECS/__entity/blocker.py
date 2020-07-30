from abstracts.abstract_tile_component import AbstractTileBlocker
from config.image_objects import LIGHT_ROCK_WALL, DARK_ROCK_WALL


class RockTileBlocker(AbstractTileBlocker):

    name = 'Rock Wall'
    image = LIGHT_ROCK_WALL
    image2 = DARK_ROCK_WALL
    opaque = False
