import pygame as py
from enums.game_states import GameStates


class InputHandler:

    @property
    def state(self):
        return self.owner.state

    @property
    def mapping(self):
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.reward,
        }
        return maps.get(self.state)

    def transduce(self, key):
        return self.mapping(key)

    @staticmethod
    def title(key):
        if key in (py.K_UP, py.K_w):
            return {'traverse_menu': -1}
        elif key in (py.K_DOWN, py.K_x):
            return {'traverse_menu': 1}
        elif key == py.K_RETURN:
            return {'choose_option': True}
        return {}

    @staticmethod
    def life(key):
        if key in (py.K_UP, py.K_w):
            return {'move': (0, -1)}
        elif key in (py.K_DOWN, py.K_s):
            return {'move': (0, 1)}
        elif key in (py.K_LEFT, py.K_a):
            return {'move': (-1, 0)}
        elif key in (py.K_RIGHT, py.K_d):
            return {'move': (1, 0)}
        elif key == py.K_c:
            return {'show_menus': 'party'}
        elif key == py.K_i:
            return {'show_menus': 'inventory'}
        elif key == py.K_m:
            return {'show_menus': 'map'}
        elif key == py.K_j:
            return {'show_menus': 'journal'}
        elif key == py.K_SPACE:
            return {'interact': True}
        if key == py.K_RETURN and py.K_LALT:
            return {'fullscreen': True}
        if key == py.K_ESCAPE:
            return {'exit': True}
        # No key
        return {}

    @staticmethod
    def encounter(key):

        if key in (py.K_UP, py.K_w):
            return {'traverse_menu': -1}
        elif key in (py.K_DOWN, py.K_x):
            return {'traverse_menu': 1}
        elif key == py.K_RETURN:
            return {'choose_option': True}
        elif key == py.K_ESCAPE:
            return {'exit': True}
        return {}

    @staticmethod
    def dialogue(key):
        return {'converse': key}

    @staticmethod
    def menus(key):
        if key == py.K_ESCAPE:
            return {'exit': True}
        elif key == py.K_j:
            return {'show_menus': 'journal'}
        elif key == py.K_c:
            return {'show_menus': 'party'}
        elif key == py.K_i:
            return {'show_menus': 'inventory'}
        elif key == py.K_m:
            return {'show_menus': 'map'}
        elif key in (py.K_a, py.K_LEFT):
            return {'traverse_menu': (-1, 0)}
        elif key in (py.K_d, py.K_RIGHT):
            return {'traverse_menu': (1, 0)}
        elif key in (py.K_w, py.K_UP):
            return {'traverse_menu': (0, -1)}
        elif key in (py.K_s, py.K_DOWN):
            return {'traverse_menu': (0, 1)}
        elif key == py.K_RETURN:
            return {'choose_option': True}
        return {}

    @staticmethod
    def reward(key):

        if key in (py.K_UP, py.K_w):
            return {'traverse_menu': -1}
        elif key in (py.K_DOWN, py.K_x):
            return {'traverse_menu': 1}
        elif key in (py.K_LEFT, py.K_a):
            return {'toggle': 'left'}
        elif key in (py.K_RIGHT, py.K_d):
            return {'toggle': 'right'}
        elif key == py.K_RETURN:
            return {'choose_menu_option': True}
        elif key == py.K_ESCAPE:
            return {'exit': True}
        return {}


def handle_targeting_keys(key):
    if key == py.K_ESCAPE:
        return {'exit': True}
        
    return {}
    
def handle_player_dead_keys(key):
    
    if key == py.K_i:
        return {'show_inventory': True}
        

    elif key == py.K_ESCAPE:
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
        
        if key == py.K_a:
            return {'level_up': 'Strength'}
        elif key == py.K_b:
            return {'level_up': 'Instinct'}
        elif key == py.K_c:
            return {'level_up': 'Coordination'}
        elif key == py.K_d:
            return {'level_up': 'Vitality'}
        elif key == py.K_e:
            return {'level_up': 'Arcana'}
        elif key == py.K_f:
            return {'level_up': 'Improvisation'}
        elif key == py.K_g:
            return {'level_up': 'Wisdom'}
        elif key == py.K_h:
            return {'level_up': 'Finesse'}
        elif key == py.K_i:
            return {'level_up': 'Charisma'}
        elif key == py.K_j:
            return {'level_up': 'Devotion'}
    
    return {}