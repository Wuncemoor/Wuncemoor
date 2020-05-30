
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
    start_town_width = 80
    start_town_height = 37

    room_max_size = 10
    room_min_size = 6
    max_rooms = 3

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 50

    max_monsters_per_room = 3
    max_items_per_room = 2

    world_map_constants = {
        'width': 150,
        'height': 150,
        'octaves': 5,
        'persist': 0.5,
        'lacuna': 2.5,
        'scale': 0.0075,
        'moist_mod': 0.5,
        'temp_mod': 0.1,
        'water_level': 0.15  # -1 to 'water_level' is water, above to 1 is land
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
        'start_town_width': start_town_width,
        'start_town_height': start_town_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'fps': fps,
        'map_width': map_width,
        'map_height': map_height,
        'world_map_constants': world_map_constants,


    }

    return constants
