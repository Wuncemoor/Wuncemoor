class Tile:
    """
    Map tile. It may or may not be blocked, and may or may not block sight.
    On the world map, type is the biome and subtype is the closest exuding Node. (Ex. Rainforest near a goblin cave.)
    Otherwise, type is the location and subtype is the unique infestation. (Ex. Cave infested with goblins.)
    Mode changes tile appearance based on neighboring nodes. (Ex. Different road pieces)
    Node power increases risk/reward
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        
        #By default, if a tile is blocked, it also blocks sight.
        if block_sight is None:
            block_sight = blocked
            
        self.block_sight = block_sight
        self.explored = False
        self.type = None
        self.subtype = None
        self.mode = None
        self.np = 0
        