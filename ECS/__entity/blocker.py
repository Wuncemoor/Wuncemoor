from abstracts.abstract_tile_component import AbstractTileBlocker


class RockTileBlocker(AbstractTileBlocker):
    """Rock wall for a cave"""

    name = 'Rock Wall'
    image = None
    image2 = None
    opaque = True
