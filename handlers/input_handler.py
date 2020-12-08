import pygame as py
from abstracts.abstract_mvc import MVC
from enums.game_states import GameStates
from handlers.menus.settings import Settings


class InputHandler(MVC):

    def transduce(self, event):
        return self.mapping(event)

    @staticmethod
    def debug(event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key == py.K_ESCAPE:
            return {'exit': True}
        elif event.key == py.K_RETURN:
            return {'command_send': True}
        elif event.key == py.K_BACKSPACE:
            return {'command_pop': True}
        else:
            return {'command_extend': event.unicode}

    @staticmethod
    def title(event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key in (py.K_UP, py.K_w):
            return {'traverse_menu': -1}
        elif event.key in (py.K_DOWN, py.K_x):
            return {'traverse_menu': 1}
        elif event.key == py.K_RETURN:
            return {'choose_option': True}
        elif event.key == py.K_PERIOD:
            return {'debug': GameStates.TITLE}
        return {}

    def life(self, event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key in (py.K_UP, py.K_w):
            return {'move': (0, -1)}
        elif event.key in (py.K_DOWN, py.K_s):
            return {'move': (0, 1)}
        elif event.key in (py.K_LEFT, py.K_a):
            return {'move': (-1, 0)}
        elif event.key in (py.K_RIGHT, py.K_d):
            return {'move': (1, 0)}
        elif event.key == py.K_c:
            return {'show_menus': self.game.party}
        elif event.key == py.K_i:
            return {'show_menus': self.game.party.inventory}
        elif event.key == py.K_m:
            return {'show_menus': self.game.party.map}
        elif event.key == py.K_j:
            return {'show_menus': self.game.party.journal}
        elif event.key == py.K_SPACE:
            return {'interact': True}
        elif event.key == py.K_PERIOD:
            return {'debug': GameStates.LIFE}
        if event.key == py.K_ESCAPE:
            return {'show_menus': Settings()}
        return {}

    @staticmethod
    def encounter(event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key in (py.K_a, py.K_LEFT):
            return {'traverse_menu': (-1, 0)}
        elif event.key in (py.K_d, py.K_RIGHT):
            return {'traverse_menu': (1, 0)}
        elif event.key in (py.K_w, py.K_UP):
            return {'traverse_menu': (0, -1)}
        elif event.key in (py.K_s, py.K_DOWN):
            return {'traverse_menu': (0, 1)}
        elif event.key == py.K_RETURN:
            return {'choose_option': True}
        elif event.key == py.K_ESCAPE:
            return {'exit': True}
        elif event.key == py.K_PERIOD:
            return {'debug': GameStates.ENCOUNTER}
        return {}

    @staticmethod
    def dialogue(event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        return {'converse': event.key}

    def shop(self, event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key == py.K_ESCAPE:
            return {'exit': True}
        elif event.key in (py.K_a, py.K_LEFT):
            return {'traverse_menu': (-1, 0)}
        elif event.key in (py.K_d, py.K_RIGHT):
            return {'traverse_menu': (1, 0)}
        elif event.key in (py.K_w, py.K_UP):
            return {'traverse_menu': (0, -1)}
        elif event.key in (py.K_s, py.K_DOWN):
            return {'traverse_menu': (0, 1)}
        elif event.key == py.K_RETURN:
            return {'choose_option': True}
        elif event.key == py.K_PERIOD:
            return {'debug': GameStates.MENUS}
        return {}

    def menus(self, event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key == py.K_ESCAPE:
            return {'exit': True}
        elif event.key == py.K_c:
            return {'show_menus': self.game.party}
        elif event.key == py.K_i:
            return {'show_menus': self.game.party.inventory}
        elif event.key == py.K_m:
            return {'show_menus': self.game.party.map}
        elif event.key == py.K_j:
            return {'show_menus': self.game.party.journal}
        elif event.key in (py.K_a, py.K_LEFT):
            return {'traverse_menu': (-1, 0)}
        elif event.key in (py.K_d, py.K_RIGHT):
            return {'traverse_menu': (1, 0)}
        elif event.key in (py.K_w, py.K_UP):
            return {'traverse_menu': (0, -1)}
        elif event.key in (py.K_s, py.K_DOWN):
            return {'traverse_menu': (0, 1)}
        elif event.key == py.K_RETURN:
            return {'choose_option': True}
        elif event.key == py.K_PERIOD:
            return {'debug': GameStates.MENUS}
        return {}

    @staticmethod
    def reward(event):
        if event.key == py.K_F11:
            return {'fullscreen': True}
        elif event.key in (py.K_UP, py.K_w):
            return {'traverse_menu': -1}
        elif event.key in (py.K_DOWN, py.K_x):
            return {'traverse_menu': 1}
        elif event.key in (py.K_LEFT, py.K_a):
            return {'toggle': 'left'}
        elif event.key in (py.K_RIGHT, py.K_d):
            return {'toggle': 'right'}
        elif event.key == py.K_RETURN:
            return {'choose_option': True}
        elif event.key == py.K_ESCAPE:
            return {'exit': True}
        elif event.key == py.K_PERIOD:
            return {'debug': GameStates.REWARD}
        return {}
