import tcod as libtcod
import pygame
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
    elif game_state in (GameStates.PRIMARY_STATS_SCREEN, GameStates.COMBAT_STATS_SCREEN, GameStates.NONCOMBAT_STATS_SCREEN, GameStates.INSTINCT_FEATS, GameStates.COORDINATION_FEATS, GameStates.VITALITY_FEATS, GameStates.ARCANA_FEATS, GameStates.IMPROVISATION_FEATS, GameStates.WISDOM_FEATS, GameStates.FINESSE_FEATS, GameStates.CHARISMA_FEATS, GameStates.DEVOTION_FEATS):
        return handle_stat_info(key)
    elif game_state == GameStates.STRENGTH_FEATS:
        return handle_strength(key)
    elif game_state == GameStates.COMPETENCE_MENU:
        return handle_competence_menu(key)
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
    elif key in (pygame.K_DOWN, pygame.K_x):
        return {'move': (0, 1)}
    elif key in (pygame.K_LEFT, pygame.K_a):
        return {'move': (-1, 0)}
    elif key in (pygame.K_RIGHT, pygame.K_d):
        return {'move': (1, 0)}
    elif key == pygame.K_q:
        return {'move': (-1, -1)}
    elif key == pygame.K_e:
        return {'move': (1, -1)}
    elif key == pygame.K_z:
        return {'move': (-1, 1)}
    elif key == pygame.K_c:
        return {'move': (1, 1)}
    elif key == pygame.K_p:
        return {'show_stats_menu': True}
    elif key == pygame.K_s:
        return {'wait': True}
    elif key == pygame.K_i:
        return {'show_inventory': True}
    # Disabled until finished
    # elif key == pygame.K_f:
    # return {'show_competence': True}
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


def handle_character_screen(key):
    if event.key == pygame.K_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_character_menu(key):

    
    if key == pygame.K_ESCAPE:
        return {'exit': True}
    elif key == pygame.K_a:
        return {'show_primary_stats': True}
    elif key == pygame.K_b:
        return {'show_combat_stats': True}
    elif key == pygame.K_c:
        return {'show_noncombat_stats': True}
    return {}

def handle_stat_info(key):
    if key == pygame.K_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_competence_menu(key):
    
    if key == pygame.K_ESCAPE:
        return {'exit':True}
    elif key == pygame.K_a:
        return {'show_strength_feats': True}
    elif key == pygame.K_b:
        return {'show_instinct_feats': True}
    elif key == pygame.K_c:
        return {'show_coordination_feats': True}
    elif key == pygame.K_d:
        return {'show_vitality_feats': True}
    elif key == pygame.K_e:
        return {'show_arcana_feats': True}
    elif key == pygame.K_f:
        return {'show_improvisation_feats': True}
    elif key == pygame.K_g:
        return {'show_wisdom_feats': True}
    elif key == pygame.K_h:
        return {'show_finesse_feats': True}
    elif key == pygame.K_i:
        return {'show_charisma_feats': True}
    elif key == pygame.K_j:
        return {'show_devotion_feats': True}
    return {}
    
def handle_strength(key):

    
    if key == pygame.K_a:
        return {'gain_competence': ('strength','mighty_strength_flag')}
    elif key == pygame.K_b:
        return {'gain_competence': ('strength','better_slash_flag')}
    elif key == pygame.K_c:
        return {'gain_competence': ('strength','better stab_flag')}
    elif key == pygame.K_d:
        return {'gain_competence': ('strength','better_blunt_flag')}

    
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