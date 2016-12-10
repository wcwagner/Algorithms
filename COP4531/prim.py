#!/usr/bin/python
from __future__ import print_function
import sys
from heapq import *
from collections import defaultdict

def MST_Prim(G, r):
    # G is adj list {u:int : {v:w, v`:w`}....}
    # each node in the min-heap is of the form [key, label, parent]
    heap = [[float("inf"), v, None] for v in G.keys() if v != r]
    # r.key = 0
    heap.append([0, r, None])
    # we have to modify the nodes in the heap later on, thus we keep
    # a dictionary, that maps each node label to it's corresponding loc
    # in the heap
    loc = {l[1]: l for l in heap}
    # Q = G.V
    heapify(heap)
    A = []
    tot_weight = 0
    while len(heap):
        u = heappop(heap)
        # ignore the first iteration, where None--Root is added into A
        # on all other iterations, append (u.parent--u) into A bc safe edge
        if u[2]:
            A.append([u[2], u[1]])
        tot_weight += u[0]
        # the node label, used to index into loc
        u = u[1]
        # remove node from Q, as it is now in the MST (A)
        del[loc[u]]

        for v in G[u]:
            # if v in Q and w(u, v) < v.key
            if v in loc and G[u][v] < loc[v][0]:
                # v.par = u
                loc[v][2] = u
                # v.key = w(u,v)
                loc[v][0] = G[u][v]
        # O(N), python has no decrease_key function, so this will suffice
        heapify(heap)
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
        G_E = [tuple(map(lambda l: int(l), line.split())) for line in file.readlines()]
        adj_list = defaultdict(dict)
        for edge in G_E:
            root = edge[0]
            # inserting u:v
            adj_list[ edge[0] ][ edge[1] ] = edge[2]
            # inserting v:u
            adj_list[ edge[1] ][ edge[0] ] = edge[2]

        MST_Prim(adj_list, 1)
