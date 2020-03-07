import tcod as libtcod
import math
from game_states import GameStates
from menus import inventory_menu, dialogue_menu, level_up_menu, competence_menu, character_menu, primary_stats_screen, combat_stats_screen, noncombat_stats_screen, strength_feats_menu, instinct_feats_menu, coordinaton_feats_menu, vitality_feats_menu, arcana_feats_menu, improvisation_feats_menu, wisdom_feats_menu, finesse_feats_menu, charisma_feats_menu, devotion_feats_menu


from enum import Enum


class RenderOrder(Enum):
    CAMERA = 1
    CORPSE = 2
    STAIRS = 3
    ITEM = 4
    ACTOR = 5
    
def get_names_under_mouse(mouse, entities, fov_map):
    (x, y) = (mouse.cx, mouse.cy)
    
    names = [entity.name for entity in entities if entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)
   
    return names.capitalize()
    
def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)
    
    libtcod.console_set_default_background(panel, back_color)
    libtcod.console_rect(panel, x, y, total_width, 1, False, libtcod.BKGND_SCREEN)
    
    libtcod.console_set_default_background(panel, bar_color)
    if bar_width > 0:
        libtcod.console_rect(panel, x, y, bar_width, 1, False, libtcod.BKGND_SCREEN)
        
    libtcod.console_set_default_foreground(panel, libtcod.white)
    libtcod.console_print_ex(panel, int(x + total_width/2), y, libtcod.BKGND_NONE, libtcod.CENTER, '{0}: {1}/{2}'.format(name, value, maximum))
    
def render_nearby(con, panel, entities, player, game_map, camera, fov_map, fov_recompute, message_log, screen_width, screen_height, bar_width, panel_height, panel_y, mouse, colors, game_state):

#Draw tiles near player
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight
                
                if visible:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(con,x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
    #draw all entities in list
    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)
    for entity in entities_in_render_order:
        draw_entity(con,entity, fov_map, game_map)
    
    
    libtcod.console_blit(con, camera.x, camera.y, screen_width, screen_height, 0, 0, 0)
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_clear(panel)
    
    #Print game messages one line at a time
    y=1
    for message in message_log.messages:
        libtcod.console_set_default_foreground(panel, message.color)
        libtcod.console_print_ex(panel, message_log.x, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
        y += 1
    
    render_bar(panel, 1, 1, bar_width, 'HP', player.combatant.attributes.current_hp, player.combatant.max_hp, libtcod.light_red, libtcod.darker_red)
    render_bar(panel, 1, 2, bar_width, 'MP', player.combatant.attributes.current_mp, player.combatant.max_mp, libtcod.light_blue, libtcod.darker_blue)
    render_bar(panel, 1, 3, bar_width, 'TP', player.combatant.attributes.current_tp, player.combatant.max_tp, libtcod.light_green, libtcod.darker_green)
    render_bar(panel, 1, 4, bar_width, 'VP', player.combatant.attributes.current_vp, player.combatant.max_vp, libtcod.light_orange, libtcod.darker_orange)
    
    libtcod.console_print_ex(panel, 1, 5, libtcod.BKGND_NONE, libtcod.LEFT, 'Dungeon Level: {0}'.format(game_map.dungeon_level))
    libtcod.console_set_default_foreground(panel, libtcod.light_grey)
    libtcod.console_print_ex(panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT, get_names_under_mouse(mouse, entities, fov_map))
    libtcod.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)
    
    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        
        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
        
        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'
            
        inventory_menu(con, inventory_title, player, 50, screen_width, screen_height)
    elif game_state == GameStates.LEVEL_UP:
        level_up_menu(con, 'Level up! Choose a stat boost:', player, 40, screen_width, screen_height)
    elif game_state == GameStates.CHARACTER_MENU:
        character_menu(con, 'What would you like to look at?', 40, screen_width, screen_height)
    elif game_state == GameStates.PRIMARY_STATS_SCREEN:
        primary_stats_screen(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.COMBAT_STATS_SCREEN:
        combat_stats_screen(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.NONCOMBAT_STATS_SCREEN:
        noncombat_stats_screen(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.COMPETENCE_MENU:
        competence_menu(con, 'What would you like to be more competent at?', 40, screen_width, screen_height)
    elif game_state == GameStates.STRENGTH_FEATS:
        strength_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.INSTINCT_FEATS:
        instinct_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.COORDINATION_FEATS:
        coordinaton_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.VITALITY_FEATS:
        vitality_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.ARCANA_FEATS:
        arcana_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.IMPROVISATION_FEATS:
        improvisation_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.WISDOM_FEATS:
        wisdom_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.FINESSE_FEATS:
        finesse_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.CHARISMA_FEATS:
        charisma_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.DEVOTION_FEATS:
        devotion_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.DIALOGUE:
        dialogue_menu(player, 40, 30, screen_width, screen_height)
        

                        
def render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, screen_width, screen_height, bar_width, panel_height, panel_y, mouse, colors, game_state):
#draw all tiles in game_map
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight
                
                if visible:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
    #draw all entities in list
    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)
    for entity in entities_in_render_order:
        draw_entity(con,entity, fov_map, game_map)
    
    
    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_clear(panel)
    
    #Print game messages one line at a time
    y=1
    for message in message_log.messages:
        libtcod.console_set_default_foreground(panel, message.color)
        libtcod.console_print_ex(panel, message_log.x, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
        y += 1
    
    render_bar(panel, 1, 1, bar_width, 'HP', player.combatant.attributes.current_hp, player.combatant.max_hp, libtcod.light_red, libtcod.darker_red)
    render_bar(panel, 1, 2, bar_width, 'MP', player.combatant.attributes.current_mp, player.combatant.max_mp, libtcod.light_blue, libtcod.darker_blue)
    render_bar(panel, 1, 3, bar_width, 'TP', player.combatant.attributes.current_tp, player.combatant.max_tp, libtcod.light_green, libtcod.darker_green)
    render_bar(panel, 1, 4, bar_width, 'VP', player.combatant.attributes.current_vp, player.combatant.max_vp, libtcod.light_orange, libtcod.darker_orange)
    
    libtcod.console_print_ex(panel, 1, 5, libtcod.BKGND_NONE, libtcod.LEFT, 'Dungeon Level: {0}'.format(game_map.dungeon_level))
    libtcod.console_set_default_foreground(panel, libtcod.light_grey)
    libtcod.console_print_ex(panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT, get_names_under_mouse(mouse, entities, fov_map))
    libtcod.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)
    
    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        
        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
        
        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'
            
        inventory_menu(con, inventory_title, player, 50, screen_width, screen_height)
    elif game_state == GameStates.LEVEL_UP:
        level_up_menu(con, 'Level up! Choose a stat boost:', player, 40, screen_width, screen_height)
    elif game_state == GameStates.CHARACTER_MENU:
        character_menu(con, 'What would you like to look at?', 40, screen_width, screen_height)
    elif game_state == GameStates.PRIMARY_STATS_SCREEN:
        primary_stats_screen(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.COMBAT_STATS_SCREEN:
        combat_stats_screen(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.NONCOMBAT_STATS_SCREEN:
        noncombat_stats_screen(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.COMPETENCE_MENU:
        competence_menu(con, 'What would you like to be more competent at?', 40, screen_width, screen_height)
    elif game_state == GameStates.STRENGTH_FEATS:
        strength_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.INSTINCT_FEATS:
        instinct_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.COORDINATION_FEATS:
        coordinaton_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.VITALITY_FEATS:
        vitality_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.ARCANA_FEATS:
        arcana_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.IMPROVISATION_FEATS:
        improvisation_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.WISDOM_FEATS:
        wisdom_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.FINESSE_FEATS:
        finesse_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.CHARISMA_FEATS:
        charisma_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.DEVOTION_FEATS:
        devotion_feats_menu(player, 40, 30, screen_width, screen_height)
    elif game_state == GameStates.DIALOGUE:
        dialogue_menu(player, 40, 30, screen_width, screen_height)
        
    

def clear_all(con, entities):

    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity, fov_map, game_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y) or (entity.stairs and game_map.tiles[entity.x][entity.y].explored):
        libtcod.console_set_default_foreground(con, entity.color)    
        libtcod.console_put_char(con, entity.x, entity.y, entity.image, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    #erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)