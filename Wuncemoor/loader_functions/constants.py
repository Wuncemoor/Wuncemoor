
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

    world_map_constants = {
        'width': 700,
        'height': 700,
        'octaves': 5,
        'persist': 0.5,
        'lacuna': 2.5,
        'scale': 0.0075,
        'moist_mod': 0.5,
        'temp_mod': 0.1,
        'water_level': 0.15  # -1 to 'water_level' is water, above to 1 is land
    }

    tiles = {
        'black': py.image.load('images\\black.png'),
        'dark_wall': py.image.load('images\\dark_wall.png'),
        'dark_ground': py.image.load('images\\dark_ground.png'),
        'light_wall': py.image.load('images\\light_wall.png'),
        'light_ground': py.image.load('images\\light_ground.png'),
        'light_grass': light_grass_dict(),
        'dark_grass': dark_grass_dict(),
        'light_road': road_dict(True),
        'dark_road': road_dict(False),
        'light_dirt': dirt_dict(True),
        'dark_dirt': dirt_dict(False),
        'light_deep': biome_dict('deep', True),
        'dark_deep': biome_dict('deep', False),
        'light_desert': biome_dict('desert', True),
        'dark_desert': biome_dict('desert', False),
        'light_forest': biome_dict('forest', True),
        'dark_forest': biome_dict('forest', False),
        'light_jungle': biome_dict('jungle', True),
        'dark_jungle': biome_dict('jungle', False),
        'light_plains': biome_dict('plains', True),
        'dark_plains': biome_dict('plains', False),
        'light_savannah': biome_dict('savannah', True),
        'dark_savannah': biome_dict('savannah', False),
        'light_shallow': biome_dict('shallow', True),
        'dark_shallow': biome_dict('shallow', False),
        'light_snow': biome_dict('snow', True),
        'dark_snow': biome_dict('snow', False),
        'light_taiga': biome_dict('taiga', True),
        'dark_taiga': biome_dict('taiga', False),
        'light_temprain': biome_dict('temprain', True),
        'dark_temprain': biome_dict('temprain', False),
        'light_tropicrain': biome_dict('tropicrain', True),
        'dark_tropicrain': biome_dict('tropicrain', False),
        'light_tundra': biome_dict('tundra', True),
        'dark_tundra': biome_dict('tundra', False),

    }

    options = {
        'grass': 13,
        'dirt': 9,
        'deep': 9,
        'desert': 9,
        'forest': 9,
        'jungle': 9,
        'plains': 9,
        'savannah': 9,
        'shallow': 9,
        'snow': 9,
        'taiga': 9,
        'temprain': 9,
        'tropicrain': 9,
        'tundra': 9,
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
        'tiles': tiles,
        'options': options,
        'fps': fps,
        'map_width': map_width,
        'map_height': map_height,
        'world_map_constants': world_map_constants,
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


def biome_dict(biome, visible):

    if visible:
        deep_dict = {
            'light_deep0': py.image.load('images\\world_map\\deep\\light_deep0.png'),
            'light_deep1': py.image.load('images\\world_map\\deep\\light_deep1.png'),
            'light_deep2': py.image.load('images\\world_map\\deep\\light_deep2.png'),
            'light_deep3': py.image.load('images\\world_map\\deep\\light_deep3.png'),
            'light_deep4': py.image.load('images\\world_map\\deep\\light_deep4.png'),
            'light_deep5': py.image.load('images\\world_map\\deep\\light_deep5.png'),
            'light_deep6': py.image.load('images\\world_map\\deep\\light_deep6.png'),
            'light_deep7': py.image.load('images\\world_map\\deep\\light_deep7.png'),
            'light_deep8': py.image.load('images\\world_map\\deep\\light_deep8.png'),
        }
        desert_dict = {
            'light_desert0': py.image.load('images\\world_map\\desert\\light_desert0.png'),
            'light_desert1': py.image.load('images\\world_map\\desert\\light_desert1.png'),
            'light_desert2': py.image.load('images\\world_map\\desert\\light_desert2.png'),
            'light_desert3': py.image.load('images\\world_map\\desert\\light_desert3.png'),
            'light_desert4': py.image.load('images\\world_map\\desert\\light_desert4.png'),
            'light_desert5': py.image.load('images\\world_map\\desert\\light_desert5.png'),
            'light_desert6': py.image.load('images\\world_map\\desert\\light_desert6.png'),
            'light_desert7': py.image.load('images\\world_map\\desert\\light_desert7.png'),
            'light_desert8': py.image.load('images\\world_map\\desert\\light_desert8.png'),
        }
        forest_dict = {
            'light_forest0': py.image.load('images\\world_map\\forest\\light_forest0.png'),
            'light_forest1': py.image.load('images\\world_map\\forest\\light_forest1.png'),
            'light_forest2': py.image.load('images\\world_map\\forest\\light_forest2.png'),
            'light_forest3': py.image.load('images\\world_map\\forest\\light_forest3.png'),
            'light_forest4': py.image.load('images\\world_map\\forest\\light_forest4.png'),
            'light_forest5': py.image.load('images\\world_map\\forest\\light_forest5.png'),
            'light_forest6': py.image.load('images\\world_map\\forest\\light_forest6.png'),
            'light_forest7': py.image.load('images\\world_map\\forest\\light_forest7.png'),
            'light_forest8': py.image.load('images\\world_map\\forest\\light_forest8.png'),
        }
        jungle_dict = {
            'light_jungle0': py.image.load('images\\world_map\\jungle\\light_jungle0.png'),
            'light_jungle1': py.image.load('images\\world_map\\jungle\\light_jungle1.png'),
            'light_jungle2': py.image.load('images\\world_map\\jungle\\light_jungle2.png'),
            'light_jungle3': py.image.load('images\\world_map\\jungle\\light_jungle3.png'),
            'light_jungle4': py.image.load('images\\world_map\\jungle\\light_jungle4.png'),
            'light_jungle5': py.image.load('images\\world_map\\jungle\\light_jungle5.png'),
            'light_jungle6': py.image.load('images\\world_map\\jungle\\light_jungle6.png'),
            'light_jungle7': py.image.load('images\\world_map\\jungle\\light_jungle7.png'),
            'light_jungle8': py.image.load('images\\world_map\\jungle\\light_jungle8.png'),
        }
        plains_dict = {
            'light_plains0': py.image.load('images\\world_map\\plains\\light_plains0.png'),
            'light_plains1': py.image.load('images\\world_map\\plains\\light_plains1.png'),
            'light_plains2': py.image.load('images\\world_map\\plains\\light_plains2.png'),
            'light_plains3': py.image.load('images\\world_map\\plains\\light_plains3.png'),
            'light_plains4': py.image.load('images\\world_map\\plains\\light_plains4.png'),
            'light_plains5': py.image.load('images\\world_map\\plains\\light_plains5.png'),
            'light_plains6': py.image.load('images\\world_map\\plains\\light_plains6.png'),
            'light_plains7': py.image.load('images\\world_map\\plains\\light_plains7.png'),
            'light_plains8': py.image.load('images\\world_map\\plains\\light_plains8.png'),
        }

        savannah_dict = {
            'light_savannah0': py.image.load('images\\world_map\\savannah\\light_savannah0.png'),
            'light_savannah1': py.image.load('images\\world_map\\savannah\\light_savannah1.png'),
            'light_savannah2': py.image.load('images\\world_map\\savannah\\light_savannah2.png'),
            'light_savannah3': py.image.load('images\\world_map\\savannah\\light_savannah3.png'),
            'light_savannah4': py.image.load('images\\world_map\\savannah\\light_savannah4.png'),
            'light_savannah5': py.image.load('images\\world_map\\savannah\\light_savannah5.png'),
            'light_savannah6': py.image.load('images\\world_map\\savannah\\light_savannah6.png'),
            'light_savannah7': py.image.load('images\\world_map\\savannah\\light_savannah7.png'),
            'light_savannah8': py.image.load('images\\world_map\\savannah\\light_savannah8.png'),
        }
        shallow_dict = {
            'light_shallow0': py.image.load('images\\world_map\\shallow\\light_shallow0.png'),
            'light_shallow1': py.image.load('images\\world_map\\shallow\\light_shallow1.png'),
            'light_shallow2': py.image.load('images\\world_map\\shallow\\light_shallow2.png'),
            'light_shallow3': py.image.load('images\\world_map\\shallow\\light_shallow3.png'),
            'light_shallow4': py.image.load('images\\world_map\\shallow\\light_shallow4.png'),
            'light_shallow5': py.image.load('images\\world_map\\shallow\\light_shallow5.png'),
            'light_shallow6': py.image.load('images\\world_map\\shallow\\light_shallow6.png'),
            'light_shallow7': py.image.load('images\\world_map\\shallow\\light_shallow7.png'),
            'light_shallow8': py.image.load('images\\world_map\\shallow\\light_shallow8.png'),
        }
        snow_dict = {
            'light_snow0': py.image.load('images\\world_map\\snow\\light_snow0.png'),
            'light_snow1': py.image.load('images\\world_map\\snow\\light_snow1.png'),
            'light_snow2': py.image.load('images\\world_map\\snow\\light_snow2.png'),
            'light_snow3': py.image.load('images\\world_map\\snow\\light_snow3.png'),
            'light_snow4': py.image.load('images\\world_map\\snow\\light_snow4.png'),
            'light_snow5': py.image.load('images\\world_map\\snow\\light_snow5.png'),
            'light_snow6': py.image.load('images\\world_map\\snow\\light_snow6.png'),
            'light_snow7': py.image.load('images\\world_map\\snow\\light_snow7.png'),
            'light_snow8': py.image.load('images\\world_map\\snow\\light_snow8.png'),
        }
        taiga_dict = {
            'light_taiga0': py.image.load('images\\world_map\\taiga\\light_taiga0.png'),
            'light_taiga1': py.image.load('images\\world_map\\taiga\\light_taiga1.png'),
            'light_taiga2': py.image.load('images\\world_map\\taiga\\light_taiga2.png'),
            'light_taiga3': py.image.load('images\\world_map\\taiga\\light_taiga3.png'),
            'light_taiga4': py.image.load('images\\world_map\\taiga\\light_taiga4.png'),
            'light_taiga5': py.image.load('images\\world_map\\taiga\\light_taiga5.png'),
            'light_taiga6': py.image.load('images\\world_map\\taiga\\light_taiga6.png'),
            'light_taiga7': py.image.load('images\\world_map\\taiga\\light_taiga7.png'),
            'light_taiga8': py.image.load('images\\world_map\\taiga\\light_taiga8.png'),
        }
        temprain_dict = {
            'light_temprain0': py.image.load('images\\world_map\\temprain\\light_temprain0.png'),
            'light_temprain1': py.image.load('images\\world_map\\temprain\\light_temprain1.png'),
            'light_temprain2': py.image.load('images\\world_map\\temprain\\light_temprain2.png'),
            'light_temprain3': py.image.load('images\\world_map\\temprain\\light_temprain3.png'),
            'light_temprain4': py.image.load('images\\world_map\\temprain\\light_temprain4.png'),
            'light_temprain5': py.image.load('images\\world_map\\temprain\\light_temprain5.png'),
            'light_temprain6': py.image.load('images\\world_map\\temprain\\light_temprain6.png'),
            'light_temprain7': py.image.load('images\\world_map\\temprain\\light_temprain7.png'),
            'light_temprain8': py.image.load('images\\world_map\\temprain\\light_temprain8.png'),
        }
        tropicrain_dict = {
            'light_tropicrain0': py.image.load('images\\world_map\\tropicrain\\light_tropicrain0.png'),
            'light_tropicrain1': py.image.load('images\\world_map\\tropicrain\\light_tropicrain1.png'),
            'light_tropicrain2': py.image.load('images\\world_map\\tropicrain\\light_tropicrain2.png'),
            'light_tropicrain3': py.image.load('images\\world_map\\tropicrain\\light_tropicrain3.png'),
            'light_tropicrain4': py.image.load('images\\world_map\\tropicrain\\light_tropicrain4.png'),
            'light_tropicrain5': py.image.load('images\\world_map\\tropicrain\\light_tropicrain5.png'),
            'light_tropicrain6': py.image.load('images\\world_map\\tropicrain\\light_tropicrain6.png'),
            'light_tropicrain7': py.image.load('images\\world_map\\tropicrain\\light_tropicrain7.png'),
            'light_tropicrain8': py.image.load('images\\world_map\\tropicrain\\light_tropicrain8.png'),
        }
        tundra_dict = {
            'light_tundra0': py.image.load('images\\world_map\\tundra\\light_tundra0.png'),
            'light_tundra1': py.image.load('images\\world_map\\tundra\\light_tundra1.png'),
            'light_tundra2': py.image.load('images\\world_map\\tundra\\light_tundra2.png'),
            'light_tundra3': py.image.load('images\\world_map\\tundra\\light_tundra3.png'),
            'light_tundra4': py.image.load('images\\world_map\\tundra\\light_tundra4.png'),
            'light_tundra5': py.image.load('images\\world_map\\tundra\\light_tundra5.png'),
            'light_tundra6': py.image.load('images\\world_map\\tundra\\light_tundra6.png'),
            'light_tundra7': py.image.load('images\\world_map\\tundra\\light_tundra7.png'),
            'light_tundra8': py.image.load('images\\world_map\\tundra\\light_tundra8.png'),
        }
    else:
        deep_dict = {
            'dark_deep0': py.image.load('images\\world_map\\deep\\dark_deep0.png'),
            'dark_deep1': py.image.load('images\\world_map\\deep\\dark_deep1.png'),
            'dark_deep2': py.image.load('images\\world_map\\deep\\dark_deep2.png'),
            'dark_deep3': py.image.load('images\\world_map\\deep\\dark_deep3.png'),
            'dark_deep4': py.image.load('images\\world_map\\deep\\dark_deep4.png'),
            'dark_deep5': py.image.load('images\\world_map\\deep\\dark_deep5.png'),
            'dark_deep6': py.image.load('images\\world_map\\deep\\dark_deep6.png'),
            'dark_deep7': py.image.load('images\\world_map\\deep\\dark_deep7.png'),
            'dark_deep8': py.image.load('images\\world_map\\deep\\dark_deep8.png'),
        }
        desert_dict = {
            'dark_desert0': py.image.load('images\\world_map\\desert\\dark_desert0.png'),
            'dark_desert1': py.image.load('images\\world_map\\desert\\dark_desert1.png'),
            'dark_desert2': py.image.load('images\\world_map\\desert\\dark_desert2.png'),
            'dark_desert3': py.image.load('images\\world_map\\desert\\dark_desert3.png'),
            'dark_desert4': py.image.load('images\\world_map\\desert\\dark_desert4.png'),
            'dark_desert5': py.image.load('images\\world_map\\desert\\dark_desert5.png'),
            'dark_desert6': py.image.load('images\\world_map\\desert\\dark_desert6.png'),
            'dark_desert7': py.image.load('images\\world_map\\desert\\dark_desert7.png'),
            'dark_desert8': py.image.load('images\\world_map\\desert\\dark_desert8.png'),
        }
        forest_dict = {
            'dark_forest0': py.image.load('images\\world_map\\forest\\dark_forest0.png'),
            'dark_forest1': py.image.load('images\\world_map\\forest\\dark_forest1.png'),
            'dark_forest2': py.image.load('images\\world_map\\forest\\dark_forest2.png'),
            'dark_forest3': py.image.load('images\\world_map\\forest\\dark_forest3.png'),
            'dark_forest4': py.image.load('images\\world_map\\forest\\dark_forest4.png'),
            'dark_forest5': py.image.load('images\\world_map\\forest\\dark_forest5.png'),
            'dark_forest6': py.image.load('images\\world_map\\forest\\dark_forest6.png'),
            'dark_forest7': py.image.load('images\\world_map\\forest\\dark_forest7.png'),
            'dark_forest8': py.image.load('images\\world_map\\forest\\dark_forest8.png'),
        }
        jungle_dict = {
            'dark_jungle0': py.image.load('images\\world_map\\jungle\\dark_jungle0.png'),
            'dark_jungle1': py.image.load('images\\world_map\\jungle\\dark_jungle1.png'),
            'dark_jungle2': py.image.load('images\\world_map\\jungle\\dark_jungle2.png'),
            'dark_jungle3': py.image.load('images\\world_map\\jungle\\dark_jungle3.png'),
            'dark_jungle4': py.image.load('images\\world_map\\jungle\\dark_jungle4.png'),
            'dark_jungle5': py.image.load('images\\world_map\\jungle\\dark_jungle5.png'),
            'dark_jungle6': py.image.load('images\\world_map\\jungle\\dark_jungle6.png'),
            'dark_jungle7': py.image.load('images\\world_map\\jungle\\dark_jungle7.png'),
            'dark_jungle8': py.image.load('images\\world_map\\jungle\\dark_jungle8.png'),
        }
        plains_dict = {
            'dark_plains0': py.image.load('images\\world_map\\plains\\dark_plains0.png'),
            'dark_plains1': py.image.load('images\\world_map\\plains\\dark_plains1.png'),
            'dark_plains2': py.image.load('images\\world_map\\plains\\dark_plains2.png'),
            'dark_plains3': py.image.load('images\\world_map\\plains\\dark_plains3.png'),
            'dark_plains4': py.image.load('images\\world_map\\plains\\dark_plains4.png'),
            'dark_plains5': py.image.load('images\\world_map\\plains\\dark_plains5.png'),
            'dark_plains6': py.image.load('images\\world_map\\plains\\dark_plains6.png'),
            'dark_plains7': py.image.load('images\\world_map\\plains\\dark_plains7.png'),
            'dark_plains8': py.image.load('images\\world_map\\plains\\dark_plains8.png'),
        }
        savannah_dict = {
            'dark_savannah0': py.image.load('images\\world_map\\savannah\\dark_savannah0.png'),
            'dark_savannah1': py.image.load('images\\world_map\\savannah\\dark_savannah1.png'),
            'dark_savannah2': py.image.load('images\\world_map\\savannah\\dark_savannah2.png'),
            'dark_savannah3': py.image.load('images\\world_map\\savannah\\dark_savannah3.png'),
            'dark_savannah4': py.image.load('images\\world_map\\savannah\\dark_savannah4.png'),
            'dark_savannah5': py.image.load('images\\world_map\\savannah\\dark_savannah5.png'),
            'dark_savannah6': py.image.load('images\\world_map\\savannah\\dark_savannah6.png'),
            'dark_savannah7': py.image.load('images\\world_map\\savannah\\dark_savannah7.png'),
            'dark_savannah8': py.image.load('images\\world_map\\savannah\\dark_savannah8.png'),
        }
        shallow_dict = {
            'dark_shallow0': py.image.load('images\\world_map\\shallow\\dark_shallow0.png'),
            'dark_shallow1': py.image.load('images\\world_map\\shallow\\dark_shallow1.png'),
            'dark_shallow2': py.image.load('images\\world_map\\shallow\\dark_shallow2.png'),
            'dark_shallow3': py.image.load('images\\world_map\\shallow\\dark_shallow3.png'),
            'dark_shallow4': py.image.load('images\\world_map\\shallow\\dark_shallow4.png'),
            'dark_shallow5': py.image.load('images\\world_map\\shallow\\dark_shallow5.png'),
            'dark_shallow6': py.image.load('images\\world_map\\shallow\\dark_shallow6.png'),
            'dark_shallow7': py.image.load('images\\world_map\\shallow\\dark_shallow7.png'),
            'dark_shallow8': py.image.load('images\\world_map\\shallow\\dark_shallow8.png'),
        }
        snow_dict = {
            'dark_snow0': py.image.load('images\\world_map\\snow\\dark_snow0.png'),
            'dark_snow1': py.image.load('images\\world_map\\snow\\dark_snow1.png'),
            'dark_snow2': py.image.load('images\\world_map\\snow\\dark_snow2.png'),
            'dark_snow3': py.image.load('images\\world_map\\snow\\dark_snow3.png'),
            'dark_snow4': py.image.load('images\\world_map\\snow\\dark_snow4.png'),
            'dark_snow5': py.image.load('images\\world_map\\snow\\dark_snow5.png'),
            'dark_snow6': py.image.load('images\\world_map\\snow\\dark_snow6.png'),
            'dark_snow7': py.image.load('images\\world_map\\snow\\dark_snow7.png'),
            'dark_snow8': py.image.load('images\\world_map\\snow\\dark_snow8.png'),
        }
        taiga_dict = {
            'dark_taiga0': py.image.load('images\\world_map\\taiga\\dark_taiga0.png'),
            'dark_taiga1': py.image.load('images\\world_map\\taiga\\dark_taiga1.png'),
            'dark_taiga2': py.image.load('images\\world_map\\taiga\\dark_taiga2.png'),
            'dark_taiga3': py.image.load('images\\world_map\\taiga\\dark_taiga3.png'),
            'dark_taiga4': py.image.load('images\\world_map\\taiga\\dark_taiga4.png'),
            'dark_taiga5': py.image.load('images\\world_map\\taiga\\dark_taiga5.png'),
            'dark_taiga6': py.image.load('images\\world_map\\taiga\\dark_taiga6.png'),
            'dark_taiga7': py.image.load('images\\world_map\\taiga\\dark_taiga7.png'),
            'dark_taiga8': py.image.load('images\\world_map\\taiga\\dark_taiga8.png'),
        }
        temprain_dict = {
            'dark_temprain0': py.image.load('images\\world_map\\temprain\\dark_temprain0.png'),
            'dark_temprain1': py.image.load('images\\world_map\\temprain\\dark_temprain1.png'),
            'dark_temprain2': py.image.load('images\\world_map\\temprain\\dark_temprain2.png'),
            'dark_temprain3': py.image.load('images\\world_map\\temprain\\dark_temprain3.png'),
            'dark_temprain4': py.image.load('images\\world_map\\temprain\\dark_temprain4.png'),
            'dark_temprain5': py.image.load('images\\world_map\\temprain\\dark_temprain5.png'),
            'dark_temprain6': py.image.load('images\\world_map\\temprain\\dark_temprain6.png'),
            'dark_temprain7': py.image.load('images\\world_map\\temprain\\dark_temprain7.png'),
            'dark_temprain8': py.image.load('images\\world_map\\temprain\\dark_temprain8.png'),
        }
        tropicrain_dict = {
            'dark_tropicrain0': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain0.png'),
            'dark_tropicrain1': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain1.png'),
            'dark_tropicrain2': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain2.png'),
            'dark_tropicrain3': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain3.png'),
            'dark_tropicrain4': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain4.png'),
            'dark_tropicrain5': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain5.png'),
            'dark_tropicrain6': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain6.png'),
            'dark_tropicrain7': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain7.png'),
            'dark_tropicrain8': py.image.load('images\\world_map\\tropicrain\\dark_tropicrain8.png'),
        }
        tundra_dict = {
            'dark_tundra0': py.image.load('images\\world_map\\tundra\\dark_tundra0.png'),
            'dark_tundra1': py.image.load('images\\world_map\\tundra\\dark_tundra1.png'),
            'dark_tundra2': py.image.load('images\\world_map\\tundra\\dark_tundra2.png'),
            'dark_tundra3': py.image.load('images\\world_map\\tundra\\dark_tundra3.png'),
            'dark_tundra4': py.image.load('images\\world_map\\tundra\\dark_tundra4.png'),
            'dark_tundra5': py.image.load('images\\world_map\\tundra\\dark_tundra5.png'),
            'dark_tundra6': py.image.load('images\\world_map\\tundra\\dark_tundra6.png'),
            'dark_tundra7': py.image.load('images\\world_map\\tundra\\dark_tundra7.png'),
            'dark_tundra8': py.image.load('images\\world_map\\tundra\\dark_tundra8.png'),
        }
    biomes_dict = {
        'deep': deep_dict,
        'desert': desert_dict,
        'forest': forest_dict,
        'jungle': jungle_dict,
        'plains': plains_dict,
        'savannah': savannah_dict,
        'shallow': shallow_dict,
        'snow': snow_dict,
        'taiga': taiga_dict,
        'temprain': temprain_dict,
        'tropicrain': tropicrain_dict,
        'tundra': tundra_dict,
    }

    return biomes_dict.get(biome)

