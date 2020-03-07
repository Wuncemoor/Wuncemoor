from random_utils import from_dungeon_level

def get_mob_chances(d_type, d_level):

    if d_type == ('directed_dungeon' or 'start_dungeon'):
    
        monster_chances = { 
            'orc' : 80,
            'goblin' : 50,
            'troll': from_dungeon_level([[20,1], [40,2], [80,3]], d_level)
            }
    elif d_type == 'goblin_cave':
    
        monster_chances = {
            'goblin' : 50
            }
            
    return monster_chances
        
        
        
        
        
        