"""Testing of Graph Data Structure with Dijkstra Algorithm."""

import pytest


def test_graph_init_set_of_nodes(graph_empty):
    """Test for empty graph at initialization."""
    assert graph_empty.set_of_nodes == set()


def test_graph_add_node(graph_empty):
    """Test for adding node to empty graph."""
    graph_empty.add_node('gnode1')
    assert 'gnode1' in graph_empty.set_of_nodes


def test_graph_has_node_true(graph_empty):
    """Test that non empty graph is True."""
    graph_empty.add_node('gnode1')
    assert graph_empty.has_node('gnode1') is True


def test_graph_node_non_hashable(graph_empty):
    """Test that node is non hashable."""
    with pytest.raises(TypeError):
        graph_empty.add_node(['list'])


def test_graph_has_node_false(graph_empty):
    """Test that empty graph is False."""
    assert graph_empty.has_node('gnode1') is False


def test_graph_add_edge_both_nodes_in_graph(graph_two_node):
    """Test that edge is correctly added to two nodes."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_two_node.gnodes['gnode1']


def test_graph_add_edge_both_nodes_in_graph_check_edge_direction(graph_two_node):
    """Test that edge direction is correctly added in two node graph."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode1' not in graph_two_node.gnodes['gnode2']


def test_graph_add_edge_one_node_in_graph_check_edge(graph_one_node):
    """Test that edge is correctly added in one node graph."""
    graph_one_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_one_node.gnodes['gnode1']


def test_graph_add_edge_neither_node_in_graph_check_edge(graph_empty):
    """Test that edge not added to node in empty graph."""
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_empty.gnodes['gnode1']


def test_graph_add_edge_neither_node_in_graph_check_node1(graph_empty):
    """Test that edge not added to gnode1."""
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode1' in graph_empty.gnodes


def test_graph_add_edge_neither_node_in_graph_check_node2(graph_empty):
    """Test that edge not added to gnode2."""
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_empty.gnodes


def test_graph_del_edge_exists(graph_two_node):
    """Test that deleted edge doesn't exist."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    graph_two_node.del_edge('gnode1', 'gnode2')
    assert 'gnode2' not in graph_two_node.gnodes['gnode1']


def test_graph_del_edge_no_exists(graph_two_node):
    """Test that deleted edge doesn't exist."""
    with pytest.raises(KeyError):
        graph_two_node.del_edge('gnode1', 'gnode2')


def test_graph_del_node_exists_check_graph_for_node(graph_one_node):
    """Test that deleted node doesn't exist."""
    graph_one_node.del_node('gnode1')
    assert 'gnode1' not in graph_one_node.gnodes


def test_graph_del_node_exists_check_set_membership(graph_one_node):
    """Test that deleted node not in list."""
    graph_one_node.del_node('gnode1')
    assert 'gnode1' not in graph_one_node.set_of_nodes


def test_graph_del_node_no_exists(graph_one_node):
    """Test that deleted node raises key error."""
    with pytest.raises(KeyError):
        graph_one_node.del_node('gnode2')


def test_graph_del_node_check_edges(graph_empty):
    """Test that no edges remain with deleted node."""
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    graph_empty.del_node('gnode2')
    assert 'gnode2' not in graph_empty.gnodes['gnode1']


def test_graph_del_node_not_a_node(graph_empty):
    """Test that deleted node is not a node."""
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    with pytest.raises(KeyError):
        graph_empty.del_node('gnode3')


def test_graph_del_node_other_nodes_not_changed(graph_two_node):
    """Test that deleted node doesn't change other nodes.."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    graph_two_node.add_edge('gnode3', 'gnode1', 0)
    graph_two_node.del_node('gnode2')
    assert 'gnode1' in graph_two_node.gnodes['gnode3']


def test_adjacent_true(graph_two_node):
    """Test that adjacent node are truly adjacent."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert graph_two_node.adjacent('gnode1', 'gnode2')


def test_adjacent_false(graph_two_node):
    """Test that two non-adjacent nodes are not adjacent."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert graph_two_node.adjacent('gnode2', 'gnode1') is False


def test_adjacent_error_not_in_graph(graph_one_node):
    """Test that TypeError raised when node not in graph."""
    with pytest.raises(TypeError):
        graph_one_node.adjacent('gnode1', 'gnode2')


def test_neighbors_has_edges(graph_two_node):
    """Test that neighbors have edges."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert graph_two_node.neighbors('gnode1') == ['gnode2']


def test_neighbors_no_edges(graph_two_node):
    """Test that neighbors have no edges."""
    assert graph_two_node.neighbors('gnode1') == []


def test_neighbors_not_in_graph(graph_one_node):
    """Test that neighbors not in graph."""
    with pytest.raises(KeyError):
        graph_one_node.neighbors('gnode2')


def test_nodes_connected(graph_multi_node):
    """Test that nodes connected."""
    assert 'gn1' in graph_multi_node.gnodes


def test_nodes_connected_test_set_membership(graph_multi_node):
    """Test set membership for nodes connected."""
    assert 'gn1' in graph_multi_node.set_of_nodes


def test_nodes_unconnected(graph_multi_node):
    """Test that nodes uncoonected."""
    assert 'gn2' in graph_multi_node.gnodes


def test_nodes_unconnected_test_set_membership(graph_multi_node):
    """Test set membership for unconnected nodes."""
    assert 'gn2' in graph_multi_node.set_of_nodes


def test_nodes_list(graph_v):
    """Test for nodes in list."""
    assert sorted(graph_v.nodes()) == ['gnode1', 'gnode2', 'gnode3', 'gnode4', 'gnode5']


def test_edge_list(graph_cyclic):
    """Test for cyclic edges in graph."""
    assert sorted(graph_cyclic.edges()) == ['gnode1->gnode2', 'gnode2->gnode3', 'gnode3->gnode1']


def test_breadth_traversal_one_node(graph_one_node):
    """Test breadth traversal for one node graph."""
    assert graph_one_node.breadth_first_traversal('gnode1') == ['gnode1']


def test_depth_trasversal_one_node(graph_one_node):
    """Test depth traversal for one node graph."""
    assert graph_one_node.depth_first_traversal('gnode1') == ['gnode1']


def test_breadth_trasversal_two_node(graph_two_node):
    """Test breadth traversal for two node graph."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_two_node.breadth_first_traversal('gnode1')


def test_depth_traversal_two_node(graph_two_node):
    """Test depth traversal for two node graph."""
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_two_node.depth_first_traversal('gnode1')


def test_breadth_traversal_two_node_not_in_traversal(graph_two_node):
    """Test breadth traversal for two nodes not in traversal."""
    graph_two_node.add_edge('gnode2', 'gnode1', 0)
    assert 'gnode2' not in graph_two_node.breadth_first_traversal('gnode1')


def test_depth_traversal_two_node_not_in_traversal(graph_two_node):
    """Test depth traversal for two nodes not in traversal."""
    graph_two_node.add_edge('gnode2', 'gnode1', 0)
    assert 'gnode2' not in graph_two_node.depth_first_traversal('gnode1')


def test_depth_traversal_multi_node(graph_multi_node):
    """Test depth traversal for multinode graph."""
    assert 'gn5' in graph_multi_node.depth_first_traversal('gn1')


def test_breadth_traversal_cyclic(graph_cyclic):
    """Test cyclic graph with traversal."""
    assert 'gnode3' in graph_cyclic.breadth_first_traversal('gnode1')


def test_depth_traversal_cyclic(graph_cyclic):
    """Test cyclic graph with traversal"""
    assert 'gnode3' in graph_cyclic.depth_first_traversal('gnode1')


def test_order_breadth_transversal(graph_v):
    """Graph: 4->2->1<-3<-5 Check to see if children append before the children's children."""
    transversal = graph_v.breadth_first_traversal('gnode1')
    assert transversal.index('gnode2') < transversal.index('gnode5')


def test_order_depth_transversal(graph_v):
    """Graph: 4->2->1<-3<-5 Check to see if it goes to the bottom before other children."""
    transversal = graph_v.depth_first_traversal('gnode1')
    if transversal.index('gnode2') < transversal.index('gnode3'):
        assert transversal.index('gnode4') < transversal.index('gnode3')
    else:
        assert transversal.index('gnode5') < transversal.index('gnode2')


def test_graph_weight(graph_empty):
    """Test for graph weight in empty graph."""
    graph_empty.add_edge('gnode1', 'gnode2', 5)
    assert graph_empty.gnodes['gnode1']['gnode2'] == 5


def test_graph_weight_test_neg_amount(graph_empty):
    """Test for graph weight with negative amount."""
    graph_empty.add_edge('gnode1', 'gnode2', -5)
    assert graph_empty.gnodes['gnode1']['gnode2'] == -5


def test_graph_weight_not_set_is_key_error(graph_empty):
    """Test graph weight not set."""
    graph_empty.add_edge('gnode1', 'gnode2', 5)
    with pytest.raises(KeyError):
        graph_empty.gnodes['gnode2']['gnode1'] == 5


def test_graph_weight_reassign_weight(graph_empty):
    """Test graph weight reassigned."""
    graph_empty.add_edge('gnode1', 'gnode2', 2)
    graph_empty.add_edge('gnode1', 'gnode2', 7)
    assert graph_empty.gnodes['gnode1']['gnode2'] == 7


def test_dijkstra_dictionary_has_all_nodes(graph_multi_node):
    """Test that all nodes are present in the dictionary."""
    for key in graph_multi_node.gnodes:
        assert key in graph_multi_node.dijkstra_init()


def test_dijkstra_init_nodes_visited(graph_multi_node):
    """Test that each node visitied is false."""
    for key in graph_multi_node.dijkstra_init():
        assert graph_multi_node.dijkstra_init()[key]["visited"] is False


def test_dijkstra_startnode_zero_distance_value(graph_multi_node):
    """Test that start node has a beginning distance of zero."""
    assert graph_multi_node.dijkstra('gn1', 'gn1')[0] == 0


def test_dijkstra_nextnode_distance_value(graph_multi_node):
    """Test that the next node has a has a distance."""
    assert graph_multi_node.dijkstra('gn1', 'gn3')[0] == 7


def test_dijkstra_nextnode_previous_value(graph_multi_node):
    """Test that the previous node value gets set."""
    assert graph_multi_node.dijkstra('gn1', 'gn3')[1] == ['gn3', 'gn1']


def test_dijkstra_shortest_distance(graph_empty, dijkstra_dictionary):
    """Test that the edge with the shortest distance is selected."""
    assert graph_empty.dijkstra_select_node(dijkstra_dictionary) == "gn3"


def test_dijkstra_update_distances(graph_multi_node, dijkstra_dictionary):
    """Test that the distance is correctly updating."""
    new_dict = graph_multi_node.dijkstra_update_distances(dijkstra_dictionary, "gn3")
    assert new_dict["gn5"]['distance'] == 17


def test_dijkstra_initialize_distances(graph_multi_node, dijkstra_dictionary):
    """Test that the distance is correctly initializing."""
    new_dict = graph_multi_node.dijkstra_update_distances(dijkstra_dictionary, "gn3")
    assert new_dict["gn4"]['distance'] == 11


def test_dijkstra_total_distance(graph_multi_node, dijkstra_dictionary_final):
    """Test that the total distance is correctly returned."""
    total_length = graph_multi_node.dijkstra_length_path(dijkstra_dictionary_final, "gn5")[0]
    assert total_length == 13


def test_dijkstra_shortest_path(graph_multi_node, dijkstra_dictionary_final):
    """Test that the shortest path is correctly returned."""
    shortest_path = graph_multi_node.dijkstra_length_path(dijkstra_dictionary_final, "gn5")[1]
    assert shortest_path == ['gn5', 'gn4', 'gn3', 'gn1']


def test_dijkstra_not_connected(graph_multi_node, dijkstra_dictionary_final):
    """Test that the value error is raised when two nodes are not connected."""
    with pytest.raises(ValueError):
        graph_multi_node.dijkstra('gn1', 'gn2')


def test_bellman_has_all_nodes(graph_multi_node):
    for key in graph_multi_node.gnodes:
        assert key in graph_multi_node.bellman_init()


def test_bellman_init_distance(graph_multi_node):
    for key in graph_multi_node.gnodes:
        assert graph_multi_node.bellman_init()[key]['distance'] == float("inf")


def test_bellman_init_prev_node(graph_multi_node):
    for key in graph_multi_node.gnodes:
        assert graph_multi_node.bellman_init()[key]['prev_node'] is None


def test_bellman_startnode_zero_distance_value(graph_multi_node):
    """Test that start node has a beginning distance of zero."""
    assert graph_multi_node.bellman('gn1')['gn1']['distance'] == 0


def test_bellman_nextnode_distance_value(graph_multi_node):
    """Test that the next node has a has a distance."""
    assert graph_multi_node.bellman('gn1')['gn3']['distance'] == 7


def test_bellman_nextnode_previous_value(graph_multi_node):
    """Test that the previous node value gets set."""
    assert graph_multi_node.bellman('gn1')['gn3']['prev_node'] == 'gn1'


def test_bellman_update_distances(graph_multi_node, dijkstra_dictionary):
    """Test that the distance is correctly updating."""
    new_dict = graph_multi_node.dijkstra_update_distances(dijkstra_dictionary, "gn3")
    assert new_dict["gn5"]['distance'] == 17


def test_bellman_initialize_distances(graph_multi_node, dijkstra_dictionary):
    """Test that the distance is correctly initializing."""
    new_dict = graph_multi_node.dijkstra_update_distances(dijkstra_dictionary, "gn3")
    assert new_dict["gn4"]['distance'] == 11


def test_bellman_negative_cycle(graph_cyclic):
    with pytest.raises(ArithmeticError):
        graph_cyclic.bellman('gnode1')
