import tcod as libtcod
from game_states import GameStates

def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key)
    elif game_state == GameStates.CHARACTER_MENU:
        return handle_character_menu(key)
    elif game_state in (GameStates.PRIMARY_STATS_SCREEN, GameStates.COMBAT_STATS_SCREEN, GameStates.NONCOMBAT_STATS_SCREEN, GameStates.STRENGTH_FEATS, GameStates.INSTINCT_FEATS, GameStates.COORDINATION_FEATS, GameStates.VITALITY_FEATS, GameStates.ARCANA_FEATS, GameStates.IMPROVISATION_FEATS, GameStates.WISDOM_FEATS, GameStates.FINESSE_FEATS, GameStates.CHARISMA_FEATS, GameStates.DEVOTION_FEATS):
        return handle_stat_info(key)
    elif game_state == GameStates.FEATS_MENU:
        return handle_feats_menu(key)
    return {}

def handle_character_screen(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_character_menu(key):
    key_char = chr(key.c)
    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
    elif key_char == 'a':
        return {'show_primary_stats': True}
    elif key_char == 'b':
        return {'show_combat_stats': True}
    elif key_char == 'c':
        return {'show_noncombat_stats': True}
    elif key_char == 'd':
        return {'show_feats': True}   
    return {}

def handle_stat_info(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_feats_menu(key):
    key_char = chr(key.c)
    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit':True}
    elif key_char == 'a':
        return {'show_strength_feats': True}
    elif key_char == 'b':
        return {'show_instinct_feats': True}
    elif key_char == 'c':
        return {'show_coordination_feats': True}
    elif key_char == 'd':
        return {'show_vitality_feats': True}
    elif key_char == 'e':
        return {'show_arcana_feats': True}
    elif key_char == 'f':
        return {'show_improvisation_feats': True}
    elif key_char == 'g':
        return {'show_wisdom_feats': True}
    elif key_char == 'h':
        return {'show_finesse_feats': True}
    elif key_char == 'i':
        return {'show_charisma_feats': True}
    elif key_char == 'j':
        return {'show_devotion_feats': True}
    return {}
    
    
def handle_player_turn_keys(key):
    key_char = chr(key.c)
    #Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'w':
        return {'move': (0,-1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'x':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'a':
        return {'move': (-1,0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'd':
        return {'move': (1,0)}
    elif key_char == 'q':
        return {'move': (-1, -1)}
    elif key_char == 'e':
        return {'move': (1, -1)}
    elif key_char == 'z':
        return {'move': (-1, 1)}
    elif key_char == 'c':
        return {'move': (1, 1)}
    elif key_char == 'p':
        return {'show_stats_menu': True}
    elif key_char == 's':
        return {'wait': True}
    if key_char == 'g':
        return {'pickup': True}
    elif key_char == 'i':
        return {'show_inventory': True}
    elif key_char == 'o':
        return {'drop_inventory': True}
    elif key.vk == libtcod.KEY_ENTER:
        return {'take_stairs': True}
    
    #Alt+Enter = Fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    #Exit the game    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
        
    #No key
    return {}
    
def handle_targeting_keys(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_player_dead_keys(key):
    key_char = chr(key.c)
    
    if key_char == 'i':
        return {'show_inventory': True}
        
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle full screen
        return {'fullscreen': True }
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}
        
    return {}
    
def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)
    
    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}
        
    return {}
    
def handle_inventory_keys(key):
    index = key.c - ord('a')
    char_key = chr(key.c)
   
    
    if index >= 0:
        return {'inventory_index': index}
        
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter = Fullscreen Toggle
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        #Exit
        return {'exit': True}
        
    return {}
    
def handle_main_menu(key):
    key_char = chr(key.c)
    
    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
        
    return {}

def handle_level_up_menu(key):
    if key:
        key_char = chr(key.c)
        
        if key_char == 'a':
            return {'level_up': 'Strength'}
        elif key_char == 'b':
            return {'level_up': 'Instinct'}
        elif key_char == 'c':
            return {'level_up': 'Coordination'}
        elif key_char == 'd':
            return {'level_up': 'Vitality'}
        elif key_char == 'e':
            return {'level_up': 'Arcana'}
        elif key_char == 'f':
            return {'level_up': 'Improvisation'}
        elif key_char == 'g':
            return {'level_up': 'Wisdom'}
        elif key_char == 'h':
            return {'level_up': 'Finesse'}
        elif key_char == 'i':
            return {'level_up': 'Charisma'}
        elif key_char == 'j':
            return {'level_up': 'Devotion'}
    
    return {}