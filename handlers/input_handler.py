import pygame as py
from abstracts.abstract_mvc import MVC
from handlers.menus.settings import Settings


class InputHandler(MVC):

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

    def life(self, key):
        if key in (py.K_UP, py.K_w):
            return {'move': (0, -1)}
        elif key in (py.K_DOWN, py.K_s):
            return {'move': (0, 1)}
        elif key in (py.K_LEFT, py.K_a):
            return {'move': (-1, 0)}
        elif key in (py.K_RIGHT, py.K_d):
            return {'move': (1, 0)}
        elif key == py.K_c:
            return {'show_menus': self.owner.party}
        elif key == py.K_i:
            return {'show_menus': self.owner.party.inventory}
        elif key == py.K_m:
            return {'show_menus': self.owner.party.map}
        elif key == py.K_j:
            return {'show_menus': self.owner.party.journal}
        elif key == py.K_SPACE:
            return {'interact': True}
        if key == py.K_RETURN and py.K_LALT:
            return {'fullscreen': True}
        if key == py.K_ESCAPE:
            return {'show_menus': Settings()}
        return {}

    @staticmethod
    def encounter(key):

        if key in (py.K_a, py.K_LEFT):
            return {'traverse_menu': (-1, 0)}
        elif key in (py.K_d, py.K_RIGHT):
            return {'traverse_menu': (1, 0)}
        elif key in (py.K_w, py.K_UP):
            return {'traverse_menu': (0, -1)}
        elif key in (py.K_s, py.K_DOWN):
            return {'traverse_menu': (0, 1)}
        elif key == py.K_RETURN:
            return {'choose_option': True}
        elif key == py.K_ESCAPE:
            return {'exit': True}
        return {}

    @staticmethod
    def dialogue(key):
        return {'converse': key}

    def menus(self, key):
        if key == py.K_ESCAPE:
            return {'exit': True}
        elif key == py.K_c:
            return {'show_menus': self.owner.party}
        elif key == py.K_i:
            return {'show_menus': self.owner.party.inventory}
        elif key == py.K_m:
            return {'show_menus': self.owner.party.map}
        elif key == py.K_j:
            return {'show_menus': self.owner.party.journal}
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
            return {'choose_option': True}
        elif key == py.K_ESCAPE:
            return {'exit': True}
        return {}
