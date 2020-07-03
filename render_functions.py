import tcod as libtcod
import pygame
from config.image_objects import TILE_BASE


def get_names_under_mouse(entities, fov_map):
    (x, y) = pygame.mouse.get_pos()

    names = [entity.name for entity in entities if
             entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()


def draw_entity(camera_surface, cx, cy, entity, fov_map, game_map, tilesize):

    surfimg = entity.images.sprite

    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y) or (
            entity.transition and game_map.tiles[entity.x][entity.y].explored):
        camera_surface.blit(surfimg, ((entity.x - cx) * tilesize, (entity.y - cy) * tilesize))


def draw_structure(camera_surface, cx, cy, structure, fov_map, game_map, tilesize):

    count = 0
    for j in range(structure.rect.y1, structure.rect.y2):
        for i in range(structure.rect.x1, structure.rect.x2):
            visible = libtcod.map_is_in_fov(fov_map, i, j)
            if visible:
                camera_surface.blit(structure.file_objs[0][count], ((i - cx) * tilesize, (j - cy) * tilesize))
                count += 1
            elif game_map.tiles[i][j].explored:
                camera_surface.blit(structure.file_objs[1][count], ((i - cx) * tilesize, (j - cy) * tilesize))
                count += 1
            else:
                camera_surface.blit(TILE_BASE.get('black'), ((i - cx) * tilesize, (j - cy) * tilesize))
                count += 1


def draw_tile(camera_surface, fov_map, game_map, x, y, cx, cy, tilesize):

    visible = libtcod.map_is_in_fov(fov_map, cx + x, cy + y)

    tile = game_map.tiles[cx + x][cy + y]

    if visible:
        camera_surface.blit(tile.image, (x * tilesize, y * tilesize))
        tile.explored = True
    elif tile.explored:
       camera_surface.blit(tile.image2, (x * tilesize, y * tilesize))
    else:
        camera_surface.blit(TILE_BASE.get('black'), (x * tilesize, y * tilesize))

