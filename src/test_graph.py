import pytest

# Test node constructor.


def test_graph_init_set_of_nodes(graph_empty):
    assert graph_empty.set_of_nodes == set()


def test_graph_add_node(graph_empty):
    graph_empty.add_node('gnode1')
    assert 'gnode1' in graph_empty.set_of_nodes


def test_graph_has_node_true(graph_empty):
    graph_empty.add_node('gnode1')
    assert graph_empty.has_node('gnode1') is True


def test_graph_node_non_hashable(graph_empty):
    with pytest.raises(TypeError):
        graph_empty.add_node(['list'])


def test_graph_has_node_false(graph_empty):
    assert graph_empty.has_node('gnode1') is False


def test_graph_add_edge_both_nodes_in_graph(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_two_node.gnodes['gnode1']


def test_graph_add_edge_both_nodes_in_graph_check_edge_direction(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode1' not in graph_two_node.gnodes['gnode2']


def test_graph_add_edge_one_node_in_graph_check_edge(graph_one_node):
    graph_one_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_one_node.gnodes['gnode1']


def test_graph_add_edge_one_node_in_graph_check_node(graph_one_node):
    graph_one_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_one_node.gnodes['gnode1']


def test_graph_add_edge_neither_node_in_graph_check_edge(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_empty.gnodes['gnode1']


def test_graph_add_edge_neither_node_in_graph_check_node1(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode1' in graph_empty.gnodes


def test_graph_add_edge_neither_node_in_graph_check_node2(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_empty.gnodes


def test_graph_del_edge_exists(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    graph_two_node.del_edge('gnode1', 'gnode2')
    assert 'gnode2' not in graph_two_node.gnodes['gnode1']


def test_graph_del_edge_no_exists(graph_two_node):
    with pytest.raises(KeyError):
        graph_two_node.del_edge('gnode1', 'gnode2')


def test_graph_del_node_exists_check_graph_for_node(graph_one_node):
    graph_one_node.del_node('gnode1')
    assert 'gnode1' not in graph_one_node.gnodes


def test_graph_del_node_exists_check_set_membership(graph_one_node):
    graph_one_node.del_node('gnode1')
    assert 'gnode1' not in graph_one_node.set_of_nodes


def test_graph_del_node_no_exists(graph_one_node):
    with pytest.raises(KeyError):
        graph_one_node.del_node('gnode2')


def test_graph_del_node_check_edges(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    graph_empty.del_node('gnode2')
    assert 'gnode2' not in graph_empty.gnodes['gnode1']


def test_graph_del_node_not_a_node(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 0)
    with pytest.raises(KeyError):
        graph_empty.del_node('gnode3')


def test_graph_del_node_other_nodes_not_changed(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    graph_two_node.add_edge('gnode3', 'gnode1', 0)
    graph_two_node.del_node('gnode2')
    assert 'gnode1' in graph_two_node.gnodes['gnode3']


def test_adjacent_true(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert graph_two_node.adjacent('gnode1', 'gnode2')


def test_adjacent_false(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert graph_two_node.adjacent('gnode2', 'gnode1') is False


def test_adjacent_error_not_in_graph(graph_one_node):
    with pytest.raises(TypeError):
        graph_one_node.adjacent('gnode1', 'gnode2')


def test_neighbors_has_edges(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert graph_two_node.neighbors('gnode1') == ['gnode2']


def test_neighbors_no_edges(graph_two_node):
    assert graph_two_node.neighbors('gnode1') == []


def test_neighbors_not_in_graph(graph_one_node):
    with pytest.raises(KeyError):
        graph_one_node.neighbors('gnode2')


def test_nodes_connected(graph_multi_node):
    assert 'gn1' in graph_multi_node.gnodes


def test_nodes_connected_test_set_membership(graph_multi_node):
    assert 'gn1' in graph_multi_node.set_of_nodes


def test_nodes_unconnected(graph_multi_node):
    assert 'gn2' in graph_multi_node.gnodes


def test_nodes_unconnected_test_set_membership(graph_multi_node):
    assert 'gn2' in graph_multi_node.set_of_nodes


def test_nodes_list(graph_v):
    assert sorted(graph_v.nodes()) == ['gnode1', 'gnode2', 'gnode3', 'gnode4', 'gnode5']


def test_edge_list(graph_cyclic):
    assert sorted(graph_cyclic.edges()) == ['gnode1->gnode2', 'gnode2->gnode3', 'gnode3->gnode1']


def test_breadth_transversal_one_node(graph_one_node):
    assert graph_one_node.breadth_first_traversal('gnode1') == ['gnode1']


def test_depth_transversal_one_node(graph_one_node):
    assert graph_one_node.depth_first_traversal('gnode1') == ['gnode1']


def test_breadth_transversal_two_node(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_two_node.breadth_first_traversal('gnode1')


def test_depth_transversal_two_node(graph_two_node):
    graph_two_node.add_edge('gnode1', 'gnode2', 0)
    assert 'gnode2' in graph_two_node.depth_first_traversal('gnode1')


def test_breadth_transversal_two_node_not_in_traversal(graph_two_node):
    graph_two_node.add_edge('gnode2', 'gnode1', 0)
    assert 'gnode2' not in graph_two_node.breadth_first_traversal('gnode1')


def test_depth_transversal_two_node_not_in_traversal(graph_two_node):
    graph_two_node.add_edge('gnode2', 'gnode1', 0)
    assert 'gnode2' not in graph_two_node.depth_first_traversal('gnode1')


def test_breadth_transversal_cyclic(graph_cyclic):
    """Test cyclic graph with transversal"""
    assert 'gnode3' in graph_cyclic.breadth_first_traversal('gnode1')


def test_depth_transversal_cyclic(graph_cyclic):
    """Test cyclic graph with transversal"""
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
    graph_empty.add_edge('gnode1', 'gnode2', 5)
    assert graph_empty.gnodes['gnode1']['gnode2'] == 5


def test_graph_weight_test_neg_amount(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', -5)
    assert graph_empty.gnodes['gnode1']['gnode2'] == -5


def test_graph_weight_not_set_is_key_error(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 5)
    with pytest.raises(KeyError):
        graph_empty.gnodes['gnode2']['gnode1'] == 5


def test_graph_weight_reassign_weight(graph_empty):
    graph_empty.add_edge('gnode1', 'gnode2', 2)
    graph_empty.add_edge('gnode1', 'gnode2', 7)
    assert graph_empty.gnodes['gnode1']['gnode2'] == 7


def test_dijkstra_dictionary_has_all_nodes(graph_multi_node):
    """Test that all nodes are present in the dictionary."""
    for key in graph_multi_node.gnodes:
        assert key in graph_multi_node.dijkstra_init()


# def test_dijkstra_init_nodes_have_distance(graph_multi_node):
#     """Test that each node has the attribute distance."""
#     for key in graph_multi_node.dijkstra_init():
#         assert graph_multi_node.dijkstra_init()[key]["distance"] is None


def test_dijkstra_init_nodes_visited(graph_multi_node):
    """Test that each node visitied is false."""
    for key in graph_multi_node.dijkstra_init():
        assert graph_multi_node.dijkstra_init()[key]["visited"] is False


def test_dijkstra_startnode_zero_distance_value(graph_multi_node):
    """Test that start node has a beginning distance of zero."""
    assert graph_multi_node.dijkstra('gn1', 'gn3')['gn1']['distance'] == 0


def test_dijkstra_nextnode_distance_value(graph_multi_node):
    """Test that the next node has a has a distance."""
    assert graph_multi_node.dijkstra('gn1', 'gn3')['gn3']['distance'] == 7


def test_dijkstra_nextnode_previous_value(graph_multi_node):
    """Test that the previous node value gets set."""
    assert graph_multi_node.dijkstra('gn1', 'gn3')['gn3']['previous_node'] == 'gn1'

def test_dijkstra_startnode_visited(graph_multi_node):
    """Test that start node has been visited."""
    assert graph_multi_node.dijkstra('gn1', 'gn3')['gn1']['visited'] is True

def test_dijkstra_shortest_distance(graph_empty, dijkstra_dictionary):
    """Test that the edge with the shortest distance is selected."""
    assert graph_empty.dijkstra_select_node(dijkstra_dictionary) == "a"







