from abstracts.abstract_tile_component import AbstractTileOverhead


class WoodenWallOverhead(AbstractTileOverhead):

    name = 'Wooden Wall'

    def __init__(self, distance_overhead, image):
        super().__init__(distance_overhead, image)


class RoofOverhead(AbstractTileOverhead):

    name = 'Roof'

    def __init__(self, distance_overhead, image):
        super().__init__(distance_overhead, image)