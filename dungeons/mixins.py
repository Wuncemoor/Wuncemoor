from map_objects.dungeon_maps import DangerousMap, SafeMap


class InitDangerousMap:
    """Adds functionality to a DungeonBuilder via multiple inheritance"""

    def initialize_map(self):
        map = DangerousMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map


class InitSafeMap:
    """Adds functionality to a DungeonBuilder via multiple inheritance"""

    def initialize_map(self):
        map = SafeMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map
