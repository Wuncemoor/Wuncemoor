from PIL import Image
import random
import math

def voronoi_generate(width, height, num_cells):
    
    image = Image.new('RGB', (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    
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
        image.save('Voronoitest.png', 'PNG')
        image.show()
        #Save final array
        if looped == (loops - 1):
            finalarray = arrayvalues.copy()

        
        #For each node
        while (node < num_cells) and ( looped < (loops - 1)):
        
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

    return width, height, finalarray, num_cells

def world_map_border(width, height, finalarray):

    image = Image.new('RGB', (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size

    border_nodes = []
    non_border_nodes = []
    continent_peaks = []
    
    for i in finalarray:
    
        if (i[1] == 0) or (i[2] == 0) or (i[1] == (width-1)) or (i[2] == (height-1)):
            if i[0] not in border_nodes:
                border_nodes.append(i[0])
        
        else:
            if (i[0] not in border_nodes) and (i[0] not in non_border_nodes): 
                non_border_nodes.append(i[0])
    
    for i in finalarray:
        
        if i[0] in border_nodes:
        
            putpixel((i[1], i[2]), (0, 0, 255))
        
        else:
            
            putpixel((i[1], i[2]), (0, 255, 0))
        
    image.save('Voronoitest.png', 'PNG')
    image.show()

        
    
x = voronoi_generate(100,100,300)
world_map_border(x[0],x[1],x[2]) 
