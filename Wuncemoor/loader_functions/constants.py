import tcod as libtcod
import pygame as py


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
    message_height = panel_height - 1
    map_width = 80
    map_height = 37

    fps = 60
    alpha_width = 80
    alpha_height = 37

    room_max_size = 10
    room_min_size = 6
    max_rooms = 3

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 50

    max_monsters_per_room = 3
    max_items_per_room = 2

    tiles = {
        'black': py.image.load('images\\black.png'),
        'dark_wall': py.image.load('images\\dark_wall.png'),
        'dark_ground': py.image.load('images\\dark_ground.png'),
        'light_wall': py.image.load('images\\light_wall.png'),
        'light_ground': py.image.load('images\\light_ground.png'),
        'light_road': py.image.load('images\\light_road.png'),
        'dark_road': py.image.load('images\\dark_road.png'),
        'light_grass': light_grass_dict(),
        'dark_grass': dark_grass_dict(),
        'light_road': road_dict(True),
        'dark_road': road_dict(False),
        'light_dirt': dirt_dict(True),
        'dark_dirt': dirt_dict(False),
    }

    options = {
        'grass': 13,
        'dirt': 9,
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
        'TAIGA': py.Color(0, 75, 0),
        'FOREST': py.Color(0, 135, 0),
        'JUNGLE': py.Color(69, 65, 35),
        'TROPICRAIN': py.Color(0, 255, 0),
        'TEMPRAIN': py.Color(90, 180, 0),
        'SHALLOW': py.Color(100, 175, 255),
        'BLUE': py.Color(0, 0, 255),
        'DEEP': py.Color(0, 0, 175),
        'WHITE': py.Color(255, 255, 255),
        'BLACK': py.Color(0, 0, 0),
        'BROWN': py.Color(162, 42, 42),
        'GREY': py.Color(84, 84, 84),
        'TUNDRA': py.Color(173, 216, 230),
        'PLAINS': py.Color(245, 222, 179),
        'RED': py.Color(255, 0, 0),
        'ORANGE': py.Color(255, 165, 0),
        'YELLOW': py.Color(255, 255, 0),
        'SAVANNAH': py.Color(128, 128, 0),
        'DESERT': py.Color(213, 164, 117),
        'OLIVE': py.Color(128, 128, 0),
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
        'options': options,
        'fps': fps,
        'map_width': map_width,
        'map_height': map_height,
    }
    return constants


def light_grass_dict():
    light_grass_dict = {
        'light_grass0': py.image.load('images\\grass\\light_grass00.png'),
        'light_grass1': py.image.load('images\\grass\\light_grass01.png'),
        'light_grass2': py.image.load('images\\grass\\light_grass02.png'),
        'light_grass3': py.image.load('images\\grass\\light_grass03.png'),
        'light_grass4': py.image.load('images\\grass\\light_grass04.png'),
        'light_grass5': py.image.load('images\\grass\\light_grass05.png'),
        'light_grass6': py.image.load('images\\grass\\light_grass06.png'),
        'light_grass7': py.image.load('images\\grass\\light_grass07.png'),
        'light_grass8': py.image.load('images\\grass\\light_grass08.png'),
        'light_grass9': py.image.load('images\\grass\\light_grass09.png'),
        'light_grass10': py.image.load('images\\grass\\light_grass10.png'),
        'light_grass11': py.image.load('images\\grass\\light_grass11.png'),
        'light_grass12': py.image.load('images\\grass\\light_grass12.png'),
    }
    return light_grass_dict


def dark_grass_dict():
    dark_grass_dict = {
        'dark_grass0': py.image.load('images\\grass\\dark_grass00.png'),
        'dark_grass1': py.image.load('images\\grass\\dark_grass01.png'),
        'dark_grass2': py.image.load('images\\grass\\dark_grass02.png'),
        'dark_grass3': py.image.load('images\\grass\\dark_grass03.png'),
        'dark_grass4': py.image.load('images\\grass\\dark_grass04.png'),
        'dark_grass5': py.image.load('images\\grass\\dark_grass05.png'),
        'dark_grass6': py.image.load('images\\grass\\dark_grass06.png'),
        'dark_grass7': py.image.load('images\\grass\\dark_grass07.png'),
        'dark_grass8': py.image.load('images\\grass\\dark_grass08.png'),
        'dark_grass9': py.image.load('images\\grass\\dark_grass09.png'),
        'dark_grass10': py.image.load('images\\grass\\dark_grass10.png'),
        'dark_grass11': py.image.load('images\\grass\\dark_grass11.png'),
        'dark_grass12': py.image.load('images\\grass\\dark_grass12.png'),
    }
    return dark_grass_dict


def road_dict(vis):
    if vis:
        road_dict = {
            '00001011': py.image.load('images\\road\\light_road00001011.png'),
            '00010110': py.image.load('images\\road\\light_road00010110.png'),
            '00011111': py.image.load('images\\road\\light_road00011111.png'),
            '01101000': py.image.load('images\\road\\light_road01101000.png'),
            '01101011': py.image.load('images\\road\\light_road01101011.png'),
            '01111111': py.image.load('images\\road\\light_road01111111.png'),
            '11010000': py.image.load('images\\road\\light_road11010000.png'),
            '11010110': py.image.load('images\\road\\light_road11010110.png'),
            '11011011': py.image.load('images\\road\\light_road11011011.png'),
            '11111000': py.image.load('images\\road\\light_road11111000.png'),
            '11111110': py.image.load('images\\road\\light_road11111110.png'),
            '11111111': py.image.load('images\\road\\light_road11111111.png'),

        }
    else:
        road_dict = {
            '00001011': py.image.load('images\\road\\dark_road00001011.png'),
            '00010110': py.image.load('images\\road\\dark_road00010110.png'),
            '00011111': py.image.load('images\\road\\dark_road00011111.png'),
            '01101000': py.image.load('images\\road\\dark_road01101000.png'),
            '01101011': py.image.load('images\\road\\dark_road01101011.png'),
            '01111111': py.image.load('images\\road\\dark_road01111111.png'),
            '11010000': py.image.load('images\\road\\dark_road11010000.png'),
            '11010110': py.image.load('images\\road\\dark_road11010110.png'),
            '11011011': py.image.load('images\\road\\dark_road11011011.png'),
            '11111000': py.image.load('images\\road\\dark_road11111000.png'),
            '11111110': py.image.load('images\\road\\dark_road11111110.png'),
            '11111111': py.image.load('images\\road\\dark_road11111111.png'),

        }

    return road_dict


def dirt_dict(visible):
    if visible:
        dirt_dict = {
            'light_dirt0': py.image.load('images\\dirt\\light_dirt0.png'),
            'light_dirt1': py.image.load('images\\dirt\\light_dirt1.png'),
            'light_dirt2': py.image.load('images\\dirt\\light_dirt2.png'),
            'light_dirt3': py.image.load('images\\dirt\\light_dirt3.png'),
            'light_dirt4': py.image.load('images\\dirt\\light_dirt4.png'),
            'light_dirt5': py.image.load('images\\dirt\\light_dirt5.png'),
            'light_dirt6': py.image.load('images\\dirt\\light_dirt6.png'),
            'light_dirt7': py.image.load('images\\dirt\\light_dirt7.png'),
            'light_dirt8': py.image.load('images\\dirt\\light_dirt8.png'),
        }
    else:
        dirt_dict = {
            'dark_dirt0': py.image.load('images\\dirt\\dark_dirt0.png'),
            'dark_dirt1': py.image.load('images\\dirt\\dark_dirt1.png'),
            'dark_dirt2': py.image.load('images\\dirt\\dark_dirt2.png'),
            'dark_dirt3': py.image.load('images\\dirt\\dark_dirt3.png'),
            'dark_dirt4': py.image.load('images\\dirt\\dark_dirt4.png'),
            'dark_dirt5': py.image.load('images\\dirt\\dark_dirt5.png'),
            'dark_dirt6': py.image.load('images\\dirt\\dark_dirt6.png'),
            'dark_dirt7': py.image.load('images\\dirt\\dark_dirt7.png'),
            'dark_dirt8': py.image.load('images\\dirt\\dark_dirt8.png'),
        }
    return dirt_dict
