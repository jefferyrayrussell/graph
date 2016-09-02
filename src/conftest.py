import pytest
from graph import Graph


@pytest.fixture()
def graph_empty():
    """Create an empty graph"""
    g = Graph()
    return g


@pytest.fixture()
def graph_two_node():
    """Create a two node graph"""
    grph = Graph()
    grph.add_node('gnode1')
    grph.add_node('gnode2')
    return grph


@pytest.fixture()
def graph_one_node():
    """Create a two node graph"""
    grph = Graph()
    grph.add_node('gnode1')
    return grph


@pytest.fixture()
def graph_cyclic(graph_two_node):
    graph_cyclic = graph_two_node
    graph_cyclic.add_edge('gnode1', 'gnode2', 0)
    graph_cyclic.add_edge('gnode2', 'gnode3', 0)
    graph_cyclic.add_edge('gnode3', 'gnode1', 0)
    return (graph_cyclic)


@pytest.fixture()
def graph_v():
    graph_v = Graph()
    graph_v.add_edge('gnode1', 'gnode2', 0)
    graph_v.add_edge('gnode1', 'gnode3', 0)
    graph_v.add_edge('gnode2', 'gnode4', 0)
    graph_v.add_edge('gnode3', 'gnode5', 0)
    return (graph_v)


@pytest.fixture()
def graph_multi_node(graph_empty):
    """Create a multi node graph"""
    graph_empty.add_node('gn2')
    graph_empty.add_edge('gn1', 'gn3', 7)
    graph_empty.add_edge('gn3', 'gn1', 7)
    graph_empty.add_edge('gn3', 'gn4', 4)
    graph_empty.add_edge('gn3', 'gn5', 10)
    graph_empty.add_edge('gn4', 'gn5', 2)
    return (graph_empty)
