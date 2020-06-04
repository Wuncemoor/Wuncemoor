
class GameMap:

    def __init__(self, current_map):
        self.current_map = current_map

    @property
    def width(self):
        return self.current_map.width

    @property
    def height(self):
        return self.current_map.height

    @property
    def tiles(self):
        return self.current_map.tiles

    @property
    def variant(self):
        return self.current_map.variant

    @property
    def dungeon_level(self):
        return self.current_map.dungeon_level

    @property
    def dangerous(self):
        return self.current_map.dangerous

    def is_blocked(self, x, y):
        if self.current_map.tiles[x][y].blocked:
            return True

        return False

    def set_current_map(self, new_map):
        self.current_map = new_map
