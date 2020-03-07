import math
import tcod as libtcod
from PIL import Image
from render_functions import RenderOrder
from components.item import Item
#Generic object representing PC and NPC, items, etc
class Entity:

    #Creation
    def __init__(self, x, y, color, blocks=False, render_order=RenderOrder.CORPSE, combatant=None, item=None, stairs=None):
        self.x = x
        self.y = y
        self.color = color
        self.blocks = blocks
        self.render_order = render_order
        self.combatant = combatant
        self.item = item
        self.stairs = stairs
        self.name = None
        self.image = None
        
        if self.combatant:
            self.combatant.owner = self
            self.name = self.combatant.name
            self.image = self.combatant.image
            if self.combatant.ai:
                self.combatant.ai.owner = self
            if self.combatant.level:
                self.combatant.level.owner = self
            if self.combatant.inventory:
                self.combatant.inventory.owner = self
            
            
        if self.item:
            self.item.owner = self
            self.name = self.item.name
            self.image = self.item.image
            if self.item.equippable:
                self.item.equippable.owner = self
            if self.item.useable:
                self.item.useable.owner = self
            

        if self.stairs:
            self.stairs.owner = self
            self.name = self.stairs.name
            self.image = self.stairs.image

        
    #Move the entity
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_towards(self, target_x, target_y, game_map, entities):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        
        if not (game_map.is_blocked(self.x + dx, self.y + dy) or get_blocking_entities_at_location(entities, self.x + dx, self.y + dy)):
            self.move(dx,dy)
            
    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
            
    def move_astar(self, target, entities, game_map):
        # Create a FOV map that has the dimensions of the map
        fov = libtcod.map_new(game_map.width, game_map.height)

        # Scan the current map each turn and set all the walls as unwalkable
        for y1 in range(game_map.height):
            for x1 in range(game_map.width):
                libtcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].block_sight,
                                           not game_map.tiles[x1][y1].blocked)

        # Scan all the objects to see if there are objects that must be navigated around
        # Check also that the object isn't self or the target (so that the start and the end points are free)
        # The AI class handles the situation if self is next to the target so it will not use this A* function anyway
        for entity in entities:
            if entity.blocks and entity != self and entity != target:
                # Set the tile as a wall so it must be navigated around
                libtcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Allocate a A* path
        my_path = libtcod.path_new_using_map(fov, 1.41)

        # Compute the path between self's coordinates and the target's coordinates
        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than 25 tiles
        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            # Find the next coordinates in the computed full path
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                # Set self's coordinates to the next path tile
                self.x = x
                self.y = y
        else:
            # Keep the old move function as a backup so that if there are no paths (for example another monster blocks a corridor)
            # it will still try to move towards the player (closer to the corridor opening)
            self.move_towards(target.x, target.y, game_map, entities)

            # Delete the path to free memory
        libtcod.path_delete(my_path) 
    
    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
        
def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity
        
    return None
    