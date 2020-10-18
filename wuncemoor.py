import pygame as py
from config.constants import SCREEN_SIZE, CAPTION
from handlers.game_handler import GameHandler
from handlers.artist_handler import ArtistHandler


def main():

    py.init()
    py.display.set_caption(CAPTION)
    screen = py.display.set_mode(SCREEN_SIZE)

    artist = ArtistHandler(screen)
    game = GameHandler(artist)
    game.state_handler = game.title
    game.options.get()
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                game.quit()
            if event.type == py.KEYDOWN:

                output = game.input.transduce(event)
                game.logic.translate(output)

        game.artist.render()
        py.display.flip()


if __name__ == '__main__':
    main()
