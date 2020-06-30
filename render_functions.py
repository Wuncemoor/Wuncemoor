import tcod as libtcod
import pygame
from enums.game_states import GameStates, MenuStates
from menus import inventory_menu, level_up_menu
from screens.mini_map import minimap_screen
from screens.dialogue_screen import dialogue_screen
from screens.encounter_screen import encounter_screen
from screens.gui_tools import print_message
from screens.resources_HUD import player_resource_display
from screens.loot_screen import loot_screen
from screens.character_screen import character_screen
from screens.journal_screen import journal_screen
from screens.calendar import display_calendar
from config.image_objects import MESSAGE_BG, TILE_BASE
from config.constants import TILES_ON_SCREEN


def get_names_under_mouse(entities, fov_map):
    (x, y) = pygame.mouse.get_pos()

    names = [entity.name for entity in entities if
             entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()


def render_all(screen, camera_surface, message_surface, entities, player, structures, transitions,
               noncombatants, game_map, world_map, camera, fov_map, fov_recompute, message_log,
               game_state, menu_handler, time_handler, encounter, loot, dialogue):
    (width, height) = TILES_ON_SCREEN


    tilesize = 16
    # Draw tiles near player
    if fov_recompute:
        for y in range(height):
            for x in range(width):
                draw_tile(camera_surface, fov_map, game_map, x, y, camera.x, camera.y, tilesize)

    for structure in structures:
        draw_structure(camera_surface, camera.x, camera.y, structure, fov_map, game_map, tilesize)
    for transition in transitions:
        draw_entity(camera_surface, camera.x, camera.y, transition, fov_map, game_map, tilesize)
    for noncom in noncombatants:
        draw_entity(camera_surface, camera.x, camera.y, noncom, fov_map, game_map, tilesize)
    # draw all entities in list
    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)
    for entity in entities_in_render_order:
        draw_entity(camera_surface, camera.x, camera.y, entity, fov_map, game_map, tilesize)


    screen.blit(camera_surface, (0, 0))

    # Print game messages one line at a time
    message_surface.blit(MESSAGE_BG, (0, 0))
    y = 0
    for message in message_log.messages:
        off_x = 30
        off_y = 5
        print_message(message_surface, message, off_x, off_y, y)
        y += 1

    screen.blit(message_surface, (300, 592))
    message_surface.fill((0, 0, 0))

    resource_hud = player_resource_display(player)
    screen.blit(resource_hud, (0 - 10, 540 + 40))

    calendar = display_calendar(time_handler.month, time_handler.day)

    if game_state == GameStates.PLAYERS_TURN:
        screen.blit(calendar, (screen.get_width() - calendar.get_width(), screen.get_height() - calendar.get_height()))


    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):

        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'

        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'

        inventory_menu(screen, inventory_title, player)
    elif game_state == GameStates.SHOW_MAP:

        minimap_screen(screen, world_map)
    elif game_state == GameStates.LEVEL_UP:
        level_up_menu(screen, player)

    elif game_state == GameStates.DIALOGUE:
        dialogue_screen(screen, player, dialogue)
    elif game_state == GameStates.ENCOUNTER:
        encounter_screen(screen, player, encounter, message_log)
    elif game_state == GameStates.LOOTING:
        loot_screen(screen, loot, message_log)
    elif game_state == GameStates.MENUS:
        if menu_handler.state == MenuStates.PARTY:
            character_screen(screen, player)
        elif menu_handler.state == MenuStates.JOURNAL:
            journal_screen(screen, menu_handler)


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

