import pytest
from graph import GNode, Graph

@pytest.fixture()
def gnode1():
    """Create gnode with a value of 1."""
    gnode = GNode(1)
    return gnode


@pytest.fixture()
def gnode2():
    """Create gnode with a value of 2."""
    gnode = GNode(2)
    return gnode


@pytest.fixture()
def graph_empty():
    """Create an empty graph"""
    grph = Graph()
    return grph


@pytest.fixture()
def graph_two_node(gnode1, gnode2):
    """Create a two node graph"""
    grph = Graph()
    grph.add_node(gnode1)
    grph.add_node(gnode2)
    return grph


@pytest.fixture()
def graph_one_node(gnode1):
    """Create a two node graph"""
    grph = Graph()
    grph.add_node(gnode1)
    return grph


@pytest.fixture()
def graph_cyclic_with_nodes(graph_two_node, gnode1, gnode2):
    graph_cyclic = graph_two_node
    gn3 = GNode(3)
    graph_cyclic.add_edge(gnode1, gnode2)
    graph_cyclic.add_edge(gnode2, gn3)
    graph_cyclic.add_edge(gn3, gnode1)
    return (graph_cyclic, gnode1, gnode2, gn3)


@pytest.fixture()
def graph_v_with_nodes(graph_two_node, gnode1, gnode2):
    graph_v = graph_two_node
    gn3 = GNode(3)
    gn4 = GNode(4)
    gn5 = GNode(5)
    graph_v.add_edge(gnode1, gnode2)
    graph_v.add_edge(gnode1, gn3)
    graph_v.add_edge(gnode2, gn4)
    graph_v.add_edge(gn3, gn5)
    return (graph_v, gnode1, gnode2, gn3, gn4, gn5)


@pytest.fixture()
def graph_multi_node(graph_two_node, gnode1, gnode2):
    """Create a multi node graph"""
    from graph import Graph
    gn3 = GNode(3)
    gn4 = GNode(4)
    gn5 = GNode(5)
    graph_two_node.add_edge(gnode1, gn3)
    graph_two_node.add_edge(gn3, gnode1)
    graph_two_node.add_edge(gn3, gn4)
    graph_two_node.add_edge(gn3, gn5)
    graph_two_node.add_edge(gn4, gn5)
    return (graph_two_node, gn3, gn4, gn5)
