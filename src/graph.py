

class GNode(object):
    """Create a GNode Constructor."""

    def __init__(self, value):
        """Create an instance of a GNode with the attribues of a value and a list of edges."""
        self.value = value
        self.edges = set()


class Edge(object):
    """Create an Edge Constructor."""

    def __init__(self, begin, end):
        """Create an instance of an edge."""
        self.begin = begin
        self.end = end


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
        """Checks to see if object is a node. Returns a TypeError if it is not a node."""
        if isinstance(node, GNode):
            return True
        else:
            raise TypeError('{} is not a GNode type.'.format(str(node)))

    def has_node(self, node):
        """True if node 'n' is contained in the graph, False if not."""
        self.is_node(node)
        return node in self.set_of_nodes


    def add_edge(self, node1, node2):
        """Adds a new edge to the graph connecting 'n1' and 'n2'; if either n1 or n2 are not lready present in the graph, they should be added."""
        self.is_node(node1)
        self.is_node(node2)
        self.set_of_nodes.add(node1)
        self.set_of_nodes.add(node2)
        node1.edges.add(node2)


    def del_edge(self, node1, node2):
        """Delete the edge connecting 'n1' and 'n2' from the graph, raises a Key Error if no such edge exists."""
        try:
            node1.edges.remove(node2)
        except KeyError:
            raise KeyError ('Edge that you are trying to exist does not exist.')
        except AttributeError:
            raise TypeError('{} is not a GNode type.'.format(str(node1)))

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
        return list(self.set_of_nodes)


    def edges(self):
        list_of_edges = []
        for node in self.set_of_nodes:
            for edge in node.edges:
                list_of_edges.append(Edge(node, edge))
        return list_of_edges

    def adjacent(self, node1, node2):
        self.is_node(node1)
        self.is_node(node2)
        if not self.has_node(node1) or not self.has_node(node2):
            raise KeyError('Cannot check adjacent on a node that is not in the graph.')
        else:
            return node2 in node1.edges


    def neighbors(self, node):
        '''Return the list of all nodes connected to 'n' by edges, raise an error if node is not in graph.'''
        if node not in self.set_of_nodes:
            raise KeyError("{} isn't a node in the graph".format(node))
        else:
            return list(node.edges)

