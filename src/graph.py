# -*- coding: utf-8 -*-
"""Graph Data Structure with Dijkstra Algorithm Implimentation Code."""


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
        """Determine the presence of a node."""
        return value in self.set_of_nodes

    def add_edge(self, value1, value2, weight):
        """Add edge and weight."""
        if not self.has_node(value1):
            self.add_node(value1)
        if not self.has_node(value2):
            self.add_node(value2)
        self.gnodes[value1][value2] = weight

    def del_edge(self, value1, value2):
        """Remove edge between two nodes."""
        try:
            del(self.gnodes[value1][value2])
        except KeyError:
            raise KeyError('Edge that you are trying to exist does not exist.')

    def del_node(self, value):
        """Remove a node."""
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
        """Return a list of nodes."""
        return list(self.set_of_nodes)

    def edges(self):
        """Return a list of edges."""
        edge_list = []
        for node in self.gnodes:
            for key in self.gnodes[node]:
                edge = '{0}->{1}'.format(node, key)
                edge_list.append(edge)
        return edge_list

    def adjacent(self, node1, node2):
        """Determine if two nodes are adjacent."""
        if not(node1 in self.set_of_nodes and node2 in self.set_of_nodes):
            raise TypeError('A node is not in the graph.')
        return node2 in self.gnodes[node1]

    def neighbors(self, node):
        """Return a list of neighbors."""
        return list(self.gnodes[node])

    def breadth_first_traversal(self, start):
        """Return visited path of completed breadth traversal."""
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
        """Return visited path of completed breadth traversal."""
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

    def dijkstra(self, start_node, end_node):
        """Implementation of Dijkstra Algorithm."""
        my_dict = self.dijkstra_init()
        my_dict[start_node]['distance'] = 0

        while True:
            current_node = self.dijkstra_select_node(my_dict)
            if current_node == end_node:
                break
            if current_node is None:
                raise ValueError
            my_dict = self.dijkstra_update_distances(my_dict, current_node)

        return self.dijkstra_length_path(my_dict, end_node)

    def dijkstra_init(self):
        """Initialization of Dijkstra Algorithm."""
        my_dict = {}
        for key in self.gnodes:
            my_dict[key] = {}
            my_dict[key]["visited"] = False
        return my_dict

    def dijkstra_select_node(self, my_dict):
        """Select the current shortest distance between two nodes."""
        smallest_length = 0
        for node in my_dict:
            try:
                current_length = my_dict[node]['distance']
            except KeyError:
                continue
            if not my_dict[node]['visited']:
                if current_length < smallest_length or smallest_length == 0:
                    smallest_length = current_length
                    current_node = node
        try:
            return current_node
        except NameError:
            return None

    def dijkstra_update_distances(self, my_dict, current_node):
        """Update current distance during traversal."""
        current_length = my_dict[current_node]['distance']
        for node in self.neighbors(current_node):
            new_length = current_length + self.gnodes[current_node][node]
            try:
                if new_length >= my_dict[node]['distance']:
                    continue
            except KeyError:
                pass

            my_dict[node]['distance'] = new_length
            my_dict[node]['previous_node'] = current_node

        my_dict[current_node]['visited'] = True
        return my_dict

    def dijkstra_length_path(self, my_dict, end_node):
        """Return length and list of previous nodes."""
        current_node = end_node
        node_list = [end_node]
        while True:
            try:
                node_list.append(my_dict[current_node]['previous_node'])
            except KeyError:
                break
            current_node = my_dict[current_node]['previous_node']
        return my_dict[end_node]['distance'], node_list

    def bellman(self, start):
        """An implimentation of the Bellman-Ford algorithm."""
        my_dict = self.bellman_init()
        list_of_nodes = list(self.set_of_nodes)
        my_dict[start]['distance'] = 0
        has_changed = True
        for itteration in range(len(list_of_nodes) - 2):
            itteration_change = False
            for node in list_of_nodes:
                my_dict, has_changed = self.bellman_update_distance(my_dict, node)
                itteration_change = itteration_change or has_changed
            if not itteration_change:
                break
        else:
            itteration_change = False
            for node in list_of_nodes:
                my_dict, has_changed = self.bellman_update_distance(my_dict, node)
                itteration_change = itteration_change or has_changed
            if itteration_change:
                raise ArithmeticError("Graph contains a negative-weight cycle")

        return my_dict

    def bellman_init(self):
        """Initialize the bellman function."""
        my_dict = {}
        for node in self.gnodes:
            my_dict[node] = {}
            my_dict[node]["distance"] = float("inf")
            my_dict[node]["prev_node"] = None
        return my_dict

    def bellman_update_distance(self, my_dict, current_node):
        """Update current distance during traversal."""
        has_changed = False
        if my_dict[current_node]['distance'] is not None:
            current_length = my_dict[current_node]['distance']
            for node in self.neighbors(current_node):
                new_length = current_length + self.gnodes[current_node][node]
                if new_length >= my_dict[node]['distance']:
                        continue

                my_dict[node]['distance'] = new_length
                my_dict[node]['prev_node'] = current_node
                has_changed = True

        return my_dict, has_changed


if __name__ == '__main__':  # pragma: no cover

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
