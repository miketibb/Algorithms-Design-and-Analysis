# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:27:11 2016

@author: Jake
"""
#from collections import defaultdict
import re
class Tracker(object):
    def __init__(self):
        self.current_node = 1
        self.explored = set()
        self.explored2 = {}
        self.min_length = {}
        self.start_node = 1
        self.goal = set([7,37,59,82,99,115,133,165,188,197])

        
def make_graph(file):
    graph = {}
    for line in file:
        x = re.findall(r"[\w']+", line)
        graph.setdefault(int(x[0]), [x[i:i+2] for i in range(1, len(x), 2)])
    for key, value in graph.items():
        for lists in value:
            for number in range(len(lists)):
                lists[number] = int(lists[number])
    return graph
    
    
def dijkstra(graph, tracker):
    if tracker.current_node == tracker.start_node:
        for distance in graph[tracker.current_node]:
            tracker.min_length[distance[0]] = distance[1]
            # find a better way
            tracker.explored2[distance[0]] = distance[1]
            tracker.explored.add(tracker.current_node)
        del tracker.explored2[tracker.current_node]

    tracker.current_node = min(tracker.explored2, key=tracker.explored2.get)
    if tracker.current_node not in tracker.explored:
        for distance in graph[tracker.current_node]:
            if distance[0] not in tracker.explored:
                current_distance = tracker.min_length[tracker.current_node]
                if current_distance + distance[1] < tracker.min_length[distance[0]]:
                    tracker.min_length[distance[0]] = current_distance + distance[1]
                    # find a better way
                    tracker.explored2[distance[0]] = current_distance + distance[1]
    tracker.explored.add(tracker.current_node)
    #find a better way
    del tracker.explored2[tracker.current_node]
    if tracker.goal.issubset(tracker.explored):
        return tracker
    dijkstra(graph, tracker)

def main():
    file = open('dijkstraData.txt')
    graph = make_graph(file)
    tracker = Tracker()
    for nodes, edges in graph.items():
        tracker.min_length.setdefault(nodes, 1000000)
        tracker.explored2.setdefault(nodes, 1000000)
    dijkstra(graph, tracker)
    return tracker.min_length[7], tracker.min_length[37], tracker.min_length[59], tracker.min_length[82], tracker.min_length[99], tracker.min_length[115], tracker.min_length[133], tracker.min_length[165], tracker.min_length[188], tracker.min_length[197]
    
    
if __name__ == "__main__":   
    print(main())