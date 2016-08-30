

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

    def __eq__(self, other):
        """Allow comparison of two equal edges."""
        return self.begin == other.begin and self.end == other.end

    def __ne__(self, other):
        """Allow comparison of two unequal edges."""
        return self.begin != other.begin or self.end != other.end


class Graph(object):
    """Create a Graph Constructor."""

    def __init__(self):
        """Create an instance of a Graph that has a list of nodes."""
        self.set_of_nodes = set()

    def add_node(self, new_node):
        """Add a new node to the graph."""
        self.is_node(new_node)
        self.set_of_nodes.add(new_node)

    def is_node(self, node):
        """Check to see if object is a node. Returns a TypeError if it is not a node."""
        if isinstance(node, GNode):
            return True
        else:
            raise TypeError('{} is not a GNode type.'.format(str(node)))

    def has_node(self, node):
        """True if node 'n' is contained in the graph, False if not."""
        self.is_node(node)
        return node in self.set_of_nodes

    def add_edge(self, node1, node2):
        """Add a new edge to the graph connecting 'n1' and 'n2'; if either n1 or n2 are not lready present in the graph, they should be added."""
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
            raise KeyError('Edge that you are trying to exist does not exist.')
        except AttributeError:
            raise TypeError('{} is not a GNode type.'.format(str(node1)))

    def del_node(self, node_to_del):
        """Delete a node from the graph, raises an error if no such node exists."""
        try:
            self.set_of_nodes.remove(node_to_del)
        except KeyError:
            raise KeyError('Node does not exist in graph.')

        for node in self.set_of_nodes:
            try:
                node.edges.remove(node_to_del)
            except KeyError:
                pass

    def nodes(self):
        """Return a list of nodes."""
        return list(self.set_of_nodes)

    def edges(self):
        """Return a list of edges."""
        list_of_edges = []
        for node in self.set_of_nodes:
            for edge in node.edges:
                list_of_edges.append(Edge(node, edge))
        return list_of_edges

    def adjacent(self, node1, node2):
        """Return true if two nodes are connected by an edge, false if not connected.  Will raise a TypeError is one node is not in the graph."""
        self.is_node(node1)
        self.is_node(node2)
        if not self.has_node(node1) or not self.has_node(node2):
            raise KeyError('Cannot check adjacent on a node that is not in the graph.')
        else:
            return node2 in node1.edges

    def neighbors(self, node):
        """Return the list of all nodes connected to a node by edges, raise an error if node is not in graph."""
        if node not in self.set_of_nodes:
            raise KeyError("{} isn't a node in the graph".format(node))
        else:
            return list(node.edges)

    def breadth_first_traversal(self, start):
        """Return the full visited path when breadth traversal is complete after starting with any node."""
        self.is_node(start)
        traversal = []
        traversal.append(start)
        index = 0
        while True:
            try:
                traversal.extend([x for x in traversal[index].edges if x not in traversal])
            except IndexError:
                break
            index += 1
        return traversal

    def depth_first_traversal(self, start):
        """Return the full visited path when depth traversal is complete after starting with any node."""
        self.is_node(start)
        traversal = []
        traversal = self.depth_traversal_add_node(start, traversal)
        return traversal

    def depth_traversal_add_node(self, start, traversal):
        """Add node for depth_first_traversal."""
        if start in traversal:
            return traversal
        else:
            traversal.append(start)
            for edge in [x for x in start.edges if x not in traversal]:
                self.depth_traversal_add_node(edge, traversal)
            return traversal


if __name__ == '__main__':

    g6 = Graph()
    node_list = list('abcdefghijk')
    for index, letter in enumerate(node_list):
        node_list[index] = GNode(letter)
    g6.add_edge(node_list[0], node_list[1])
    g6.add_edge(node_list[0], node_list[2])
    g6.add_edge(node_list[1], node_list[3])
    g6.add_edge(node_list[1], node_list[4])
    g6.add_edge(node_list[1], node_list[5])
    g6.add_edge(node_list[2], node_list[6])
    g6.add_edge(node_list[2], node_list[7])
    g6.add_edge(node_list[7], node_list[8])
    g6.add_edge(node_list[5], node_list[9])
    g6.add_edge(node_list[9], node_list[10])
    btraversal = g6.breadth_first_traversal(node_list[2])
    dtraversal = g6.depth_first_traversal(node_list[2])
    print('\nTest #6')
    for node in btraversal:
        print(node.value)
    print('\nTest #6')
    for node in dtraversal:
        print(node.value)

    g7 = Graph()
    node_list = list('abcdefghijk')
    for index, letter in enumerate(node_list):
        node_list[index] = GNode(letter)
    g7.add_edge(node_list[0], node_list[1])
    g7.add_edge(node_list[0], node_list[2])
    g7.add_edge(node_list[1], node_list[3])
    g7.add_edge(node_list[2], node_list[4])
    g7.add_edge(node_list[2], node_list[5])
    g7.add_edge(node_list[5], node_list[6])
    g7.add_edge(node_list[6], node_list[7])
    g7.add_edge(node_list[6], node_list[8])
    g7.add_edge(node_list[6], node_list[9])
    g7.add_edge(node_list[9], node_list[10])
    btraversal = g7.breadth_first_traversal(node_list[0])
    dtraversal = g7.depth_first_traversal(node_list[0])
    print('\nTest #7')
    for node in btraversal:
        print(node.value)
    print('\nTest #7')
    for node in dtraversal:
        print(node.value)

    g8 = Graph()
    node_list = list('abcdefghijk')
    for index, letter in enumerate(node_list):
        node_list[index] = GNode(letter)
    g8.add_edge(node_list[0], node_list[1])
    g8.add_edge(node_list[1], node_list[2])
    g8.add_edge(node_list[1], node_list[3])
    g8.add_edge(node_list[2], node_list[4])
    g8.add_edge(node_list[2], node_list[3])
    g8.add_edge(node_list[3], node_list[4])
    g8.add_edge(node_list[3], node_list[7])
    g8.add_edge(node_list[4], node_list[2])
    g8.add_edge(node_list[4], node_list[5])
    g8.add_edge(node_list[5], node_list[6])
    g8.add_edge(node_list[5], node_list[3])
    g8.add_edge(node_list[7], node_list[0])
    g8.add_edge(node_list[7], node_list[8])
    g8.add_edge(node_list[7], node_list[10])
    g8.add_edge(node_list[8], node_list[5])
    g8.add_edge(node_list[8], node_list[6])
    btraversal = g8.breadth_first_traversal(node_list[5])
    dtraversal = g8.depth_first_traversal(node_list[5])
    print('\nTest #8')
    for node in btraversal:
        print(node.value)
    print('\nTest #8')
    for node in dtraversal:
        print(node.value)

    g9 = Graph()
    node_list = list('abcdefghijk')
    for index, letter in enumerate(node_list):
        node_list[index] = GNode(letter)
    g9.add_edge(node_list[0], node_list[1])
    g9.add_edge(node_list[0], node_list[2])
    g9.add_edge(node_list[1], node_list[3])
    g9.add_edge(node_list[1], node_list[4])
    g9.add_edge(node_list[1], node_list[5])
    g9.add_edge(node_list[2], node_list[1])
    g9.add_edge(node_list[4], node_list[7])
    g9.add_edge(node_list[5], node_list[7])
    g9.add_edge(node_list[7], node_list[10])
    g9.add_edge(node_list[7], node_list[8])
    g9.add_edge(node_list[8], node_list[9])
    btraversal = g9.breadth_first_traversal(node_list[0])
    dtraversal = g9.depth_first_traversal(node_list[0])
    print('\nTest #9')
    for node in btraversal:
        print(node.value)
    print('\nTest #9')
    for node in dtraversal:
        print(node.value)
