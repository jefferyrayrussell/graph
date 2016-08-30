import pytest

#test node constructor

def test_node_init_value(gnode1):
    assert gnode1.value == 1


def test_node_init_edges(gnode1):
    assert gnode1.edges == set()

def test_graph_init_set_of_nodes(graph_empty):
    assert graph_empty.set_of_nodes == set()

def test_graph_is_node_true(graph_empty, gnode1):
    assert graph_empty.is_node(gnode1)

def test_graph_is_node_error(graph_empty):
    with pytest.raises(TypeError):
        graph_empty.is_node('not_a_node')

def test_graph_add_node(graph_empty, gnode1):
    graph_empty.add_node(gnode1)
    assert gnode1 in graph_empty.set_of_nodes

def test_graph_has_node_true(graph_empty, gnode1):
    graph_empty.add_node(gnode1)
    assert graph_empty.has_node(gnode1) is True

def test_graph_has_node_false(graph_empty, gnode1):
    assert graph_empty.has_node(gnode1) is False

def test_graph_add_edge_both_nodes_in_graph(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert gnode2 in gnode1.edges

def test_graph_add_edge_both_nodes_in_graph_check_edge_direction(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert gnode1 not in gnode2.edges

def test_graph_add_edge_one_node_in_graph_check_edge(graph_one_node, gnode1, gnode2):
    graph_one_node.add_edge(gnode1, gnode2)
    assert gnode2 in gnode1.edges

def test_graph_add_edge_one_node_in_graph_check_node(graph_one_node, gnode1, gnode2):
    graph_one_node.add_edge(gnode1, gnode2)
    assert gnode2 in graph_one_node.set_of_nodes

def test_graph_add_edge_neither_node_in_graph_check_edge(graph_empty, gnode1, gnode2):
    graph_empty.add_edge(gnode1, gnode2)
    assert gnode2 in gnode1.edges

def test_graph_add_edge_neither_node_in_graph_check_node1(graph_empty, gnode1, gnode2):
    graph_empty.add_edge(gnode1, gnode2)
    assert gnode1 in graph_empty.set_of_nodes

def test_graph_add_edge_neither_node_in_graph_check_node2(graph_empty, gnode1, gnode2):
    graph_empty.add_edge(gnode1, gnode2)
    assert gnode2 in graph_empty.set_of_nodes


def test_graph_del_edge_exists(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    graph_two_node.del_edge(gnode1, gnode2)
    assert gnode2 not in gnode1.edges


def test_graph_del_edge_no_exists(graph_two_node, gnode1, gnode2):
    with pytest.raises(KeyError):
        graph_two_node.del_edge(gnode1, gnode2)


def test_graph_del_edge_not_a_node(graph_two_node, gnode1, gnode2):
    with pytest.raises(TypeError):
        graph_two_node.del_edge('gnode1', gnode2)


def test_graph_del_node_exists_check_graph_for_node(graph_one_node, gnode1):
    graph_one_node.del_node(gnode1)
    assert gnode1 not in graph_one_node.set_of_nodes


def test_graph_del_node_no_exists(graph_one_node, gnode1, gnode2):
    with pytest.raises(KeyError):
        graph_one_node.del_node(gnode2)


def test_graph_del_node_check_edges(graph_empty, gnode1, gnode2):
    graph_empty.add_edge(gnode1, gnode2)
    graph_empty.del_node(gnode2)
    assert gnode2 not in gnode1.edges

def test_graph_del_node_not_a_node(graph_empty, gnode1, gnode2):
    graph_empty.add_edge(gnode1, gnode2)
    with pytest.raises(KeyError):
        graph_empty.del_node('gnode2')

def test_graph_del_node_other_nodes_not_changed(graph_two_node, gnode1, gnode2):
    from graph import GNode
    gnode3 = GNode(3)
    graph_two_node.add_edge(gnode1, gnode2)
    graph_two_node.add_edge(gnode3, gnode1)
    graph_two_node.del_node(gnode2)
    assert gnode1 in gnode3.edges


def test_adjacent_true(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert graph_two_node.adjacent(gnode1, gnode2)


def test_adjacent_false(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert graph_two_node.adjacent(gnode2, gnode1) is False


def test_adjacent_error_not_in_graph(graph_one_node, gnode1, gnode2):
    with pytest.raises(KeyError):
        graph_one_node.adjacent(gnode1, gnode2)


def test_adjacent_error_not_a_node(graph_one_node, gnode1, gnode2):
    with pytest.raises(TypeError):
        graph_one_node.adjacent(gnode1, 'not a node')


def test_neighbors_has_edges(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert graph_two_node.neighbors(gnode1) == [gnode2]



def test_neighbors_no_edges(graph_two_node, gnode1, gnode2):
    assert graph_two_node.neighbors(gnode1) == []


def test_neighbors_not_in_graph(graph_one_node, gnode1, gnode2):
    with pytest.raises(KeyError):
        graph_one_node.neighbors(gnode2)


def test_nodes_connected(graph_multi_node, gnode1):
    grph = graph_multi_node[0]
    assert gnode1 in grph.nodes()


def test_nodes_unconnected(graph_multi_node, gnode2):
    grph = graph_multi_node[0]
    assert gnode2 in grph.nodes()


def test_edges_connected(graph_multi_node):
    from graph import Edge
    my_edge = Edge(graph_multi_node[1], graph_multi_node[2])
    assert my_edge in graph_multi_node[0].edges()


def test_edges_not_connected(graph_multi_node):
    from graph import Edge
    my_edge = Edge(graph_multi_node[2], graph_multi_node[1])
    assert my_edge not in graph_multi_node[0].edges()


def test_breadth_transversal_one_node(graph_one_node, gnode1):
    assert graph_one_node.breadth_first_traversal(gnode1) == [gnode1]


def test_depth_transversal_one_node(graph_one_node, gnode1):
    assert graph_one_node.depth_first_traversal(gnode1) == [gnode1]


def test_breadth_transversal_two_node(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert gnode2 in graph_two_node.breadth_first_traversal(gnode1)


def test_depth_transversal_two_node(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode1, gnode2)
    assert gnode2 in graph_two_node.depth_first_traversal(gnode1)



def test_breadth_transversal_two_node_not_in_traversal(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode2, gnode1)
    assert gnode2 not in graph_two_node.breadth_first_traversal(gnode1)


def test_depth_transversal_two_node_not_in_traversal(graph_two_node, gnode1, gnode2):
    graph_two_node.add_edge(gnode2, gnode1)
    assert gnode2 not in graph_two_node.depth_first_traversal(gnode1)


def test_breadth_transversal_cyclic(graph_cyclic_with_nodes):
    graph_cylic = graph_cyclic_with_nodes[0]
    gnode1 = graph_cyclic_with_nodes[1]
    gnode3 = graph_cyclic_with_nodes[3]
    assert gnode3 in graph_cylic.breadth_first_traversal(gnode1)


def test_depth_transversal_cyclic(graph_cyclic_with_nodes):
    """Test cyclic graph with transversal"""
    graph_cylic = graph_cyclic_with_nodes[0]
    gnode1 = graph_cyclic_with_nodes[1]
    gnode3 = graph_cyclic_with_nodes[3]
    assert gnode3 in graph_cylic.depth_first_traversal(gnode1)


def test_order_breadth_transversal(graph_v_with_nodes):
    """Graph: 4->2->1<-3<-5 Check to see if children append before the children's children."""
    graph_v = graph_v_with_nodes[0]
    node1 = graph_v_with_nodes[1]
    node2 = graph_v_with_nodes[2]
    node5 = graph_v_with_nodes[5]
    transversal = graph_v.breadth_first_traversal(node1)
    assert transversal.index(node2) < transversal.index(node5)


def test_order_depth_transversal(graph_v_with_nodes):
    """Graph: 4->2->1<-3<-5 Check to see if it goes to the bottom before other children."""
    graph_v = graph_v_with_nodes[0]
    node1 = graph_v_with_nodes[1]
    node2 = graph_v_with_nodes[2]
    node3 = graph_v_with_nodes[3]
    node4 = graph_v_with_nodes[4]
    node5 = graph_v_with_nodes[5]
    transversal = graph_v.depth_first_traversal(node1)
    if transversal.index(node2) < transversal.index(node3): 
        assert transversal.index(node4) < transversal.index(node3)
    else:
        assert transversal.index(node5) < transversal.index(node2)
