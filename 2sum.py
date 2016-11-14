# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:23:28 2016

@author: Jake
"""
import bisect

def make_graph(file):
    graph = []
    for line in file:
        graph.append(int(line))
    return graph
    
def two_sum(array):
    """Returns the numbers from [-WIDTH, WIDTH] that can be obtained by
    summing up any two elements in 'array'."""

    WIDTH = 10000
    out = set()
    for i in array:
        lower = bisect.bisect_left(array, -WIDTH - i)
        upper = bisect.bisect_right(array, WIDTH - i)
        out |= set([i + j for j in array[lower:upper]])
    return out
        
def main():
#    tracker = 0
    file = open('2sum.txt')
#    graph = set([int(line) for line in file])
#    for t in range(-10000, 10001):
#        for num in graph:
#            if t - num in graph:
#                tracker += 1
#    return tracker           
    graph = make_graph(file)
    graph.sort()
    return len(two_sum(graph))
    
if __name__ == '__main__':
    print(main())