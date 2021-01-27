import pygame as py
from config.constants import SCREEN_SIZE, CAPTION, KEYDOWN_DELAY
from handlers.game_handler import GameHandler
from handlers.artist_handler import ArtistHandler
from handlers.input_handler import InputHandler
from handlers.logic_handler import LogicHandler
from handlers.options_handler import OptionsHandler


def main():

    py.init()
    py.display.set_caption(CAPTION)
    py.key.set_repeat(KEYDOWN_DELAY)
    screen = py.display.set_mode(SCREEN_SIZE, flags=py.FULLSCREEN)
    clock = py.time.Clock()

    options = OptionsHandler()
    game = GameHandler(options)
    options.game = game
    input = InputHandler(game)
    logic = LogicHandler(game)
    artist = ArtistHandler(game, screen, clock)

    game.state_handler = game.title
    game.options.get()
    running = True
    while running:
        clock.tick()
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
