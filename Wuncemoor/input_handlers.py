import tcod as libtcod

def handle_keys(key):
    key_char = chr(key.c)
    #Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'move': (0,-1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'move': (-1,0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {'move': (1,0)}
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move' (1, 1)}
    
    #Alt+Enter = Fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    #Exit the game    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
        
    #No key
    return {}
    