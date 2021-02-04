import pygame as py

from config.constants import CAPTION, KEYDOWN_DELAY, SCREEN_SIZE
from handlers.artist_handler import ArtistHandler
from handlers.game_handler import GameHandler
from handlers.input_handler import InputHandler
from handlers.logic_handler import LogicHandler
from handlers.options_handler import OptionsHandler


def mvc(screen, clock):
    options = OptionsHandler()
    game = GameHandler(options)
    options.game = game
    input = InputHandler(game)
    logic = LogicHandler(game)
    artist = ArtistHandler(game, screen, clock)

    game.set_root_state()

    return input, logic, artist


def pygame():
    py.init()
    py.display.set_caption(CAPTION)
    py.key.set_repeat(KEYDOWN_DELAY)
    screen = py.display.set_mode(SCREEN_SIZE, flags=py.FULLSCREEN)
    clock = py.time.Clock()

    return screen, clock
