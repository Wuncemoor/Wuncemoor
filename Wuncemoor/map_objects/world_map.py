from tile import Tile
from PIL import Image
import random
import math

class WorldMap:
    
    #Setting up world map, num_cells is # of voronoi nodes
    def __init__(self, width, height, num_cells):
        self.width = width
        self.height = height
        self.num_cells = num_cells
        self.tiles = self.initialize_tiles()
        self.voronoi = self.voronoi_generate()
        self.continents = self.continents_generate()
        self.border_nodes = None
        self.finalarray = None
        self.new_centroids = None
    
    #Applying Tile.py class to WorldMap array
    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        
        return tiles
        
    #Make voronoi map with nodes = num_cells, lloyd relaxation = loops    
    def voronoi_generate(self):
        
        #Initialize map image
        image = Image.new('RGB', (self.width, self.height))
        putpixel = image.putpixel
        imgx, imgy = image.size
        
        #Bunch of constants
        looped = 0
        loops = 6
        node = 0
        xy = []
        rgb = []
        arrayvalues = []
        finalarray = []
        new_centroids = []
        node_x = []
        node_y = []
        border_nodes = []
        non_border_nodes = []

        
        #Voronoi generation and Lloyd relaxation loop
        while looped < loops:
           
            while len(xy) < self.num_cells:
                
                #Pick random points for first loop
                if looped == 0:
                    x, y = random.randrange(imgx), random.randrange(imgy)
                    if [x,y] not in xy:
                    
                        xy.append([x,y])
                        rgb.append([random.randrange(256),random.randrange(256),random.randrange(256)])
                
                #Use new centroids for other loops
                else:
                    xy = new_centroids.copy()
      
            new_centroids.clear()
                    
            #For all tiles in the 2D map        
            for y in range(imgy):
                for x in range(imgx):
                    #There exists a closest node
                    dmin = math.hypot(imgx - 1, imgy - 1)
                    j = -1
                    #Compare distance to nodes
                    for i in range(self.num_cells):
                        d = math.hypot(xy[i][0]-x, xy[i][1]-y)
                        #Assign to closest node
                        if d < dmin:
                            dmin = d
                            j = i
                    arrayvalues.append([j,x,y])
                    putpixel((x, y), (rgb[j][0], rgb[j][1], rgb[j][2]))
            #Save final array
            if looped == (loops - 1):
                finalarray = arrayvalues.copy()

            
            #For each node
            while (node < self.num_cells):
            
                #Compare to each tile in array
                for i in range(len(arrayvalues)):
                    
                    if arrayvalues[i][0] == node:
                        node_x.append(arrayvalues[i][1])
                        node_y.append(arrayvalues[i][2])
                
                #Find new centroids
                average_x = math.floor((sum(node_x))/(len(node_x)))+ random.randrange(1)
                average_y = math.floor((sum(node_y))/(len(node_y))) + random.randrange(1)
                new_centroids.append([average_x,average_y])
                node_x.clear()
                node_y.clear()
                node += 1
            node = 0
            xy.clear()
            arrayvalues.clear()
            looped += 1
            
        #Set map border to blue (water), non-border to green (land)   
        for i in finalarray:
            #If a pixel is on the edge of the map
            if (i[1] == 0) or (i[2] == 0) or (i[1] == (self.width-1)) or (i[2] == (self.height-1)):
                #And it isn't already in border_nodes
                if i[0] not in border_nodes:
                    border_nodes.append(i[0])
            
            else:
                if (i[0] not in border_nodes) and (i[0] not in non_border_nodes): 
                    non_border_nodes.append(i[0])
        
        for i in finalarray:
            
            if i[0] in border_nodes:
                #Map border always blue (water)
                putpixel((i[1], i[2]), (0, 0, 255))
            
            else:
                
                putpixel((i[1], i[2]), (0, 255, 0))
        self.new_centroids = new_centroids
        self.finalarray = finalarray
        self.border_nodes = border_nodes    
        image.save('Voronoitest.png', 'PNG')
        image.show()
        
        
        
    def continents_generate(self):

        image = Image.new('RGB', (self.width, self.height))
        putpixel = image.putpixel
        imgx, imgy = image.size

        continent_centroids = []
        continents_centroids = []
        possibilities = []
        water_nodes = self.border_nodes
        continent_nodes = []
        continents_nodes = []
        nodes_in_continent = []
        land_mass = math.floor(self.num_cells*0.3)
        starting_centroid = None
        loops = 4
        looped = 0
        
        cells_per_continent = [0]*loops
        
        #How big is each continent?
        for i in range(land_mass):
        
            x = random.randint(0, loops-1)
            cells_per_continent[x] += 1
        print(cells_per_continent)
            
        
        

        while looped < loops:
        
            #Until you've got enough nodes
            while len(continent_centroids) < cells_per_continent[looped]:
                #Randomize the first one
                if len(continent_centroids) < 2:
                    for i in self.finalarray:
                        #Leave the used nodes alone
                        if i[0] not in (water_nodes or continents_nodes):
                            
                            possibilities.append(i)
                    #Randomized starting continent location    
                    town = random.choice(possibilities)
                    

                    
                    for i in self.finalarray:
                        
                        #Find the centroid of the starting town
                        if [i[1], i[2]] in self.new_centroids and i[0] == town[0]:
                            
                            starting_centroid = [i[1], i[2]]
                            continent_centroids.append([i[1],i[2]])
                            continents_centroids.append([i[1],i[2]])

                    

                
                #After you've gotten the island generation started
                else:
                    starting_centroid = random.choice(continent_centroids)
                    
                shortest_distance = 1000000000000
                closest_centroid = [0,0]            
                #Find the closest centroid to starting centroid
                for i in self.new_centroids:
                
                    distance = math.hypot(i[0]-starting_centroid[0], i[1]-starting_centroid[1])
                    if distance < shortest_distance and i not in continents_centroids:
                        shortest_distance = distance
                        closest_centroid = i
                shortest_distance = 1000000000000
                continent_centroids.append(closest_centroid)
                continents_centroids.append(closest_centroid)

            for i in self.finalarray:
                
                for centroid in continent_centroids:
                    
                    if i[0] not in continents_nodes and i[1] == centroid[0] and i[2] == centroid[1] :
                    
                        continent_nodes.append(i[0])
                        continents_nodes.append(i[0])
                        
            #Turn nodes around continent to water
            for i in self.finalarray:
                
                nearby_right = [ i[1]+1, i[2]]
                nearby_left = [ i[1]-1, i[2]]
                nearby_up = [ i[1], i[2] - 1]
                nearby_down = [ i[1], i[2] + 1]
                
                if i[0] in continent_nodes:
                    
                    for j in self.finalarray:
                        
                        if j[1] == nearby_right[0] and j[2] == nearby_right[1]:
                        
                            if i[0] != j[0] and j[0] not in continent_nodes:
                                water_nodes.append(j[0])
                                
                        if j[1] == nearby_left[0] and j[2] == nearby_left[1]:
                            
                            if i[0] != j[0] and j[0] not in continent_nodes:
                                water_nodes.append(j[0])
                                
                        if j[1] == nearby_down[0] and j[2] == nearby_down[1]:
                        
                            if i[0] != j[0] and j[0] not in continent_nodes:
                                water_nodes.append(j[0])
                                
                        if j[1] == nearby_up[0] and j[2] == nearby_up[1]:
                            
                            if i[0] != j[0] and j[0] not in continent_nodes:
                                water_nodes.append(j[0])
            these_nodes = continent_nodes.copy()  
            nodes_in_continent.append(these_nodes)
            continent_centroids.clear()
            continent_nodes.clear()
            looped += 1
                                       

        for i in self.finalarray:
            
            if i[0] in water_nodes:
                
                putpixel((i[1], i[2]), (0, 0, 255))
                
            elif i[0] in continents_nodes:
            
                putpixel((i[1], i[2]), (0,255,0))

            else:
                
                putpixel((i[1], i[2]), (0, 0, 255))
                
        print(nodes_in_continent)
        #print(len(nodes_in_continent[0]),len(nodes_in_continent[1]), len(nodes_in_continent[2]), len(nodes_in_continent[3]), len(nodes_in_continent[4]))
            
        image.save('Voronoitest.png', 'PNG')
        image.show()

        return town
        
worldmap = WorldMap(100,100,300)