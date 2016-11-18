##Djikstra's Algorithm
Dijksrta's algorithm is another algorithm which finds the shortest path. The difference between this
and past algorithms is that this computes the shortest distance when the arc lengths vary. It works
very similarly to depth first search but has a few tweaks. It starts at a given node and then explores
all lengths of the arcs to all adjacent nodes. These lengths are saved as the minimum length to that
node. The algorithm then picks one of the nodes adjacent the starting node and explores all the lengths
connected to it. It adds the length needed to reach this node to the newly explored arc lengths in order
to calculate the distances to the new nodes. If the length to any of the newly explored nodes is 
shorter than the previous length to that node the minimum length is overwritten and saved. The algorithm
explores the distances to all the nodes it can reach and calculates the minimum distance to each node.
The algorithm runs in O(mn) time, where m is the number of edges and n is the number of nodes.