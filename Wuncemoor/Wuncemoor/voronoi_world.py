import tcod as libtcod
from PIL import Image
from loader_functions.initialize_new_game import get_constants
import random
import math

class WorldMap:
    
    def __init__(self, width, height, num_cells):
    
        self.width = width
        self.height = height
        self.num_cells = num_cells
        
    def make_tiles(self):
        
        tiles = [[Tile(True) for y in range(self.height)] for x in range(width)]
            
        return tiles
        
    

    def make_voronoi(self, num_cells):
        
        image = Image.new('RGB', (self.width, self.height))
        putpixel = image.putpixel

        imgx, imgy = image.size
        
        nx = []
        ny = []
        nr = []
        ng = []
        nb = []
        
        for i in range(num_cells):
            nx.append(random.randrange(imgx))
            ny.append(random.randrange(imgy))
            nr.append(random.randrange(256))
            ng.append(random.randrange(256))
            nb.append(random.randrange(256))
        
        for y in range(imgy):
            for x in range(imgx):
                dmin = math.hypot(imgx - 1, imgy - 1)
                nodes = -1
                nodegroups = []
                for i in range(num_cells):
                    d = math.hypot(nx[i]-x, ny[i]-y)
                    if d < dmin:
                        dmin = d
                        nodes = i
                nodegroups.append([nodes, x, y]) 
                putpixel((x, y), (nr[nodes], ng[nodes], nb[nodes]))

                
        return nodegroups
                        
                        
        image.save('Voronoitest.png', 'PNG')
        image.show()
        
def __main__:

    constants = get_constants()

    libtcod.console_set_custom_font(r'C:\Users\penic\Desktop\Wuncemoor\arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(constants['screen_width'], constants['screen_height'], constants['window_title'], False)
    
    con = libtcod.console_new(constants['screen_width'],constants['screen_height'])
    panel = libtcod.console_new(constants['screen_width'], constants['panel_height'])

    show_main_menu = True
    show_load_error_message = False
    
    main_menu_background_image = libtcod.image_load(r'C:\Users\penic\Desktop\Wuncemoor\the_fall_of_icarus.jpg')

    key = libtcod.Key()
    mouse = libtcod.Mouse()
   
    while not libtcod.console_is_window_closed():
    
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

        
if __name__ == '__main__':
     main()   
map = WorldMap(100, 100, 25)
