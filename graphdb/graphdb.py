from graph import Graph
from transformer import Transformer
import json


class GraphDB:

    def __init__(self):
        self._graph = {}
        self._pipetypes = {}
        self._Q = {}
        self._T = Transformer()

    @staticmethod
    def from_string(s):
        """
        Load JSON into new graph
        :param s:
        :return:
        """
        obj = json.loads(s)
        return GraphDB.graph(v=obj.V, e=obj.E)

    @staticmethod
    def make_gremlin(vertex, state):
        """
        A gremlin is a creature that travels through the graph doing our bidding.
        :param vertex:
        :param state:
        :return:
        """
        return {vertex: vertex, state: state or {}}

    @staticmethod
    def goto_vertex(gremlin, vertex):
        """

        :param gremlin:
        :param vertex:
        :return:
        """
        return GraphDB.make_gremlin(vertex, gremlin.state)

    @staticmethod
    def filter_edges(edge, ofilter):
        """

        :param edge:
        :param ofilter:
        :return:
        """
        if not ofilter:
            return True
        if type(ofilter) is str:
            return edge.get_label() == ofilter
        if type(ofilter) is list:
            return any(item == edge.get_label() for item in ofilter)

        return GraphDB.object_filter(edge, ofilter)

    def add_pipe_type(self, name, func, *args):
        """
        Add a pipe to the query.
        :param name:
        :param func:
        :param args:
        :return:
        """
        self._pipetypes[name] = func
        self._Q[name].add(name, args)  # add the pipetype and args to the query.

    def get_pipe_type(self, name):
        """
        Get the pipetype
        :param name:
        :return:
        """
        pipetype = self._pipetypes[name]

        if not pipetype:
            raise "Unknown PipeType: " + name

        return pipetype or GraphDB.faux_pipe

    @staticmethod
    def faux_pipe(graph, args, maybe_gremlin):                 # if you can't find a pipe type
        """
        Create a new faux pipe
        :param graph:
        :param args:
        :param maybe_gremlin:
        :return:
        """
        return maybe_gremlin or 'pull'                                  # just keep things flowing along

    @staticmethod
    def object_filter(thing, ofilter):
        """

        :param thing:
        :param ofilter:
        :return:
        """
        return all(thing[key] == ofilter[key] for key in ofilter)

    @staticmethod
    def clean_vertex(key, value):
        """
        Dagoba.cleanVertex = function(key, value) {                       # for JSON.stringify
          return (key == '_in' || key == '_out') ? undefined : value
        }
        """
        pass

    @staticmethod
    def clean_edge(key, value):
        """
        Dagoba.cleanEdge = function(key, value) {
          return (key == '_in' || key == '_out') ? value._id : value
        }
        """
        pass

    @staticmethod
    def jsonify(graph):
        """
        Dagoba.jsonify = function(graph) {                                # kids, don't hand code JSON
          return '{"V":' + JSON.stringify(graph.vertices, Dagoba.cleanVertex)
               + ',"E":' + JSON.stringify(graph.edges,    Dagoba.cleanEdge)
               + '}'
        }
        """
        # Todo: This should only write valid parts.
        return '{"V":' + json.dumps(graph.vertices) + ',"E":' + json.dumps(graph.edges) + '}'

    @staticmethod
    def persist(graph, name):
        pass  # Todo

    @staticmethod
    def depersist( name):
        pass  # Todo

    @staticmethod
    def error(msg):
        """
        Todo: add logging.
        :param msg:
        :return:
        """
        pass

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

    def transform(self, program):
        return self._T.transform(program)
