import sys
import pygame
import engine.initialize as initialize


def main():
    screen, clock = initialize.pygame()
    input, logic, artist = initialize.mvc(screen, clock)

    running = True

    while running:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            if event.type == pygame.KEYDOWN:

                output = input.transduce(event)
                logic.translate(output)

        artist.render()
        pygame.display.flip()


if __name__ == '__main__':
    main()
