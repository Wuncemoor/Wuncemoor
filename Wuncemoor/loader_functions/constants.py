import tcod as libtcod
import pygame
from PIL import Image

def get_constants():
    window_title = 'Wuncemoor: The Eternal Dream'
    
    screen_width = 1280
    screen_height = 720
    cscreen_width = 1280
    cscreen_height = 592
    rscreen_width = 300
    rscreen_height = 128
    mscreen_width = 980
    mscreen_height = 128
    
    bar_width = 300
    panel_height = 8
    panel_y = screen_height - panel_height
    
    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height -1
    map_width = 80
    map_height = 37


    fps = 60
    alpha_width = 150
    alpha_height = 100
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 3
    
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10000
    
    max_monsters_per_room = 3
    max_items_per_room = 2
    
    tiles = {
        'black': pygame.image.load(r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\black.png'),
        'dark_wall': pygame.image.load(r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\dark_wall.png'),
        'dark_ground': pygame.image.load(r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\dark_ground.png'),
        'light_wall': pygame.image.load(r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\light_wall.png'),
        'light_ground': pygame.image.load(r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\light_ground.png'),
        }
    
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50),
        'grass': libtcod.Color(0, 191, 0),
        'water': libtcod.Color(0, 191, 191)
        }
        
    pycolors = {
          'TAIGA' : pygame.Color(0,75,0),
          'FOREST' : pygame.Color(0,135,0),
          'JUNGLE' : pygame.Color(69,65,35),
          'TROPICRAIN' : pygame.Color(0,255,0),
          'TEMPRAIN' : pygame.Color(90,180,0),
          'SHALLOW' : pygame.Color(100,175,255),
          'BLUE' : pygame.Color(0,0,255),
          'DEEP' : pygame.Color(0,0,175),
          'WHITE' : pygame.Color(255,255,255),
          'BLACK' : pygame.Color(0,0,0),
          'BROWN' : pygame.Color(162,42,42),
          'GREY' : pygame.Color(84,84,84),
          'TUNDRA' : pygame.Color(173, 216, 230),
          'PLAINS' : pygame.Color(245,222,179),
          'RED' : pygame.Color(255,0,0),
          'ORANGE' : pygame.Color(255,165,0),
          'YELLOW' : pygame.Color(255,255,0),
          'SAVANNAH' : pygame.Color(128,128,0),
          'DESERT' : pygame.Color(213,164,117),
          'OLIVE' : pygame.Color(128,128,0),
          }
    
    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'cscreen_width': cscreen_width,
        'cscreen_height': cscreen_height,
        'rscreen_width': rscreen_width,
        'rscreen_height': rscreen_height,
        'mscreen_width': mscreen_width,
        'mscreen_height': mscreen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'alpha_width': alpha_width,
        'alpha_height': alpha_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors,
        'pycolors': pycolors,
        'tiles': tiles,
        'fps': fps,
        'map_width': map_width,
        'map_height': map_height,
        }
    return constants
