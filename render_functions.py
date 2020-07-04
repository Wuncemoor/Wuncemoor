import tcod as libtcod
import pygame


def get_names_under_mouse(entities, fov_map):
    (x, y) = pygame.mouse.get_pos()

    names = [entity.name for entity in entities if
             entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()


