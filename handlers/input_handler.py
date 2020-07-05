import pygame
from enums.game_states import GameStates


class InputHandler:

    @property
    def mapping(self):
        state = self.owner.state
        maps = {
            GameStates.TITLE: self.main_menu,
            GameStates.LIFE: self.default,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.loot,
            GameStates.SHOW_MAP: self.map,
        }
        return maps.get(state)

    def output(self, key):
        return self.mapping(key)

    @staticmethod
    def main_menu(key):
        if key in (pygame.K_UP, pygame.K_w):
            return {'traverse_menu': -1}
        elif key in (pygame.K_DOWN, pygame.K_x):
            return {'traverse_menu': 1}
        elif key == pygame.K_RETURN:
            return {'choose_menu_option': True}
        return {}

    @staticmethod
    def default(key):
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
            return {'show_menus': 'inventory'}
        elif key == pygame.K_m:
            return {'show_map': True}
        elif key == pygame.K_j:
            return {'show_menus': 'journal'}
        elif key == pygame.K_SPACE:
            return {'interact': True}
        if key == pygame.K_RETURN and pygame.K_LALT:
            return {'fullscreen': True}
        if key == pygame.K_ESCAPE:
            return {'exit': True}
        # No key
        return {}

    @staticmethod
    def encounter(key):

        if key in (pygame.K_UP, pygame.K_w):
            return {'traverse_menu': -1}
        elif key in (pygame.K_DOWN, pygame.K_x):
            return {'traverse_menu': 1}
        elif key == pygame.K_RETURN:
            return {'choose_menu_option': True}
        elif key == pygame.K_ESCAPE:
            return {'exit': True}
        return {}

    @staticmethod
    def dialogue(key):
        return {'converse': key}

    @staticmethod
    def menus(key):
        if key == pygame.K_ESCAPE:
            return {'exit': True}
        elif key == pygame.K_j:
            return {'show_menus': 'journal'}
        elif key == pygame.K_c:
            return {'show_menus': 'party'}
        elif key == pygame.K_i:
            return {'show_menus': 'inventory'}
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

    @staticmethod
    def map(key):
        if key == pygame.K_ESCAPE:
            return {'exit': True}
        elif key == pygame.K_m:
            return {'exit': True}
        return {}

    @staticmethod
    def loot(key):

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