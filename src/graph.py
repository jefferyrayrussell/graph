
class GNode(object):
    """Create a GNode Constructor."""

    def __init__(self, value):
        """Create an instance of a GNode with the attribues of a value and a list of edges."""
        self.value = value
        self.edges = []


class Graph(object):
    """Create a Graph Constructor."""

    def __init__(self):
        """Create an instance of a Graph that has a list of nodes."""
        self.list_of_nodes = []

    def add_node(self, new_node):
        """Adds a new node to the graph"""
        self.list_of_nodes.append(new_node)


    def has_node(self, node):
        """True if node 'n' is contained in the graph, False if not."""
        return node in self.list_of_nodes


    def add_edge(self, node1, node2):
        """Adds a new edge to the graph connecting 'n1' and 'n2'; if either n1 or n2 are not lready present in the graph, they should be added."""
        pass




# nodes() return a list of all the nodes in a graph
# for node in list of nodes
# print node

# edges() return a list of all edges in the graph
# for node in list of nodes
# print the list of edges for that node


# add.edge(n1,n2) adds a new edge to the graph connetion 'n1' and 'n2'; if either n1 or n2 are not lready present in the graph, they should be added.
# if n1 or n2 is not in the current list of nodes
#     then add.node(n) with the new node as the argument
# append n2 to n1's list of nodes

# del_node(n) deletes the node 'n' from the graph, raises an error if no such node exists
# check to see that node n is in the current list of nodes
#     if not in list raise error
#     if in list 
#         delete node from list of nodes
#         for node in list of nodes
#             look for the node in the list of edges for the remaining nodes
#             remove edge from the node

# del_edge(n1, n2) deletes the edge connecting 'n1' and 'n2' from the graph, raises an eror if no such edge exists.
#     if not in the list of edges raise error
#     if in list
#         delete edge from the n1

# neighbors(n) returns the list of all nodes connected to 'n' by edges, raise an error if n is not in g.
#     check has.node 
#     if False, return error
#     else return edges from node n (check with instructor regarding one way or two way arrows)

# adjacent(n1,n2) returns true if there is an edge connecting n1 and n2, False if not, raises an error if either node not in list.
#     check if nodes in list
#     if false, return error
#     if true check if n2 is an edge of n1
#         if true return true,
#         if not return false.









