import tcod as libtcod
from config.constants import FOV_RADIUS

def initialize_fov(game_map):
    fov_map = libtcod.map_new(game_map.width, game_map.height)
    
    for y in range(game_map.height):
        for x in range(game_map.width):
            libtcod.map_set_properties(fov_map, x, y, not game_map.tiles[x][y].block_sight, not game_map.tiles[x][y].blocked)
    
    return fov_map
    
def recompute_fov(fov_map, x, y):
    # Light wall = True, fov algorithm = 0
    libtcod.map_compute_fov(fov_map, x, y, FOV_RADIUS, True, 0)
    