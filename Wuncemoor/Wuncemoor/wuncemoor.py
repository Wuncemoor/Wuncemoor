import tcod as libtcod
from fov_function import initialize_fov, recompute_fov
from entity import get_blocking_entities_at_location
from death_functions import kill_monster, kill_player
from game_states import GameStates
from game_messages import Message
from input_handlers import handle_keys, handle_mouse, handle_main_menu
from render_functions import clear_all, render_all, render_bar
from loader_functions.initialize_new_game import get_constants, get_game_variables
from loader_functions.data_loaders import load_game, save_game
from menus import main_menu, message_box
from PIL import Image
import random
import math
import pygame

pygame.init()

size = (700,500)
constants = get_constants()
colors = constants['colors']


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Wuncemoor')




clock = pygame.time.Clock()

#Main Loop
def main():
    carryOn = True

    while carryOn:
        
        for event in pygame.event.get(): #User input
            if event.type == pygame.QUIT:
                carryOn = False
                
        #Game Logic Here
        
        #Drawing code here
        
        screen.fill(colors.get('white'))
        pygame.draw.rect(screen, colors.get('dark_wall'), [0, 0, 100, 500],0)
        pygame.draw.rect(screen, colors.get('white'), [100, 0, 20, 500],0)
        pygame.draw.rect(screen, colors.get('light_wall'), [120, 0, 100, 500],0)
        pygame.draw.rect(screen, colors.get('white'), [220, 0, 20, 500],0)
        pygame.draw.rect(screen, colors.get('light_ground'), [240, 0, 100, 500],0)
        pygame.draw.rect(screen, colors.get('white'), [340, 0, 20, 500],0)
        pygame.draw.rect(screen, colors.get('light_ground'), [360, 0, 100, 500],0)
        pygame.draw.rect(screen, colors.get('white'), [460, 0, 20, 500],0)
        pygame.draw.rect(screen, colors.get('light_wall'), [480, 0, 100, 500],0)
        pygame.draw.rect(screen, colors.get('white'), [580, 0, 20, 500],0)
        pygame.draw.rect(screen, colors.get('dark_wall'), [600, 0, 100, 500],0)

        pygame.draw.line(screen, colors.get('light_wall'), [0,0], [100,100], 5)
        pygame.draw.ellipse(screen, colors.get('dark_ground'), [20,20,250,100], 2)
        
        #Blit
        pygame.display.flip()
        
        #60 FPS
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
