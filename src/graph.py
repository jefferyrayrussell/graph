class Graph(object):
    """Create a Graph Constructor."""

    def __init__(self):
        """Create an instance of a Graph that has a list of nodes."""
        self.gnodes = {}
        self.set_of_nodes = set()

    def add_node(self, value):
        """Add a new node to the graph."""
        if value not in self.set_of_nodes:
            try:
                self.gnodes[value] = {}
                self.set_of_nodes.add(value)
            except TypeError:
                raise TypeError('Nodes value need to be a hashable type.')


    def has_node(self, value):
        return value in self.set_of_nodes


    def add_edge(self, value1, value2, weight):
        # import pdb; pdb.set_trace()
        if not self.has_node(value1):
            self.add_node(value1)
        if not self.has_node(value2):
            self.add_node(value2)
        self.gnodes[value1][value2] = weight


    def del_edge(self, value1, value2):
        try:
            del(self.gnodes[value1][value2])
        except KeyError:
            raise KeyError('Edge that you are trying to exist does not exist.')


    def del_node(self, value):
        try:
            self.set_of_nodes.remove(value)
        except KeyError:
            raise KeyError('Node does not exist in graph.')
        del(self.gnodes[value])
        for node in self.gnodes:
            try:
                del(self.gnodes[node][value])
            except KeyError:
                pass

    def nodes(self):
        return list(self.set_of_nodes)


    def edges(self):
        edge_list = []
        for node in self.gnodes:
            for key in self.gnodes[node]:
                edge = '{0}->{1}'.format(node, key)
                edge_list.append(edge)
        return edge_list


    def adjacent(self, node1, node2):
        if not(node1 in self.set_of_nodes and node2 in self.set_of_nodes):
            raise TypeError('A node is not in the graph.')
        return node2 in self.gnodes[node1]


    def neighbors(self, node):
        return list(self.gnodes[node])


    def breadth_first_traversal(self, start):
        """Return the full visited path when breadth traversal is complete after starting with any node."""
        if self.has_node(start):
            traversal = []
            traversal.append(start)
            index = 0
            while True:
                try:
                    traversal.extend([x for x in self.neighbors(traversal[index]) if x not in traversal])
                except IndexError:
                    break
                index += 1
            return traversal


    def depth_first_traversal(self, start):
        """Return the full visited path when depth traversal is complete after starting with any node."""
        if self.has_node(start):
            traversal = []
            traversal = self.depth_traversal_add_node(start, traversal)
            return traversal


    def depth_traversal_add_node(self, start, traversal):
        """Add node for depth_first_traversal."""
        if start in traversal:
            return traversal
        else:
            traversal.append(start)
            for edge in [x for x in self.neighbors(start) if x not in traversal]:
                self.depth_traversal_add_node(edge, traversal)
            return traversal

    """
    Pseudo-Code for Dijkstra's Algorithm used to find the shortest
    path between two nodes.

    Function will take two nodes of a graph data structure and return
    the shortest path between those two nodes.  The return will be the
    path of nodes in a list and the total weight.

    Set up a dictionary whose keys are each individual node in the graph
    structure and the value for each key will be a second dictionary.
    That second dictionary contains keys that will be distance,
    previous node, and has been visited node (true or false).

    Begin with a start_node A whose distance is set to 0.
    For neighbors of A:
        distance equals the weight of the edge between A and the neighbor.
        previous node equals A
    Start node A becomes visited.
    We need to traverse through each of the nodes in the dictionary my_dict
    and determine which node has the shortest distance.  That node with
    the shortest distance becomes the current node.  We reiterate through
    the dictionary.  We process the neighbors of the new current node.


    """

    def dijkstra(self, start_node, end_node):
        """Implementation of Dijkstra Algorithm to determine the shortest distance between two nodes."""
        my_dict = self.dijkstra_init()
        my_dict[start_node]['distance'] = 0
        for neighbor in self.neighbors(start_node):
            my_dict[neighbor]['distance'] = self.gnodes[start_node][neighbor]
            my_dict[neighbor]['previous_node'] = start_node
        my_dict[start_node]['visited'] = True
        return my_dict


    def dijkstra_init(self):
        """Implementation of Dijkstra Algorithm to determine the shortest distance between two nodes."""
        my_dict = {}
        for key in self.gnodes:
            my_dict[key] = {}
            my_dict[key]["distance"] = None
            my_dict[key]["visited"] = False
        return my_dict

    def dijkstra_select_node(self, my_dict):
        """Select the current shortest distance"""
        smallest_length = 0
        for node in my_dict:
            try:
                current_length = my_dict[node]['distance']
            except KeyError:
                continue
            if current_length < smallest_length or smallest_length = 0:
                smallest_length = current_length
                current_node = node
        try:
            return current_node
        except NameError:
            return None
            





if __name__ == '__main__':              # pragma: no cover

    g6 = Graph()
    node_list = list('abcdefghijk')
    g6.add_edge(node_list[0], node_list[1], 0)
    g6.add_edge(node_list[0], node_list[2], 0)
    g6.add_edge(node_list[1], node_list[3], 0)
    g6.add_edge(node_list[1], node_list[4], 0)
    g6.add_edge(node_list[1], node_list[5], 0)
    g6.add_edge(node_list[2], node_list[6], 0)
    g6.add_edge(node_list[2], node_list[7], 0)
    g6.add_edge(node_list[7], node_list[8], 0)
    g6.add_edge(node_list[5], node_list[9], 0)
    g6.add_edge(node_list[9], node_list[10], 0)
    btraversal = g6.breadth_first_traversal(node_list[0])
    dtraversal = g6.depth_first_traversal(node_list[0])
    print('\nTest #6 - Breadth')
    print(btraversal)
    print('\nTest #6 - Depth')
    print(dtraversal)

    g7 = Graph()
    node_list = list('abcdefghijk')
    g7.add_edge(node_list[0], node_list[1], 0)
    g7.add_edge(node_list[0], node_list[2], 0)
    g7.add_edge(node_list[1], node_list[3], 0)
    g7.add_edge(node_list[2], node_list[4], 0)
    g7.add_edge(node_list[2], node_list[5], 0)
    g7.add_edge(node_list[5], node_list[6], 0)
    g7.add_edge(node_list[6], node_list[7], 0)
    g7.add_edge(node_list[6], node_list[8], 0)
    g7.add_edge(node_list[6], node_list[9], 0)
    g7.add_edge(node_list[9], node_list[10], 0)
    btraversal = g7.breadth_first_traversal(node_list[0])
    dtraversal = g7.depth_first_traversal(node_list[0])
    print('\nTest #7 - Breadth')
    print(btraversal)
    print('\nTest #7 - Depth')
    print(dtraversal)

    g8 = Graph()
    node_list = list('abcdefghijk')
    g8.add_edge(node_list[0], node_list[1], 0)
    g8.add_edge(node_list[1], node_list[2], 0)
    g8.add_edge(node_list[1], node_list[3], 0)
    g8.add_edge(node_list[2], node_list[4], 0)
    g8.add_edge(node_list[2], node_list[3], 0)
    g8.add_edge(node_list[3], node_list[4], 0)
    g8.add_edge(node_list[3], node_list[7], 0)
    g8.add_edge(node_list[4], node_list[2], 0)
    g8.add_edge(node_list[4], node_list[5], 0)
    g8.add_edge(node_list[5], node_list[6], 0)
    g8.add_edge(node_list[5], node_list[3], 0)
    g8.add_edge(node_list[7], node_list[0], 0)
    g8.add_edge(node_list[7], node_list[8], 0)
    g8.add_edge(node_list[7], node_list[10], 0)
    g8.add_edge(node_list[8], node_list[5], 0)
    g8.add_edge(node_list[8], node_list[6], 0)
    btraversal = g8.breadth_first_traversal(node_list[5])
    dtraversal = g8.depth_first_traversal(node_list[5])
    print('\nTest #8 - Breadth')
    print(btraversal)
    print('\nTest #8 - Depth')
    print(dtraversal)

    g9 = Graph()
    node_list = list('abcdefghijk')
    g9.add_edge(node_list[0], node_list[1], 0)
    g9.add_edge(node_list[0], node_list[2], 0)
    g9.add_edge(node_list[1], node_list[3], 0)
    g9.add_edge(node_list[1], node_list[4], 0)
    g9.add_edge(node_list[1], node_list[5], 0)
    g9.add_edge(node_list[2], node_list[1], 0)
    g9.add_edge(node_list[4], node_list[7], 0)
    g9.add_edge(node_list[5], node_list[7], 0)
    g9.add_edge(node_list[7], node_list[10], 0)
    g9.add_edge(node_list[7], node_list[8], 0)
    g9.add_edge(node_list[8], node_list[9], 0)
    btraversal = g9.breadth_first_traversal(node_list[0])
    dtraversal = g9.depth_first_traversal(node_list[0])
    print('\nTest #9 - Breadth')
    print(btraversal)
    print('\nTest #9 - Depth')
    print(dtraversal)
