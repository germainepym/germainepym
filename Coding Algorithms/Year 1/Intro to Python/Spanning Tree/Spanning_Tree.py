#Spanning Tree
def extension(vertices, graph):
    n = len(graph)
    for i in vertices:
        for j in range(n):
            if j not in vertices and graph[i][j]:
                return i, j

def spanning_tree(graph):
    '''input: graph given as adjacency matrix
       output: spanning tree of graph (as adj. mat)'''
    n = len(graph)
    tree =  [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    conn = [0]
    while len(conn) < n:
        i, j = extension(conn, graph)
        tree[i][j] = 1
        tree[j][i] = 1
        conn = conn + [j]
    return tree

G = [[0,1,1,1],
     [1,0,1,1],
     [1,1,0,0],
     [1,1,0,0]]

print(spanning_tree(G))

#Spanning Tree of an edge-weighted graph
from math import inf

def minimum_extension(vertices, graph):
    min_weight = inf
    for i in vertices:
        for j in range(len(graph)):
            if j not in vertices and 0 < graph[i][j] < min_weight:
                v,w = i,j
                min_weight = graph[i][j]
    return v,w

def minimum_spanning_tree(graph):
    '''input: graph given as adjacency matrix
       output: spanning tree of graph (as adj. mat)'''
    n = len(graph)
    tree =  [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    conn = [0]
    while len(conn) < n:
        i, j = minimum_extension(conn, graph)
        tree[i][j],tree[j][i] = graph[i][j], graph[j][i]
        conn = conn + [j]
    return tree

G = [[0,5,4,7],
     [5,0,8,6],
     [4,8,0,0],
     [7,6,0,0]]

print(minimum_spanning_tree(G))

