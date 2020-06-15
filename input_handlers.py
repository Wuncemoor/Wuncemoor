import pygame
from enums.game_states import GameStates, MenuStates


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
    elif game_state == GameStates.MENUS:
        return handle_menus(key)
    elif game_state == GameStates.SHOW_MAP:
        return handle_map_screen(key)
    elif game_state == GameStates.DIALOGUE:
        return handle_dialogue_menu(key)
    elif game_state == GameStates.ENCOUNTER:
        return handle_encounter_screen(key)
    elif game_state == GameStates.LOOTING:
        return handle_loot_screen(key)
    return {}


def handle_main_menu(key):
    if key == pygame.K_a:
        return {'new_game': True}
    elif key == pygame.K_b:
        return {'load_game': True}
    elif key in (pygame.K_c, pygame.K_ESCAPE):
        return {'exit': True}

    return {}


def handle_player_turn_keys(key):
    # Movement keys
    if key in (pygame.K_UP, pygame.K_w):
        return {'move': (0, -1)}
    elif key in (pygame.K_DOWN, pygame.K_s):
        return {'move': (0, 1)}
    elif key in (pygame.K_LEFT, pygame.K_a):
        return {'move': (-1, 0)}
    elif key in (pygame.K_RIGHT, pygame.K_d):
        return {'move': (1, 0)}
    elif key == pygame.K_c:
        return {'show_menus': 'party'}
    elif key == pygame.K_i:
        return {'show_inventory': True}
    elif key == pygame.K_m:
        return {'show_map': True}
    elif key == pygame.K_j:
        return {'show_menus': 'journal'}
    elif key == pygame.K_o:
        return {'drop_inventory': True}
    elif key == pygame.K_SPACE:
        return {'interact': True}


    # Alt+Enter = Fullscreen
    if key == pygame.K_RETURN and pygame.K_LALT:
        return {'fullscreen': True}
    # Exit the game
    if key == pygame.K_ESCAPE:
        return {'exit': True}

    # No key
    return {}


def handle_inventory_keys(key):


    if key is not None:
        index = key - ord('a')
    else:
        index = -1

    if index >= 0 and index <= 26:
        return {'inventory_index': index}


    elif key == pygame.K_ESCAPE:
        # Exit
        return {'exit': True}

    return {}


def handle_map_screen(key):
    if key == pygame.K_ESCAPE:
        return {'exit': True}
    elif key == pygame.K_m:
        return {'exit': True}
        
    return {}

def handle_menus(key):
    if key == pygame.K_ESCAPE:
        return {'exit': True}
    elif key in (pygame.K_a, pygame.K_LEFT):
        return {'traverse_menu': (-1, 0)}
    elif key in (pygame.K_d, pygame.K_RIGHT):
        return {'traverse_menu': (1, 0)}
    elif key in (pygame.K_w, pygame.K_UP):
        return {'traverse_menu': (0, -1)}
    elif key in (pygame.K_s, pygame.K_DOWN):
        return {'traverse_menu': (0, 1)}
    elif key == pygame.K_RETURN:
        return {'choose_menu_option': True}
    return {}



def handle_dialogue_menu(key):

    return {'converse': key}


def handle_encounter_screen(key):

    if key in (pygame.K_UP, pygame.K_w):
        return {'traverse_menu': -1}
    elif key in (pygame.K_DOWN, pygame.K_x):
        return {'traverse_menu': 1}
    elif key == pygame.K_RETURN:
        return {'choose_menu_option': True}
    elif key == pygame.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_loot_screen(key):

    if key in (pygame.K_UP, pygame.K_w):
        return {'traverse_menu': -1}
    elif key in (pygame.K_DOWN, pygame.K_x):
        return {'traverse_menu': 1}
    elif key in (pygame.K_LEFT, pygame.K_a):
        return {'toggle': 'left'}
    elif key in (pygame.K_RIGHT, pygame.K_d):
        return {'toggle': 'right'}
    elif key == pygame.K_RETURN:
        return {'choose_menu_option': True}
    elif key == pygame.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_targeting_keys(key):
    if key == pygame.K_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_player_dead_keys(key):
    
    if key == pygame.K_i:
        return {'show_inventory': True}
        

    elif key == pygame.K_ESCAPE:
        # Exit the menu
        return {'exit': True}
        
    return {}
    
def handle_mouse(mouse):
    try:
        (x, y) = (mouse[0][0], mouse[0][1])
    
    
        if mouse[1] == 1:
            return {'left_click': (x, y)}
        elif mouse[1] == 3:
            return {'right_click': (x, y)}
    except:
        return {}
        
    return {}


def handle_level_up_menu(key):
    if key:
        
        if key == pygame.K_a:
            return {'level_up': 'Strength'}
        elif key == pygame.K_b:
            return {'level_up': 'Instinct'}
        elif key == pygame.K_c:
            return {'level_up': 'Coordination'}
        elif key == pygame.K_d:
            return {'level_up': 'Vitality'}
        elif key == pygame.K_e:
            return {'level_up': 'Arcana'}
        elif key == pygame.K_f:
            return {'level_up': 'Improvisation'}
        elif key == pygame.K_g:
            return {'level_up': 'Wisdom'}
        elif key == pygame.K_h:
            return {'level_up': 'Finesse'}
        elif key == pygame.K_i:
            return {'level_up': 'Charisma'}
        elif key == pygame.K_j:
            return {'level_up': 'Devotion'}
    
    return {}