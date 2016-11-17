##Kosaraju's Two-Pass Algorithm
This is probably the the most difficult algorithm that is covered in the course but is really fascinating.
It covers how to discover strongly connected components in a directed graph. I think of strongly connected
components as miniature graphs inside the larger graph. They are nodes which all connect to each other 
but there is only one way in or out strongly connected component.

The way this algorithm works is by first reversing all the arcs in the directed graph. Starting at the last
node we work backwards, discovering the finishing times for every node. The finishing time for a node is 
when we have run Depth First Search and we run out of places to go and we have to start backtracking. The 
last node to be explored in the DFS gets the finishing time of 1. The node explored just before that gets a
finishing time of 2 and etc. until all nodes that we have already seen are given a finishing time. After
we have explored all of those nodes we move to the highest node which has not yet been explored and repeat
the process, once again assigning finishing times. After finishing times for all nodes have been recorded we
reverse the edges back to their original starting directions and starting with the node with the highest
finishing time we record we again run DFS. The difference this time though is that we record the leader. The
leader is the starting node of the DFS. If a node can be reached from that DFS then it is recorded to the leader.
Once a DFS terminates it moves to the node with the highest finishing time and runs DFS again starting at that
node and recording all the subsequent nodes to that leader. After this is done you are done! Every node reached
from a DFS with a shared leader is an acyclic graph or strongly connected component. Return these groupings
and there you have it.

This is one of those 'magical' algorithms that even once you know how it works you really still don't feel like
you know how it works. The running time is O(m + n) where m is the number of edges and n is the number of
nodes. This was one of my favorite algorithms from course but it can take a while to wrap you head around.