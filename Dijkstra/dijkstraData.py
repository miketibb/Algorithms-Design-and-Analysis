# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:27:11 2016

@author: Mike
"""
import re
class Tracker(object):
    def __init__(self):
        self.current_node = 1
        self.explored = set()
        self.min_length = {}
        self.start_node = 1

# returns a dict where keys are the nodes
# values are a list of 2 items, first item is the node it is attached to
# second value is the length of the arc       
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
    
# checks all the arc lengths from the current_node to any adjacent nodes
# that have not already been explored. If the combined length is less than
# the current min_length for the node min_length[key] is overwritten.
def dijkstra(graph, tracker, goal):
    if tracker.current_node == tracker.start_node:
        for distance in graph[tracker.current_node]:
            tracker.min_length[distance[0]] = distance[1]
            tracker.explored.add(tracker.current_node)

    tracker.current_node = min(set(tracker.min_length)-tracker.explored,
                               key=tracker.min_length.get)
    if tracker.current_node not in tracker.explored:
        for distance in graph[tracker.current_node]:
            if distance[0] not in tracker.explored:
                current_distance = tracker.min_length[tracker.current_node]
                if current_distance + distance[1] < tracker.min_length[distance[0]]:
                    tracker.min_length[distance[0]] = current_distance + distance[1]
    tracker.explored.add(tracker.current_node)
    if set(goal).issubset(tracker.explored):
        return tracker
    dijkstra(graph, tracker, goal)

def main():
    file = open('dijkstraData.txt')
    graph = make_graph(file)
    tracker = Tracker()
    for nodes, edges in graph.items():
        tracker.min_length.setdefault(nodes, 1000000)
    goal = [7,37,59,82,99,115,133,165,188,197]
    dijkstra(graph, tracker, goal)
    return [tracker.min_length[i] for i in goal]
    
    
if __name__ == "__main__":   
    print(main())