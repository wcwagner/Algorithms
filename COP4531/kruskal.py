#!/usr/bin/python
from __future__ import print_function
import sys
from collections import defaultdict

class Node(object):
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return str(self.val)

# this will take in a node, and create new instance attrs parent and rank
def Make_Set(x):
    x.parent = x
    x.rank = 0

def Union(x, y):
    x_root = Find_Set(x)
    y_root = Find_Set(y)
    if x_root is y_root:
        return
    # set the smaller tree's representative to the bigger tree's representative
    if x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif y_root.rank < x_root.rank:
        y_root.parent = x_root
    else:
        y_root.parent = x_root
        x_root.rank += 1
# when traversing upwards to the root, this will compress the path
# e.g. making every node's represenative on the path upward to the base root
# this improves look-up times on furuter find calls
def Find_Set(x):
    if x.parent is not x:
        x.parent = Find_Set(x.parent)
    return x.parent

def is_connected(graph, root):
    visited, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # adds all the non-visited vetcies incident with the curr vetex
            stack.extend(graph[vertex] - visited)
    G_V = set(graph.keys())
    visited.add(root)
    if len(G_V) == len(visited):
        return True
    else:
        return False

def MST_Kruskal(G_V, G_E):
    A = []
    tot_weight = 0
    # keyd by the vert val
    nodes = {v: Node(v) for v in G_V}
    # this will set the parent and rank attrs for each node
    for val in nodes:
        Make_Set(nodes[val])
    # sort by weights
    G_E.sort(key=lambda t: t[2])
    for e in G_E:
        u, v, w = e
        if Find_Set(nodes[u]) is not Find_Set(nodes[v]):
            A.append([u, v])
            Union(nodes[u], nodes[v])
            tot_weight += w
    # output in the desired format
    print(tot_weight)
    for edge in A:
        if edge[0] > edge[1]:
            edge[0], edge[1] = edge[1], edge[0]
    A.sort()
    for edge in A:
        print("{u} {v}".format(u=edge[0], v=edge[1]))

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        num_vertcies = file.readline()
        # split each line, then convert the strs to ints. Last line is \n so ignore
        # each element of G_E is (u:int, v:int, w:int)
        G_E = [tuple(map(lambda l: int(l), line.split())) for line in file.readlines()]
        adj_list = defaultdict(set)
        for e in G_E:
            root = e[0]
            adj_list[e[0]].add(e[1])
            adj_list[e[1]].add(e[0])
        # unique list of vertices
        G_V = set([t[0] for t in G_E] + [t[1] for t in G_E])
        if is_connected(adj_list, root):
            MST_Kruskal(G_V, G_E)
        else:
            print("Impossible")
