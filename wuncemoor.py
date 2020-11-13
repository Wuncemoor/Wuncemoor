import pygame as py
from config.constants import SCREEN_SIZE, CAPTION
from handlers.game_handler import GameHandler
from handlers.artist_handler import ArtistHandler
from handlers.input_handler import InputHandler
from handlers.logic_handler import LogicHandler
from handlers.options_handler import OptionsHandler


def main():

    py.init()
    py.display.set_caption(CAPTION)
    screen = py.display.set_mode(SCREEN_SIZE, flags=py.FULLSCREEN)

    input = InputHandler()
    logic = LogicHandler()
    options = OptionsHandler()
    artist = ArtistHandler(screen)

    game = GameHandler(options)
    input.game, logic.game, options.game, artist.game = game, game, game, game

    game.state_handler = game.title
    game.options.get()
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                game.quit()
            if event.type == py.KEYDOWN:

                output = input.transduce(event)
                logic.translate(output)

        artist.render()
        py.display.flip()


if __name__ == '__main__':
    main()
