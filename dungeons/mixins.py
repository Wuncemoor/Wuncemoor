from map_objects.dungeon_maps import DangerousMap, SafeMap


class InitDangerousMap:

    def initialize_map(self):
        map = DangerousMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map


class InitSafeMap:

    def initialize_map(self):
        map = SafeMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map
