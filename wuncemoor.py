from config.constants import START
from handlers.game_handler import GameHandler
from handlers.artist_handler import ArtistHandler
import pygame as py


def main():

    (screen_size, caption) = START
    py.init()
    py.display.set_caption(caption)
    screen = py.display.set_mode(screen_size)

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

                output = game.input.transduce(event.key)
                game.logic.translate(output)

        game.artist.render()
        py.display.flip()


if __name__ == '__main__':
    main()
