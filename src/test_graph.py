#test node constructor

def test_node_init_value():
    from graph import GNode
    node1 = GNode(1)
    assert node1.value == 1


def test_node_init_edges():
    from graph import GNode
    node1 = GNode(1)
    assert node1.edges == []

def test_graph_init_list_of_nodes():
    from graph import Graph
    test_graph = Graph()
    assert test_graph.list_of_nodes == []

def test_graph_add_node():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node = GNode(1)
    test_graph.add_node(test_node)
    assert test_node in test_graph.list_of_nodes

def test_graph_has_node_true():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node = GNode(1)
    test_graph.add_node(test_node)
    assert test_graph.has_node(test_node) is True

def test_graph_has_node_false():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node = GNode(1)
    assert test_graph.has_node(test_node) is False

def test_graph_add_edge_both_nodes_in_graph():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_node(test_node1)
    test_graph.add_node(test_node2)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node2 in test_node1.edges

def test_graph_add_edge_both_nodes_in_graph_check_edge_direction():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_node(test_node1)
    test_graph.add_node(test_node2)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node1 not in test_node2.edges

def test_graph_add_edge_one_node_in_graph_check_edge():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_node(test_node1)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node1.edges == [test_node2]

def test_graph_add_edge_one_node_in_graph_check_node():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_node(test_node1)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node2 in test_graph.list_of_nodes

def test_graph_add_edge_neither_node_in_graph_check_edge():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node1.edges == [test_node2]

def test_graph_add_edge_neither_node_in_graph_check_node1():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node1 in test_graph.list_of_nodes

def test_graph_add_edge_neither_node_in_graph_check_node2():
    from graph import GNode
    from graph import Graph
    test_graph = Graph()
    test_node1 = GNode(1)
    test_node2 = GNode(2)
    test_graph.add_edge(test_node1, test_node2)
    assert test_node2 in test_graph.list_of_nodes
