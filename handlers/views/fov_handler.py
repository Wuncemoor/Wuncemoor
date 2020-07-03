import tcod
from config.constants import FOV_RADIUS


class FovHandler:
    def __init__(self):
        self.map = None
        self.recompute = True

    @staticmethod
    def initialize_fov(game_map):
        fov_map = tcod.map_new(game_map.width, game_map.height)

        for y in range(game_map.height):
            for x in range(game_map.width):
                tcod.map_set_properties(fov_map, x, y, not game_map.tiles[x][y].block_sight,
                                           not game_map.tiles[x][y].blocked)
        return fov_map

    @staticmethod
    def recompute_fov(fov_map, x, y):
        # Light wall = True, fov algorithm = 0
        tcod.map_compute_fov(fov_map, x, y, FOV_RADIUS, True, 0)