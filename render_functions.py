import tcod as libtcod
import pygame
from enums.game_states import GameStates
from menus import inventory_menu, level_up_menu, competence_menu, character_menu, primary_stats_screen, \
    combat_stats_screen, noncombat_stats_screen, strength_feats_menu, instinct_feats_menu, coordinaton_feats_menu, \
    vitality_feats_menu, arcana_feats_menu, improvisation_feats_menu, wisdom_feats_menu, finesse_feats_menu, \
    charisma_feats_menu, devotion_feats_menu, map_menu, dialogue_menu, encounter_screen
from random_utils import pseudorandom_seed


from enum import Enum


class RenderOrder(Enum):
    CORPSE = 1
    STAIRS = 2
    ITEM = 3
    ACTOR = 4


def get_names_under_mouse(entities, fov_map):
    (x, y) = pygame.mouse.get_pos()

    names = [entity.name for entity in entities if
             entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()


def render_bar(resource_surface, x, y, bar_x, bar_y, name, val, maxval):

    window = pygame.Surface((bar_x, bar_y))

    full = get_render_bar_asset(name, full=True)
    empty = get_render_bar_asset(name, full=False)

    percent = float(val / maxval) * 100
    assetwidth = 15

    for i in range(20):
        if percent >= (i + 1) * 5:
            window.blit(full, ((i * assetwidth), 0))
        else:
            window.blit(empty, ((i * assetwidth), 0))

    resource_surface.blit(window, (x, y))
    fontsize = 20
    font = pygame.font.SysFont("comicsansms", fontsize)
    text = font.render('{0}: {1}/{2}'.format(name, val, maxval), True, (255, 255, 255))
    window.blit(text, (50, -5))
    resource_surface.blit(window, (x, y))


def get_render_bar_asset(name, full):
    render_dict = {
        'HP': ['images\\render_bar_assets\\hp_full.png',
               'images\\render_bar_assets\\hp_empty.png'],
        'MP': ['images\\render_bar_assets\\mp_full.png',
               'images\\render_bar_assets\\mp_empty.png'],
        'TP': ['images\\render_bar_assets\\tp_full.png',
               'images\\render_bar_assets\\tp_empty.png'],
        'VP': ['images\\render_bar_assets\\vp_full.png',
               'images\\render_bar_assets\\vp_empty.png']
    }
    try:
        pack = render_dict.get(name)
        if full:
            asset = pack[0]
        else:
            asset = pack[1]
    except TypeError:
        asset = 'images\\render_bar_assets\\blank.png'
    return pygame.image.load(asset)


def render_all(screen, camera_surface, resource_surface, message_surface, entities, player, structures, transitions,
               noncombatants, game_map, world_map, images, camera, fov_map, fov_recompute, message_log, camera_width,
               camera_height, map_width, map_height, game_state, encounter=None):
    tiles = images.get('tiles')
    options = images.get('options')
    ents = images.get('entities')
    tilesize = 16
    # Draw tiles near player
    if fov_recompute:
        for y in range(map_height):
            for x in range(map_width):
                draw_tile(camera_surface, fov_map, game_map, x, y, camera.x, camera.y, tiles, tilesize, options)

    for structure in structures:
        draw_structure(camera_surface, camera.x, camera.y, structure, fov_map, game_map, tiles, tilesize)
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
    y = 0
    for message in message_log.messages:
        print_message(message_surface, message, 20, y)
        y += 1

    screen.blit(message_surface, (300, 592))
    message_surface.fill((0, 0, 0))

    render_bar(resource_surface, 0, 0, 300, 25, get_names_under_mouse(entities, fov_map), 1, 1)
    render_bar(resource_surface, 0, 20, 300, 25, 'HP', player.combatant.attributes.current_hp, player.combatant.max_hp)
    render_bar(resource_surface, 0, 40, 300, 25, 'MP', player.combatant.attributes.current_mp, player.combatant.max_mp)
    render_bar(resource_surface, 0, 60, 300, 25, 'TP', player.combatant.attributes.current_tp, player.combatant.max_tp)
    render_bar(resource_surface, 0, 80, 300, 25, 'VP', player.combatant.attributes.current_vp, player.combatant.max_vp)
    render_bar(resource_surface, 0, 100, 300, 25, 'Dungeon Level: {0}'.format(game_map.dungeon_level), 1, 1)

    screen.blit(resource_surface, (0, 592))

    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        gui_img = images.get('gui').get('inventory_menu')


        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'

        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'

        inventory_menu(screen, inventory_title, gui_img, player, camera_width, camera_height)
    elif game_state == GameStates.SHOW_MAP:
        mm_width = 400
        mm_height = 400
        mm_images = tiles.get('world_map').get('mini_map')
        map_menu(screen, world_map, mm_images, mm_width, mm_height, camera_width, camera_height)
    elif game_state == GameStates.LEVEL_UP:
        gui_img = images.get('gui').get('levelup_menu')
        level_up_menu(screen, 'Level up! Choose a stat boost:', gui_img, player, camera_width, camera_height)
    elif game_state == GameStates.CHARACTER_MENU:
        gui_img = images.get('gui').get('character_menu')
        character_menu(screen, 'What would you like to look at?', gui_img, camera_width, camera_height)
    elif game_state == GameStates.PRIMARY_STATS_SCREEN:
        gui_img = images.get('gui').get('primary_stats_screen')
        primary_stats_screen(screen, player, gui_img, camera_width, camera_height)
    elif game_state == GameStates.COMBAT_STATS_SCREEN:
        css_width = 400
        css_height = 400
        combat_stats_screen(screen, player, css_width, css_height, camera_width, camera_height)
    elif game_state == GameStates.NONCOMBAT_STATS_SCREEN:
        nss_width = 400
        nss_height = 400
        noncombat_stats_screen(screen, player, nss_width, nss_height, camera_width, camera_height)
    elif game_state == GameStates.DIALOGUE:
        gui_img = images.get('gui').get('dialogue_menu')
        dialogue_menu(screen, gui_img, player, noncom, camera_width, camera_height)
    elif game_state == GameStates.ENCOUNTER:
        res_menu_imgs = images.get('gui').get('resource_hud_objs')
        encounter_screen(screen, res_menu_imgs, player, encounter)
    elif game_state == GameStates.COMPETENCE_MENU:
        cm_width = 400
        competence_menu(screen, 'What would you like to be more competent at?', cm_width, camera_width, camera_height)
    elif game_state == GameStates.STRENGTH_FEATS:
        sf_width = 400
        sf_height = 300
        strength_feats_menu(player, sf_width, sf_height, camera_width, camera_height)
    elif game_state == GameStates.INSTINCT_FEATS:
        if_width = 400
        if_height = 300
        instinct_feats_menu(player, if_width, if_height, camera_width, camera_height)
    elif game_state == GameStates.COORDINATION_FEATS:
        cf_width = 400
        cf_height = 300
        coordinaton_feats_menu(player, cf_width, cf_height, camera_width, camera_height)
    elif game_state == GameStates.VITALITY_FEATS:
        vf_width = 400
        vf_height = 300
        vitality_feats_menu(player, vf_width, vf_height, camera_width, camera_height)
    elif game_state == GameStates.ARCANA_FEATS:
        af_width = 400
        af_height = 300
        arcana_feats_menu(player, af_width, af_height, camera_width, camera_height)
    elif game_state == GameStates.IMPROVISATION_FEATS:
        if_width = 400
        if_height = 300
        improvisation_feats_menu(player, if_width, if_height, camera_width, camera_height)
    elif game_state == GameStates.WISDOM_FEATS:
        wf_width = 400
        wf_height = 300
        wisdom_feats_menu(player, wf_width, wf_height, camera_width, camera_height)
    elif game_state == GameStates.FINESSE_FEATS:
        ff_width = 400
        ff_height = 300
        finesse_feats_menu(player, ff_width, ff_height, camera_width, camera_height)
    elif game_state == GameStates.CHARISMA_FEATS:
        cf_width = 400
        cf_height = 300
        charisma_feats_menu(player, cf_width, cf_height, camera_width, camera_height)
    elif game_state == GameStates.DEVOTION_FEATS:
        df_width = 400
        df_height = 300
        devotion_feats_menu(player, df_width, df_height, camera_width, camera_height)


def draw_entity(camera_surface, cx, cy, entity, fov_map, game_map, tilesize):
    surfimg = entity.image
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y) or (
            entity.transition and game_map.tiles[entity.x][entity.y].explored):
        camera_surface.blit(surfimg, ((entity.x - cx) * tilesize, (entity.y - cy) * tilesize))


def draw_structure(camera_surface, cx, cy, structure, fov_map, game_map, tiles, tilesize):

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
                camera_surface.blit(tiles.get('black'), ((i - cx) * tilesize, (j - cy) * tilesize))
                count += 1


def print_message(message_surface, message, mlogx, y):
    fontsize = 12
    font = pygame.font.SysFont("comicsansms", fontsize)
    pm = font.render(message.text, True, message.color)
    message_surface.blit(pm, (mlogx, y * fontsize))


def draw_tile(camera_surface, fov_map, game_map, x, y, cx, cy, tiles, tilesize, options):
    visible = libtcod.map_is_in_fov(fov_map, cx + x, cy + y)

    tile = game_map.tiles[cx + x][cy + y]
    gmv = tiles.get(game_map.variant)
    tt = tile.type
    if visible:
        prefix = 'light_'
        if tt == 'road':
            obj = tiles.get(prefix + tt).get(tile.mode)
            camera_surface.blit(obj, (x * tilesize, y * tilesize))
        elif tt == 'wall':
            camera_surface.blit(tiles.get(prefix + tt), (x * tilesize, y * tilesize))
        else:
            try:
                camera_surface.blit(gmv.get(prefix + tt).get(prefix + tt + tile.mode), (x * tilesize, y * tilesize))
            except:
                img = game_map.current_map.floor_image
                choice = str(pseudorandom_seed(x, y, options.get(img)))
                obj = tiles.get(prefix + img).get(prefix + img + choice)
                camera_surface.blit(obj, (x * tilesize, y * tilesize))
        tile.explored = True
    elif tile.explored:
        prefix = 'dark_'
        if tt == 'road':
            obj = tiles.get(prefix + tt).get(game_map.tiles[cx + x][cy + y].mode)
            camera_surface.blit(obj, (x * tilesize, y * tilesize))
        elif tt == 'wall':
            camera_surface.blit(tiles.get(prefix + tt), (x * tilesize, y * tilesize))
        else:
            try:
                camera_surface.blit(gmv.get(prefix + tt).get(prefix + tt + tile.mode), (x * tilesize, y * tilesize))
            except:
                img = game_map.current_map.floor_image
                choice = str(pseudorandom_seed(x, y, options.get(img)))
                obj = tiles.get(prefix + img).get(prefix + img + choice)
                camera_surface.blit(obj, (x * tilesize, y * tilesize))

    else:
        camera_surface.blit(tiles.get('black'), (x * tilesize, y * tilesize))

