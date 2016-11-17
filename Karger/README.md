##Karger's Minimum Cuts
This is a really fun algorithm as it deals with determining what are the fewest number of cuts needed to split
a connected graph into 2 distinct paths. This project deals with undirected graphs but it can fairly easily
be generalized to directed graphs as well. As inputs we are given 200 rows of digits, the first column specifies
the node and the subsequent columns are the nodes which connect to that node. The purpose of this algorithm is 
to split the graph into two parts with the fewest number of edges crossing between the two groups. This is 
accomplished through contracting connecting nodes into one node.

We first contract the two connecting nodes into one and we remove the connected node. The new node has all the
attributes of the old node except it now now contains two vertices and all the edges coming from each (self
loops are deleted). This algorithm chooses random vertices to contract until all but two groups remain. After this
is done we will have two distinct groups each with a list of all the vertices that have been contracted and a list
of all the edges they connect too. If we are randomly contracting vertices the odds that any single run of this
algorithm will lead to the smallest number of edges between two groups is very small (precisely it is 1 / n C 2
where n is the number of vertices). If we repeat the process multiple times choosing different, random vertices
to contract each time we can boost the probability that it will find the minimum cut value. 