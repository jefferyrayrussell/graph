"""Fixtures for graph data structure testing."""

import pytest
from graph import Graph


@pytest.fixture()
def graph_empty():
    """Create an empty graph."""
    g = Graph()
    return g


@pytest.fixture()
def graph_two_node():
    """Create a two node graph."""
    grph = Graph()
    grph.add_node('gnode1')
    grph.add_node('gnode2')
    return grph


@pytest.fixture()
def graph_one_node():
    """Create a two node graph."""
    grph = Graph()
    grph.add_node('gnode1')
    return grph


@pytest.fixture()
def graph_cyclic(graph_two_node):
    """Create a cyclic two node graph."""
    graph_cyclic = graph_two_node
    graph_cyclic.add_edge('gnode1', 'gnode2', 1)
    graph_cyclic.add_edge('gnode2', 'gnode3', -5)
    graph_cyclic.add_edge('gnode3', 'gnode1', 2)
    return (graph_cyclic)


@pytest.fixture()
def graph_v():
    """Create a v graph."""
    graph_v = Graph()
    graph_v.add_edge('gnode1', 'gnode2', 0)
    graph_v.add_edge('gnode1', 'gnode3', 0)
    graph_v.add_edge('gnode2', 'gnode4', 0)
    graph_v.add_edge('gnode3', 'gnode5', 0)
    return (graph_v)


@pytest.fixture()
def graph_multi_node(graph_empty):
    """Create a multi node graph."""
    graph_empty.add_node('gn2')
    graph_empty.add_edge('gn1', 'gn3', 7)
    graph_empty.add_edge('gn1', 'gn5', 20)
    graph_empty.add_edge('gn3', 'gn1', 7)
    graph_empty.add_edge('gn3', 'gn4', 4)
    graph_empty.add_edge('gn3', 'gn5', 10)
    graph_empty.add_edge('gn4', 'gn5', 2)
    return (graph_empty)


@pytest.fixture()
def dijkstra_dictionary():
    """Create a dictionary for Dijkstra Algorithm testing."""
    my_dict = {
        'gn1': {'distance': 0, 'visited': True},
        'gn3': {'distance': 7, 'visited': False},
        'gn4': {'visited': False},
        'gn5': {'distance': 20, 'visited': False}
    }
    return my_dict


@pytest.fixture()
def dijkstra_dictionary_final():
    """Create final dictionary for Dijkstra Algorithm testing."""
    my_dict = {
        'gn1': {'distance': 0, 'visited': True},
        'gn2': {'visited': False},
        'gn3': {'distance': 7, 'visited': True, 'previous_node': 'gn1'},
        'gn4': {'distance': 11, 'visited': True, 'previous_node': 'gn3'},
        'gn5': {'distance': 13, 'visited': False, 'previous_node': 'gn4'}
    }
    return my_dict
