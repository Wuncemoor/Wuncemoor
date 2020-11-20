from abstracts.abstract_tile import AbstractTile
from abstracts.abstract_tile_component import AbstractTileFloor
from map_objects.floors.outside_floors import GrassTileFloor, DirtTileFloor


class FakeTileFloor(AbstractTileFloor):
    """A fake TileFloor for a fake Tile. Used for Structure creation, before integration with a real Map"""

    def __init__(self):
        super().__init__()
        self.name = None

    name = 'Fake'


class FakeTile(AbstractTile):
    """A fake Tile with reduced functionality. Used for Structure creation, before integration with a real Map"""

    def __init__(self):
        super().__init__()

    def initialize_floor(self):
        return FakeTileFloor()

    def initialize_blocker(self):
        return None


class Tile(AbstractTile):
    """
    Map tile. It may or may not be blocked, and may or may not block sight.
    On the world map, type is the biome and subtype is the closest exuding Node. (Ex. Rainforest near a goblin cave.)
    Otherwise, type is the location and subtype is the unique infestation. (Ex. Cave infested with goblins.)
    Node power increases risk/reward
    """
    def __init__(self, variant):
        self.floor = self.initialize_floor(variant)
        self.decoration = None
        self.blocker = self.initialize_blocker(variant)
        self.overhead = None
        self.is_interior = False
        self.explored = False
        self.type = None
        self.subtype = None
        self.np = 0

    def initialize_floor(self, variant):
        if variant in ('alpha', 'beta', 'gamma', 'delta'):
            base = GrassTileFloor()
        elif variant == 'cave':
            base = DirtTileFloor()
        else:
            base = None
        return base

    def initialize_blocker(self, variant):
        return None
