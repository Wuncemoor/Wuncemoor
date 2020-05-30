class Graph:
    
    def __init__(self, graph_dict=None):
        
        if graph_dict == None:
            graph_dict = {}
        
        self.__graph_dict = graph_dict
        
        
    def vertices(self):
        return list(self.__graph_dict.keys())
        
    def edges(self):
        return self.__generate_edges()
        
    def add_vertex(self, vertex):
    
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            
    def add_edge(self, edge):
        
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
        
    def __generate_edges(self):
    
        edges = []
        for vertex in self.__graph_dict:
            for nearby in self.__graph_dict[vertex]:
                if {nearby, vertex} not in edges:
                    edges.append({vertex, nearby})
        return edges
        
if __name__ == "__main__":
    
    g = {
    'a' : ['d'],
    'b' : ['c'],
    'c' : ['b','c','d','e'],
    'd' : ['a','c'],
    'e' : ['c'],
    'f' : []
    }
    
    graph = Graph(g)
    
    print('vertices of graph:')
    print(graph.vertices())
    
    print('edges of graph:')
    print(graph.edges())
    
    print('add vertex:')
    graph.add_vertex('z')
    
    print('vertices of graph:')
    print(graph.vertices())
    
    print('add an edge:')
    graph.add_edge({'a','z'})
    
    print('vertices of graph:')
    print(graph.vertices())
    
    print('edges of graph:')
    print(graph.edges())
    
    print ('adding edge{"x","y"} wiht new vertgices:')
    graph.add_edge({"x","y"})
    print('vertices of graph:')
    print(graph.vertices())
    print('edges of graph:')
    print(graph.edges())
    