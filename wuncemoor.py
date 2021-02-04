import pygame as py
import engine.initialize as initialize


def main():
    screen, clock = initialize.pygame()
    input, logic, artist = initialize.mvc(screen, clock)

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
