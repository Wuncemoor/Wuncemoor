import tcod
from config.constants import FOV_RADIUS


class FovHandler:
    def __init__(self):
        self.map = None
        self.needs_recompute = True

    @staticmethod
    def initialize(game_map):
        fov_map = tcod.map_new(game_map.height, game_map.width)

        for y in range(game_map.height):
            for x in range(game_map.width):
                tcod.map_set_properties(fov_map, y, x, not game_map.tiles[y][x].block_sight,
                                           not game_map.tiles[y][x].blocker)
        return fov_map

    def recompute(self):
        x, y, = self.owner.owner.party.x, self.owner.owner.party.y
        # Light wall = True, fov algorithm = 0
        tcod.map_compute_fov(self.map, y, x, FOV_RADIUS, True, 0)
