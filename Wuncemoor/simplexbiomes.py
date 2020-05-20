from opensimplex import OpenSimplex
import pygame
import random

heightmesh = OpenSimplex(seed=random.randint(1,1000000))
heightmesh2 = OpenSimplex(seed=random.randint(1,1000000))
heightmesh3 = OpenSimplex(seed=random.randint(1,1000000))
moistmesh = OpenSimplex(seed=random.randint(1,1000000))
moistmesh2 = OpenSimplex(seed=random.randint(1,1000000))
moistmesh3 = OpenSimplex(seed=random.randint(1,1000000))

TAIGA = pygame.Color(0,75,0)
FOREST = pygame.Color(0,135,0)
JUNGLE = pygame.Color(69,65,35)
TROPICRAIN = pygame.Color(0,255,0)
TEMPRAIN = pygame.Color(90,180,0)
SHALLOW = pygame.Color(100,175,255)
BLUE = pygame.Color(0,0,255)
DEEP = pygame.Color(0,0,175)
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
BROWN = pygame.Color(162,42,42)
GREY = pygame.Color(84,84,84)
TUNDRA = pygame.Color(173, 216, 230)
PLAINS = pygame.Color(245,222,179)
RED = pygame.Color(255,0,0)
ORANGE = pygame.Color(255,165,0)
YELLOW = pygame.Color(255,255,0)
SAVANNAH = pygame.Color(128,128,0)
DESERT = pygame.Color(213,164,117)

OLIVE = pygame.Color(128,128,0)

def moisture(table, moist_level):
    for (value, level) in table:
        if moist_level >= level:
            return value
    return -1 
    
def get_moistlist(temp):
    
        
    dict = {
        'very_hot': [(TROPICRAIN, .6), (JUNGLE, .2), (SAVANNAH, 0),(DESERT, -10)],
        'hot': [(TEMPRAIN, .5), (FOREST, .3),(SAVANNAH, 0), (DESERT, -10)],
        'warm': [(TEMPRAIN, .65), (FOREST, .3), (SAVANNAH, 0), (PLAINS, -.25), (DESERT, -10)],
        'cool': [(TEMPRAIN, .7), (FOREST, .2), (SAVANNAH, -.2), (PLAINS, -.5), (DESERT, -10)],
        'cold': [(TAIGA, 0), (PLAINS, -10)],
        'very_cold': [(TUNDRA, 0),(WHITE, -10)],
        'polar': [(WHITE, -10)],
        }
        
        
    return dict[temp]

def temperature(table, temp_level):
    for (value, level) in table:
        if temp_level >= level:
            return value
    return -1     
    
def avg(list):
    x = 0
    for i in list:
        x += i
    return x/len(list)

def draw_simplex_map(screen, width, height, octaves, persist, lacuna):

    scale = .0075

    equator = height/2         
    
    for i in range(height):
    
        tempdiff = abs(equator - i) / equator

        for j in range(width):
        
            amp = 1
            freq = 1
            height = 0
            moist = 0
            temp = 1 - tempdiff
            
            for k in range(octaves):
                octavex = j*scale*freq
                octavey = i*scale*freq 
                            
                hvalue = heightmesh.noise2d(x=octavex, y=octavey)
                hvalue2=heightmesh2.noise2d(x=octavex, y=octavey)
                hvalue3 = heightmesh3.noise2d(x=octavex, y=octavey)
                mvalue = moistmesh.noise2d(x=octavex, y=octavey)
                mvalue2 = moistmesh2.noise2d(x=octavex, y=octavey)
                mvalue3 = moistmesh3.noise2d(x=octavex, y=octavey)
                height += avg([hvalue,hvalue2, hvalue3]) * amp
                moist += avg([mvalue,mvalue2, mvalue3]) * amp
                
                amp *= persist
                freq *= lacuna 
                color = height
            heightmod = (abs(height))*.7    
            temp -= heightmod
            moist -= heightmod
            moist += 0.5
            temp += 0.1
            templist =  [('very_hot',5/6), ('hot',4/6), ('warm',3/6), ('cool',2/6), ('cold', 1/6), ('very_cold',0) , ('polar',-10)]
                
            if height <= 0.15:
                if height > 0:
                    screen.set_at((j,i), DEEP)
                else:
                    screen.set_at((j,i), DEEP)

            else:
                 
                temp = temperature(templist, temp)
                moistlist = get_moistlist(temp)
                biome = moisture(moistlist, moist)
                screen.set_at((j,i), biome)
                    

def main():
    
    pygame.init()
    
    pygame.display.set_caption('Opensimplex')
    

    screen_width = 350
    screen_height = 350
    octaves = 5
    persist = 0.5
    lacuna = 2.5
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    draw_simplex_map(screen, screen_width, screen_height, octaves, persist, lacuna)
    
    pygame.display.flip()
    
    running = True
    
    while running:
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

                

if __name__ == '__main__':
    main()


