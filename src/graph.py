
class GNode(object):
    """Create a GNode Constructor."""

    def __init__(self, value):
        """Create an instance of a GNode with the attribues of a value and a list of edges."""
        self.value = value
        self.edges = set()

    def __str__(self):
        return 'Node: {}'.format(str(self.value)


class Graph(object):
    """Create a Graph Constructor."""

    def __init__(self):
        """Create an instance of a Graph that has a list of nodes."""
        self.set_of_nodes = set()

    def add_node(self, new_node):
        """Adds a new node to the graph"""
        self.set_of_nodes.add(new_node)


    def has_node(self, node):
        """True if node 'n' is contained in the graph, False if not."""
        return node in self.set_of_nodes


    def add_edge(self, node1, node2):
        """Adds a new edge to the graph connecting 'n1' and 'n2'; if either n1 or n2 are not lready present in the graph, they should be added."""
        self.set_of_nodes.add(node1)
        self.set_of_nodes.add(node2)
        node1.edges.add(node2)


    def del_edge(self, node1, node2):
        """Delete the edge connecting 'n1' and 'n2' from the graph, raises a Key Error if no such edge exists."""
        try:
            node1.edges.remove(node2)
        except KeyError:
            raise KeyError ('Edge that you are trying to exist does not exist.')

    def del_node(self, node_to_del):
        '''del_node deletes the node 'n' from the graph, raises an error if no such node exists'''
        try:
            self.set_of_nodes.remove(node_to_del)
        except KeyError:
            raise KeyError ('Node does not exist in graph.')

        for node in self.set_of_nodes:
            try:
                node.edges.remove(node_to_del)
            except KeyError:
                pass

    def nodes(self):
        pass




# nodes() return a list of all the nodes in a graph
# for node in list of nodes
# print node

# edges() return a list of all edges in the graph
# for node in list of nodes
# print the list of edges for that node


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









