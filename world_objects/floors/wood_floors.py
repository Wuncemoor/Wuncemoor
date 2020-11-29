from abstracts.abstract_tile_component import AbstractTileFloor


class WoodPlankTileFloor(AbstractTileFloor):

    name = 'Wooden Floor'

    def __init__(self, image):
        super().__init__()
        self.image = image
