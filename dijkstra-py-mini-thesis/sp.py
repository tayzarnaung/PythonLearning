from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        # print(from_node, to_node,weight)

graph = Graph()

# edges = [
#     ('X', 'A', 7), ('X', 'B', 2), ('X', 'C', 3),('X', 'E', 4),
#     ('A', 'B', 3), ('A', 'D', 4),
#     ('B', 'D', 4),('B', 'H', 5),
#     ('C', 'L', 2),
#     ('D', 'F', 1),
#     ('F', 'H', 3),
#     ('G', 'H', 2), ('G', 'Y', 2),
#     ('I', 'J', 6), ('I', 'K', 4),('I', 'L', 4),
#     ('J', 'L', 1),
#     ('K', 'Y', 5),
# ]
# edges = [
#     ('A','B',3), ('A','C',1),
#     ('B','C',7), ('B','D',5), ('B','E',1),
#     ('C','D',2),
#     ('D','E',7),
# ]
edges = [
    ('Sule','Sule Myodaw Hall',0.277987317), ('Sule','Pan Soe Tan',0.308944496),('Sule','Thein Gyi Zay',0.607758151963839),
    ('Sule Myodaw Hall','Yoke Shin Yone',0.267080093), ('Sule Myodaw Hall','Bar Lan',0.319386564), ('Sule Myodaw Hall','Kone Zay Tan',0.607241518667168), 
    ('Yoke Shin Yone','Youk Lan',0.445289046),('Yoke Shin Yone','Pan Soe Tan2',0.319575954), ('Yoke Shin Yone','Bo Gyoke Zay',0.597112789),
    ('Youk Lan','Youk Lann',0.401209158), ('Youk Lan','Youk Lan 2',0.217517123), ('Youk Lan','Railway',0.321112960225533),
    ('Youk Lann','Kyauk Taing',0.309336351),
    ('Youk Lan2','Kyauk Taing',0.486675035),
    ('Kyauk Taing','U Htaung Bo',0.757996616),
    ('U Htaung Bo','Taung Phat Mote', 0.670646109), ('U Htaung Bo','Kan Yeik Thar', 0.646248473),('U Htaung Bo','Bahan 3 Lan', 0.424969627585825),
    ('Bahan 3 Lan', 'A Shae Phat Mote',0.661485795102546),('Bahan 3 Lan','Yae Khae Saing',0.178602973432072),
    ('Taung Phat Mote','A Shae Phat Mote', 0.385173739),('Taung Phat Mote','U Wisara Awine', 0.387238813526231),
    ('Pan Soe Tan','Bar Lan', 0.267080098), 
    ('Bar Lan','Sule Myodaw Hall', 0.319386564),('Bar Lan','Pan Soe Tan2', 0.278191101),
    ('Pan Soe Tan2','Yoke Shin Yone', 0.319575954),('Pan Soe Tan2','Railway', 0.467503801633509),
    ('Thein Gyi Zay','Kone Zay Tan',0.266867823947164), ('Thein Gyi Zay','Phone Gyi Lan',0.885392549158717),
    ('Kone Zay Tan','Bo Gyoke Zay',0.278801558781131),('Kone Zay Tan','San Pya',0.870106164012649),
    ('Bo Gyoke Zay','Phyar Lan',0.278191095220989),('Bo Gyoke Zay','Tha Yet Taw',0.888088144092057),
    ('Phyar Lan', 'U Wisara',0.465556678015865), ('Phyar Lan', 'Construction',0.455899199242704),
    ('Construction','Taung Phat Mote',1.0869028392065796),
    ('U Wisara','U Wisara Awine',1.1573252770122),
    ('U Wisara Awine', 'Wizaya Plaza',1.13683676335783),('U Wisara Awine','PyaeAlone',0.724761558742046),
    ('Wizaya Plaza', 'Hantharwady', 1.32791710272074),('Wizaya Plaza','Har Mit Tic 2',1.52924871096126),('Wizaya Plaza','Shwe Gon Daing',1.39254186037551),
    ('PyaeAlone','Myaeni Gone',0.769252234475195),
    ('Phone Gyi Lan', 'San Pya', 0.260622671150373),
    ('San Pya','Tha Yet Taw',0.318081634643598),
    ('Tha Yet Taw','Pegu Club',0.938386802296795),
    ('Pegu Club', 'Myaeni Gone',1.38538058684929),
    ('Myaeni Gone','Hantharwady',1.51465451478916),('Myaeni Gone','Wizaya Plaza',0.646031908907462),
    ('Hantharwady','Hledan',1.47397206232825),
    ('Yae Khae Saing','Shwe Gon Daing 2', 0.689927305116301),('Yae Khae Saing', 'A Shae Phat Mote',0.754057265280479),
    ('Shwe Gon Daing 2', 'Shwe Gon Daing',0.357253876304097),
    ('Shwe Gon Daing', 'Har Mit Tic 2', 0.734580955432107),
    ('Har Mit Tic 2', 'Har Mit Tic', 0.656136411191445),
    ('Har Mit Tic','Kokkaing',0.906431518959193),
    ('Kokkaing','Myanmar Plaza',0.648084587959013),('Kokkaing','Inya Myaing',0.585709904881401),
    ('Inya Myaing','Thanlwin',0.43337868827772),
    ('Thanlwin','UFL',0.49351102915595),
    ('UFL', 'Hledan', 1.05581357244266)
    ]


for edge in edges:
    graph.add_edge(*edge)

# arr = []
# arr = [('A', 'B',3),('A','C',1)]
# for i in range(3):
#     x = input("Type source:")
#     y = input("Type destination:")
#     dist = float( input("Type distance: ") )

#     string =  x , y , dist 
#     print (string)  #will output e.g.('A','B',3)
#     arr.append(string)
# print(arr)

# for edge in arr:
#     graph.add_edge(*edge)



def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

# path = dijsktra(graph, 'X', 'Y')
# source = input("Type source:")
# destination = input("Type destination:")
# path  = dijsktra(graph, source, destination)
# print(path)