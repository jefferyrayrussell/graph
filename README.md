# data-structures

Classic Data Structure Assignments

__authors:__ Zach Rickert and Jeffery Russell

__date:__ 8/17/2016

These modules are recreations of classic data structures.


###Graph###

A Graph in Python.

A Graph is A graph is a set of (vertices, nodes, points) and a 
collection of (edges, lines, arcs) that each connect a pair of vertices.  
Nodes and edges are the key attributes of a graph.

__Methods__:
* g.nodes(): return a list of all nodes in the graph
* g.edges(): return a list of all edges in the graph
* g.add_node(n): adds a new node ‘n’ to the graph
* g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and 
    'n2’, if either n1 or n2 are not already present in the graph, they 
    should be added.
* g.del_node(n): deletes the node ‘n’ from the graph, raises an error if 
    no such node exists
* g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the 
    graph, raises an error if no such edge exists.
* g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
* g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, 
    raises an error if n is not in graph.
* g.adjacent(n1, n2): returns True if there is an edge connecting n1 and 
    n2, False if not, raises an error if either of the supplied nodes are 
    not in graph.
* g.depth_first_traversal(start): Perform a full depth-first traversal of 
    the graph beginning at start. Return the full visited path when 
    traversal is complete.
* g.breadth_first_traversal(start): Perform a full breadth-first traversal 
    of the graph, beginning at start. Return the full visited path when 
    traversal is complete.
* g.weighting(): Allows edges of graph to have weight.