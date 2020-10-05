from collections import deque as Queue
from heapq import *


class Graph:
    """
        The class for the Graph
    """

    def __init__(self, gfile):
        """
        This function reads the file provided and constructs a graph
        Arguments:          gfile
        Time complexity:    Best case: O(V^2) for v is the number of vertices in the graph
                            Worst case: O(V^2) for v is the number of vertices in the graph

        Space complexity: O(V^2) or v is the number of vertices in the graph
        Aux space complexity: O(V^2) or v is the number of vertices in the graph
        Return: does not return anything
        """
        with open(gfile, 'r') as file:
            count = 0
            for line in file:
                line = line.strip()
                count += 1
                if count == 1:
                    self.vertices = [None] * int(line)  # list of vertices
                    for i in range(int(line)):  # create the vertices
                        self.vertices[i] = Vertex(i)
                else:
                    u, v, w = line.split(' ')
                    item = [u, v, w]
                    self.add_edges(item)

            file.close()

    def __str__(self): #print graph
        """
               This function visualizes the graph
               Arguments:          None
               Time complexity:    Best case: O(v) for v is the number of vertices in the graph
                                   Worst case: O(v) for v is the number of vertices in the graph

               Space complexity: O(v) for v is the number of vertices in the graph
               Aux space complexity: O(1)
               Return: returns a string that shows the existing vertex and edges in the graph
        """
        return_string = ''
        for vertex in self.vertices:
            return_string = return_string + "vertex " + str(vertex) + "\n"

        return return_string

    def reset(self, function = None):
        """
              This function resets the graph
              Arguments:          function = which function is it resetting for
              Time complexity:    Best case: O(v) for v is the number of vertices in the graph
                                  Worst case: O(v) for v is the number of vertices in the graph

              Space complexity: O(1)
              Aux space complexity: O(1)
              Return: does not return anything
       """

        if function == 'shortest_errand':
            for vertex in self.vertices:
                vertex.discovered = False
                vertex.visited = False
        else:
            for vertex in self.vertices:
                vertex.discovered = False
                vertex.visited = False
                vertex.distance = 0

    def add_edges(self,argv_edges, argv_direct = False):
        """
                 This function adds edges to the vertex
                 Arguments:          argv_edges = a list containing the edge the vertex contain and their weight
                                     argv_direct = if False means its connected graph

                 Time complexity:    Best case: O(1)
                                     Worst case: O(1)

                 Space complexity: O(1)
                 Aux space complexity: O(1)
                 Return: does not return anything
        """
        u = argv_edges[0]
        v = argv_edges[1]
        w = argv_edges[2]
        #add u to v
        current_edge = Edge(u,v,w)
        current_vertex = self.vertices[int(u)]
        current_vertex.add_edge(current_edge)
        # add v to u
        if not argv_direct:
            current_edge = Edge(v, u, w)
            current_vertex = self.vertices[int(v)]
            current_vertex.add_edge(current_edge)

    def shallowest_spanning_tree(self):
        """
                 This function finds the shortest spanning tree (vertex with the least height)
                 Arguments:          None

                 Time complexity:    Best case: O(V^3) where V is the number of vertices in the graph.
                                     Worst case: O(V^3) where V is the number of vertices in the graph.

                 Space complexity: O(1)
                 Aux space complexity: O(1)
                 Return: the vertex with the shortest spanning tree
        """

        vertex, depth = 0, 0
        for i in range(len(self.vertices)):
            self.reset()
            source = self.vertices[i]
            test_vertex, test_depth = i, 0
            discovered = Queue()  # queue()
            discovered.append(source)
            while len(discovered) > 0:  # if i have vertex that i haven't discovered before
                u = discovered.popleft()  # popleft() is serve ( from the front)
                u.visited = True
                count = 0
                for edge in u.edges:
                    # if reached max height of the tree is reached
                    if test_depth == 0:
                        test_depth = self.vertices[int(edge.u)].distance
                    elif test_depth < self.vertices[int(edge.u)].distance:
                        test_depth = self.vertices[int(edge.u)].distance

                    v = int(edge.v)  # neighbour, the vertex beside
                    v = self.vertices[v]
                    if v.discovered == False and v.visited == False:  # if not discovered
                        v.distance = self.vertices[int(edge.u)].distance + 1
                        discovered.append(v)  # put it in the queue
                        v.discovered = True
                    else:
                        count += 1

             # compare the vertexes, to find the shallowest depth
            if i == 0:
                vertex = test_vertex
                depth = test_depth
            else:
                if depth > test_depth:
                    depth = test_depth
                    vertex = test_vertex

        return vertex, depth

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        """
                 This function is incomplete
                 Arguments:          home = source vertex
                                     destination = end vertex
                                     ice_locs = ice vertex
                                     ice_cream_locs = ice cream vertex

                 Time complexity:    Best case: O(ElogV) where V is the number of vertices in the graph and E is the
                                                         number of edges
                                     Worst case: O(ElogV) where V is the number of vertices in the graph and E is the
                                                         number of edges

                 Space complexity: O(ic) for i is ice_locs and c is ice_cream_locs
                 Aux space complexity: O(1)
                 Return: None
        """

        # -------------------1st Dijkstra----------------
        # The 1st dijkstra traverses through the whole graph from home to all vertex
        function = 'shortest_errand'
        self.reset(function)
        source = self.vertices[home]
        discovered = MinHeap()
        source.distance = 0
        discovered.push(0, source)
        count = 0
        while len(discovered.array) > 0:  # if i have vertex that i havent discovered before
            u = discovered.pop()
            if count != 0:
                u = self.vertices[u]
            if u.discovered is True:
                continue

            count += 1
            u.discovered = True
            for edge in u.edges:
                v = int(edge.v)
                v = self.vertices[v]
                if v.discovered is False:  # if not discovered
                    if v.distance > u.distance + int(edge.w):
                        # update distance
                        v.distance = u.distance + int(edge.w)
                        v.previous = u
                        # update heap
                        discovered.push(v.distance, v.id)


        # -------------------2nd Dijkstra----------------
        # second dijkstra traverses through the graph from ice to all vertex

        discovered2 = MinHeap()

        for i in ice_locs:
            ice = self.vertices[i]
            discovered2.push(ice.distance, ice.id)

        function = 'shortest_errand'
        self.reset(function)

        while len(discovered2.array) > 0:  # if i have vertex that i havent discovered before
            u = discovered2.pop()
            u = self.vertices[u]
            if u.discovered is True:
                continue

            u.discovered = True
            for edge in u.edges:
                v = int(edge.v)
                v = self.vertices[v]
                if v.discovered is False:  # if not discovered
                    if v.distance > int(edge.w):
                        # update distance
                        v.distance = u.distance + int(edge.w)
                        v.previous = u



        # -------------------3rd Dijkstra----------------
        # the third dijkstra traverses from ice cream to all vertex

        discovered3 = MinHeap()

        for i in ice_cream_locs:
            cream = self.vertices[i]
            discovered3.push(cream.distance, cream.id)

        function = 'shortest_errand'
        self.reset(function)

        while len(discovered3.array) > 0:  # if i have vertex that i havent discovered before
            u = discovered3.pop()
            u = self.vertices[u]
            if u.discovered is True:
                continue

            u.discovered = True
            for edge in u.edges:
                v = int(edge.v)
                v = self.vertices[v]
                if v.discovered is False:  # if not discovered
                    if v.distance > int(edge.w):
                        # update distance
                        v.distance = u.distance + int(edge.w)
                        v.previous = u




class Vertex:
    """
        The class for the Vertex
    """
    def __init__(self, id):
        """
        This function initializes the vertex
        Arguments:          ID = the current vertex

        Time complexity:    Best case: O(1)
                            Worst case: O(1)

        Space complexity: O(n) for n is list of edges
        Aux space complexity: O(n) for n is list of edges
        Return: does not return anything

        """
        self.id = id
        #list
        self.edges = []
        # for traversal
        self.discovered = False
        self.visited = False
        #distance
        self.distance = 0
        #backtracking/ where i was from
        self.previous = None

    def __str__(self):
        """
               This function visualizes the vertex
               Arguments:          None
               Time complexity:    Best case: O(e) for e is the number of edges in the graph
                                   Worst case: O(e) for e is the number of edges in the graph

               Space complexity: O(e) for e is the number of edges in the graph
               Aux space complexity: O(1)
               Return: returns a string that shows the existing vertex in the graph
        """

        return_string = str(self.id)
        for edge in self.edges:
            return_string = return_string +'\n with edges' + str(edge)
        return return_string


    def add_edge(self, edge):
        """
                 This function adds edges to the vertex
                 Arguments:          edge = contains the edge of the vertex contain and their weight

                 Time complexity:    Best case: O(1)
                                     Worst case: O(1)

                 Space complexity: O(1)
                 Aux space complexity: O(1)
                 Return: does not return anything
        """

        self.edges.append(edge)

class Edge:
    """
        The class for the Edge
    """

    def __init__(self, u, v, w):
        """
        This function initializes the edge
        Arguments:          u = the current vertex
                            v = the neighbouring vertex
                            w = weight of the edge

        Time complexity:    Best case: O(1)
                            Worst case: O(1)

        Space complexity: O(1)
        Aux space complexity: O(1)
        Return: does not return anything

        """

        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        """
               This function visualizes the edge
               Arguments:          None
               Time complexity:    Best case: O(1)
                                   Worst case: O(1)

               Space complexity: O(1)
               Aux space complexity: O(1)
               Return: returns a string that shows the edges in the graph
        """
        return_string = str(self.u) + "," + str(self.v) + ',' + str(self.w)
        return return_string

class MinHeap:
    """
        The class for the MinHeap
    """
    def __init__(self):
        """
               This function initializes the MinHeap
               Arguments:          None
               Time complexity:    Best case: O(1)
                                   Worst case: O(1)

               Space complexity: O(n) for n is the size of the heap
               Aux space complexity: O(n) for n is the size of the heap
               Return: does not return anything
        """
        self.array = []


    def push(self, distance, vertex):
        """
               This function pushes in element into the array
               Arguments:          vertex = the vertex of the graph
                                   distance = the distance between vertex
               Time complexity:    Best case: O(1)
                                   Worst case: O(1)

               Space complexity: O(1)
               Aux space complexity: O(1)
               Return: does not return anything
        """

        heappush(self.array, (distance, vertex))


    def pop(self):
        """
               This function pops out the element from the array
               Arguments:          None

               Time complexity:    Best case: O(1)
                                   Worst case: O(1)

               Space complexity: O(1)
               Aux space complexity: O(1)
               Return: does not return anything
        """
        vertex = heappop(self.array)[1]
        return vertex

    def is_empty(self):
        """
               If the array is empty return
               Arguments:          None

               Time complexity:    Best case: O(1)
                                   Worst case: O(1)

               Space complexity: O(1)
               Aux space complexity: O(1)
               Return: return
        """
        return len(self.array) == 0


if __name__ == "__main__":
    my_graph = Graph("given_graph2")
    print(my_graph.shallowest_spanning_tree())
    print(my_graph.shortest_errand(0, 8, [1, 5, 8], [4, 6]))
    print(my_graph)