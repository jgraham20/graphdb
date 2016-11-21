from graph import Graph
import json


class GraphDB:

    def __init__(self, instance_name='Default'):
        self.instance_name = instance_name

    @staticmethod
    def from_string(s):
        """
        Load JSON into new graph
        :param s:
        :return:
        """
        obj = json.loads(s)
        return GraphDB.graph(e=obj.E)

    @staticmethod
    def graph(v, e):
        """
        Factory for the creation of Graphs.
        :param v: vertices
        :param e: edges
        :return: Graph
        """
        mygraph = Graph()  # Setup of Graph is in __init__

        if isinstance(v, str):
            vertices = json.loads(v)
        elif isinstance(v, list):
            vertices = v
        else:
            raise Exception("Error loading Vertices")

        mygraph.add_vertices(vertices)

        if isinstance(e, str):
            edges = json.loads(e)
        elif isinstance(e, list):
            edges = e
        else:
            raise Exception("Error loading Edges")

        mygraph.add_edges(edges)

        return mygraph


