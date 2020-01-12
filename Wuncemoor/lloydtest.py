from PIL import Image
import random
import math

def voronoi_generate(width, height, num_cells):
    
    #Initialize map image
    image = Image.new('RGB', (width, height))
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
       
        while len(xy) < num_cells:
            
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
                for i in range(num_cells):
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
        while (node < num_cells):
        
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
        
    #Sort nodes into border and non-border  
    for i in finalarray:
        #If a pixel is on the edge of the map
        if (i[1] == 0) or (i[2] == 0) or (i[1] == (width-1)) or (i[2] == (height-1)):
            #And it isn't already in border_nodes
            if i[0] not in border_nodes:
                border_nodes.append(i[0])
        
        else:
            if (i[0] not in border_nodes) and (i[0] not in non_border_nodes): 
                non_border_nodes.append(i[0])
    

        
    return finalarray, border_nodes, non_border_nodes, width, height, num_cells, new_centroids
    
    
def continents_generate(finalarray, border_nodes, non_border_nodes, width, height, num_cells, new_centroids):

    image = Image.new('RGB', (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size

    continent_centroids = []
    continents_centroids = []
    possibilities = []
    water_nodes = border_nodes
    continent_nodes = []
    continents_nodes = []
    nodes_in_continent = []
    land_mass = math.floor(num_cells*0.3)
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
                for i in finalarray:
                    #Leave the used nodes alone
                    if i[0] not in (water_nodes or continents_nodes):
                        
                        possibilities.append(i)
                #Randomized starting continent location    
                town = random.choice(possibilities)
                

                
                for i in finalarray:
                    
                    #Find the centroid of the starting town
                    if [i[1], i[2]] in new_centroids and i[0] == town[0]:
                        
                        starting_centroid = [i[1], i[2]]
                        continent_centroids.append([i[1],i[2]])
                        continents_centroids.append([i[1],i[2]])

                

            
            #After you've gotten the island generation started
            else:
                starting_centroid = random.choice(continent_centroids)
                
            shortest_distance = 1000000000000
            closest_centroid = [0,0]            
            #Find the closest centroid to starting centroid
            for i in new_centroids:
            
                distance = math.hypot(i[0]-starting_centroid[0], i[1]-starting_centroid[1])
                if distance < shortest_distance and i not in continents_centroids:
                    shortest_distance = distance
                    closest_centroid = i
            shortest_distance = 1000000000000
            continent_centroids.append(closest_centroid)
            continents_centroids.append(closest_centroid)

        for i in finalarray:
            
            for centroid in continent_centroids:
                
                if i[0] not in continents_nodes and i[1] == centroid[0] and i[2] == centroid[1] :
                
                    continent_nodes.append(i[0])
                    continents_nodes.append(i[0])
                    
        #Turn nodes around continent to water
        for i in finalarray:
            
            nearby_right = [ i[1]+1, i[2]]
            nearby_left = [ i[1]-1, i[2]]
            nearby_up = [ i[1], i[2] - 1]
            nearby_down = [ i[1], i[2] + 1]
            
            if i[0] in continent_nodes:
                
                for j in finalarray:
                    
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
                                   

    for i in finalarray:
        
        if i[0] in water_nodes:
            
            putpixel((i[1], i[2]), (0, 0, 255))
            
        elif i[0] in continents_nodes:
        
            putpixel((i[1], i[2]), (0,255,0))

        else:
            
            putpixel((i[1], i[2]), (0, 0, 255))
                    
    image.save('Continentstest.png', 'PNG')
    image.show()

    return width, height, finalarray, water_nodes, continents_nodes
    
def bigger_map(width, height, finalarray, water_nodes, continents_nodes):

    ratio = 5
    image = Image.new('RGB', (ratio*width, ratio*height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    
    big_map = [None]*len(finalarray)*(ratio**2)
    small_loop = 0
    big_loop = 0
    bigmap_x = 0
    bigmap_y = 0
    x_amp = 0 
    y_amp = 0
    
    #Until the bigger map has been created
    while bigmap_y < ratio*height:
        
        #The current tile being amplified is
        current_tile = finalarray[small_loop]
        
        #Amplify the map by the ratio
        if y_amp < ratio:  
        
            #Until you reach the end of the row
            if bigmap_x < ratio*width:
                
                #Amplify the map by the ratio
                if x_amp < ratio:
                
                    #Fill in the big map, move along the pointers
                    if current_tile[0] in continents_nodes:
                        
                        big_map[big_loop] = [1, bigmap_x, bigmap_y]
                        x_amp += 1
                        big_loop += 1
                        putpixel((bigmap_x, bigmap_y), (0,255,0))
                        bigmap_x += 1
                        
                    else:
                        
                        big_map[big_loop] = [0, bigmap_x, bigmap_y]
                        x_amp += 1
                        big_loop += 1
                        putpixel((bigmap_x, bigmap_y), (0,0,255))
                        bigmap_x += 1

                    
                else:
                    
                    small_loop += 1
                    x_amp = 0
            
            else: 
            
                small_loop -= width
                bigmap_x -= ratio*width
                bigmap_y += 1
                y_amp += 1
        
        else: 
            
            small_loop += width
            y_amp = 0
            
    image.save('Biggermaptest.png', 'PNG')
    image.show()

            


        
    
x = voronoi_generate(100,100,300) 
y = continents_generate(x[0],x[1], x[2], x[3], x[4], x[5], x[6])
z = bigger_map(y[0],y[1],y[2],y[3],y[4])

