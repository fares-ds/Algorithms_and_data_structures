class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return f"{self.id} connected to {[(x.id, self.get_weight(x)) for x in self.connected_to]}"


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vertex_list:
            self.add_vertex(from_vertex)

        if to_vertex not in self.vertex_list:
            self.add_vertex(to_vertex)

        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], cost)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def __contains__(self, item):
        return item in self.vertex_list


g = Graph()
list_of_classes = ['Maths', 'Physics', 'Computer Science', 'Art', 'Geographic', 'History', 'Literature']
for student_class in list_of_classes:
    g.add_vertex(student_class)

# print(g.vertex_list)
g.add_edge(list_of_classes[0], list_of_classes[1], 2)
g.add_edge(list_of_classes[5], list_of_classes[3], 7)
g.add_edge(list_of_classes[3], list_of_classes[4], 2)
g.add_edge(list_of_classes[2], list_of_classes[5], 3)
g.add_edge(list_of_classes[1], list_of_classes[3], 6)
g.add_edge(list_of_classes[4], list_of_classes[0], 2)

for vertex in g:
    # print(f"{vertex} -> {vertex.get_connections()}")
    print(vertex)
