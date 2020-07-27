from ECS.__entity.floor import GrassTileFloor, DirtTileFloor
from ECS.__entity.blocker import RockTileBlocker
from config.constants import IMAGE_OPTIONS
from random import randint

from config.image_objects import LIGHT_GRASS, DARK_GRASS, LIGHT_DIRT, DARK_DIRT, LIGHT_ROCK_WALL, DARK_ROCK_WALL


class Tile:
    """
    Map tile. It may or may not be blocked, and may or may not block sight.
    On the world map, type is the biome and subtype is the closest exuding Node. (Ex. Rainforest near a goblin cave.)
    Otherwise, type is the location and subtype is the unique infestation. (Ex. Cave infested with goblins.)
    Mode changes tile appearance based on neighboring nodes. (Ex. Different road pieces)
    Node power increases risk/reward
    """
    def __init__(self, variant):
        self.base = self.initialize_base(variant)
        self.blocker = self.initialize_blocker(variant)
        self.block_sight = self.initialize_block_sight()
        self.explored = False
        self.type = None
        self.subtype = None
        self.mode = None
        self.np = 0
        self.image = None
        # Temporary dark image until fov shader implemented
        self.image2 = None
        # Temp holder for images that appear overworld entities
        self.image_air = None

    def initialize_base(self, variant):
        if variant == 'town':
            base = GrassTileFloor()
        elif variant == 'cave':
            base = DirtTileFloor()
        elif variant == 'overworld':
            base = None
        return base

    def initialize_blocker(self, variant):
        if variant in ('town', 'overworld'):
            return None
        if variant == 'cave':
            return RockTileBlocker()

    def initialize_block_sight(self):
        if self.blocker is None:
            return False
        else:
            return self.blocker.opaque

    def clear_blocker(self):
        self.blocker = None


