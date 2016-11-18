# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:51:24 2016

@author: Mike
"""
from collections import defaultdict
import sys
import resource

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


class Tracker(object):
    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()
        
def make_graph(filename):
    '''creates a dictionary where the the tails are the keys and the value
    is a list of heads'''
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for line in filename:
        x = line.strip().split()
        x1,x2 = int(x[0]), int(x[1])
        graph[x1].append(x2)
        reverse_graph[x2].append(x1)
    return graph, reverse_graph
        
def SCC(graph, reverse_graph):
    tracker1 = Tracker()
    tracker2 = Tracker()
    nodes = set()
    for tail, head in graph.items():
        nodes |= set(head)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reverse_graph, nodes, tracker1)
    order_finish = sorted(tracker1.finish_time, key=tracker1.finish_time.get,
                          reverse=True)
    dfs_loop(graph, order_finish, tracker2)                               
    return list(tracker2.leader.values())
    
        
def dfs_loop(graph, nodes, tracker):
    '''outer loop checks out all SCCs'''
    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph, node, tracker)
        
def dfs(graph, node, tracker):
    """inner loop checks out all SCCs"""
    tracker.explored.add(node)
    tracker.leader.setdefault(tracker.current_source, [])
    if tracker.current_source not in tracker.leader[tracker.current_source]:
        tracker.leader[tracker.current_source].append(tracker.current_source)
    for head in graph[node]:
        if head not in tracker.explored:
            tracker.leader[tracker.current_source].append(head)
            dfs(graph, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time
        
def main():
    file = open('SCC.txt')
    graph, reverse_graph = make_graph(file)
    groups = SCC(graph, reverse_graph)
    top_5 = sorted(groups, key=len, reverse=True)
    results = []
    for i in range(5):
        try:
            results.append(len(top_5[i]))
        except:
            results.append(0)
    return results
    
if __name__ == '__main__':
    print(main())