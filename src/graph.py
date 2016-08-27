
class GNode(object):
    """Create a GNode Constructor."""

    def __init__(self, value):
        """Create an instance of a GNode with the attribues of a value and a list of edges."""
        self.value = value
        self.edges = set()

    def __str__(self):
        return 'Node: {}'.format(str(self.value))

    def print_edges(self):
        list_of_edge_values = []
        for edge in self.edges:
            list_of_edge_values.append(str(edge.value))
        return 'Edges: {0}'.format(', '.join(list_of_edge_values))


class Graph(object):
    """Create a Graph Constructor."""

    def __init__(self):
        """Create an instance of a Graph that has a list of nodes."""
        self.set_of_nodes = set()

    def add_node(self, new_node):
        """Adds a new node to the graph"""
        self.is_node(new_node)
        self.set_of_nodes.add(new_node)

    def is_node(self, node):
        """Checks to see if object is a node. Will run before adding to Graph."""
        if not isinstance(node, GNode):
            raise TypeError('{} is not a GNode type.'.format(str(node)))

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
        for node in self.set_of_nodes:
            print(node)

    def edges(self):
        for node in self.set_of_nodes:
            print('{0} {1}'.format(node, node.print_edges()))




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









