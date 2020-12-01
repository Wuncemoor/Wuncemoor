from abstracts.abstract_tile_component import AbstractTileBlocker


class WoodenWallTileBlocker(AbstractTileBlocker):

    name = 'Wooden Wall'
    opaque = True

    def __init__(self, image, int_image=None):
        super().__init__(image, int_image)