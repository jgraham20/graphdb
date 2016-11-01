from graphdb.graph import Graph
from graphdb.vertex import Vertex
from graphdb.graphdb import GraphDB


vertices = """
    [
        {
            "_id": 1,
            "name": "Fred"
        },
        {
            "_id": 2,
            "name": "Bob"
        },
        {
            "_id": 3,
            "name": "Tom"
        },
        {
            "_id": 4,
            "name": "Dick"
        },
        {
            "_id": 5,
            "name": "Harry"
        },
        {
            "_id": 6,
            "name": "Lucy"
        }
    ]"""

edges = """
    [
    {
        "_out": 1,
        "_in": 2,
        "_label": "son"
    },
    {
        "_out": 2,
        "_in": 3,
        "_label": "son"
    },
    {
        "_out": 2,
        "_in": 4,
        "_label": "son"
    },
    {
        "_out": 2,
        "_in": 5,
        "_label": "son"
    },
    {
        "_out": 2,
        "_in": 6,
        "_label": "daughter"
    },
    {
        "_out": 3,
        "_in": 4,
        "_label": "brother"
    },
    {
        "_out": 4,
        "_in": 5,
        "_label": "brother"
    },
    {
        "_out": 5,
        "_in": 3,
        "_label": "brother"
    },
    {
        "_out": 3,
        "_in": 5,
        "_label": "brother"
    },
    {
        "_out": 4,
        "_in": 3,
        "_label": "brother"
    },
    {
        "_out": 5,
        "_in": 4,
        "_label": "brother"
    },
    {
        "_out": 3,
        "_in": 6,
        "_label": "sister"
    },
    {
        "_out": 4,
        "_in": 6,
        "_label": "sister"
    },
    {
        "_out": 5,
        "_in": 6,
        "_label": "sister"
    },
    {
        "_out": 6,
        "_in": 3,
        "_label": "brother"
    },
    {
        "_out": 6,
        "_in": 4,
        "_label": "brother"
    },
    {
        "_out": 6,
        "_in": 5,
        "_label": "brother"
    }
]  """

def test_add_vertex():
    g = Graph()

    v1 = Vertex('N1')
    g.add_vertex(v1)
    assert v1.get_id() == 1

    v2 = Vertex('N2')
    g.add_vertex(v2)
    assert v2.get_id() == 2

    v3 = Vertex('N3')
    g.add_vertex(v3)
    assert v3.get_id() == 3

def test_add_edge():
    pass
    # g.addEdge({_out: 10, _in: 30, _label: 'parent'})
    # g.addEdge({_out: 10, _in: 'charlie', _label: 'knows'})

def test_v():
    gdb = GraphDB()

    g = graph(vertices, edges)

    q = g.v(1)

def test_build_graph():
    gdb = GraphDB()

    g = graph(vertices, edges)
    assert len(g.edges) == 17
    assert len(g.vertices) == 6


