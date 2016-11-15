# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:52:08 2016

@author: Jake
"""
import random
import math
import copy

class Adjacency(object):
    
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge
        
    def contract(self, other):
        self.vertex += other.vertex
        self.edge = [i for i in self.edge + other.edge if i not in self.vertex]
        
    def __repr__(self):
        return 'Adjacency (vertex = %r, edge = %r)' % (self.vertex, self.edge)
        
def cut(graph):
    if len(graph) == 2:
        return graph
    else:
        rand_vertex = random.choice(graph)
        merge_vertex = random.choice(rand_vertex.edge)
        merge_pick = [i for i in graph if merge_vertex in i.vertex]

        rand_vertex.contract(merge_pick[0])
        graph.remove(merge_pick[0])
        return cut(graph)
    
def min_cut(graph):
    trial_nu = int(math.pow(len(graph), 1) * math.log(len(graph)))
    min_cross = float('inf')
    for i in range(trial_nu):
        trial = cut(copy.deepcopy(graph))
        cut_cross = len(trial[0].edge)
        if cut_cross < min_cross:
            min_cross = cut_cross
    return min_cross
        
def main():
    file_in = open('kargerMinCut.txt')
    data = [[[int(line.split()[0])], [int(i) for i in line.split()[1:]]]
            for line in file_in]
    graph = [Adjacency(i[0], i[1]) for i in data]
    return min_cut(graph)
    
if __name__ == '__main__':
    print(main())