from map_objects.dungeon_maps import DangerousMap, SafeMap
from map_objects.tile import Tile


class DangerousMapMixin:

    def initialize_map(self):
        map = DangerousMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map


class SafeMapMixin:

    def initialize_map(self):
        map = SafeMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map
