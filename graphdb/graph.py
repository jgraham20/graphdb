from graphdb.edge import Edge
from graphdb.vertex import Vertex
from graphdb.query import Query
from transformer import Transformer
from graphdb.pipetypes import PipeTypes
import json
from functools import partial


class Graph(object):

    def __init__(self):

        self.edges = []
        self.vertices = []
        self.vertexIndex = {}
        self.autoid = 1
        self._pipetypes = {}
        self._Q = {}
        self._T = Transformer()
        self.query = Query(self)
        self.pipetypes = PipeTypes(self)
        self.add_pipe_type('_in', partial(self.pipetypes.traversal_in_pipe))
        self.add_pipe_type('_out', partial(self.pipetypes.traversal_in_pipe))

        print(repr(self.query))

    def add_vertex(self, vertex):
        """
         Add a vertex to the graph
        """
        vid = vertex.vertex_id

        if not vid:
            vertex.vertex_id = self.autoid
            self.autoid += 1
        elif self.find_vertex_by_id(vid):
            raise Exception('The vertex id is already in use: ' + str(self.autoid))

        self.vertices.append(vertex)
        self.vertexIndex[vertex.vertex_id] = vertex

        return vertex.vertex_id

    def add_edge(self, edge):
        """
        # Add edge
        :param edge:
        :return:
        """
        edge_in = self.find_vertex_by_id(edge.get_in())
        edge_out = self.find_vertex_by_id(edge.get_out())

        if not (edge_in and edge_out):
            raise Exception("That edge's vertex wasn't found")

        edge_out.add_out(edge)  # add edge to the edge's out vertex's out edges
        edge_in.add_in(edge)  # vice versa
        self.edges.append(edge)

    def add_vertices(self, vertices):
        """
        Add vertices from list
        :param vertices:
        :return:
        """
        for v in vertices:
            self.add_vertex(Vertex(vertex_id=v['_id'], vertex_name=v['name']))

    def add_edges(self, edges):
        """
        Add edges in List
        """
        for e in edges:
            self.add_edge(Edge(label=e['_label'], _in=e['_in'], _out=e['_out']))

    def v(self, *args):
        #q = Query(self)
        #q.add('vertex', args)
        #return q
        self.query.add('vertex', args)
        return self.query

    def find_vertices(self, vertices=None, *args):
        # Fixme
        if not vertices:
            return list(self.vertices)

    def find_vertices_by_ids(self, ids):
        if len(ids) == 1:
            maybe_vertex = self.find_vertex_by_id(ids[0])
            if maybe_vertex:
                return maybe_vertex
            else:
                return []
        # Todo: add Else condition to handle array of ids

    def find_vertex_by_id(self, vid):
        """
        Return the vertex desigated by the id.
        :param vid:
        :return:
        """
        if vid in self.vertexIndex:
            return self.vertexIndex[vid]
        else:
            return None

    def search_vertices(self, vertex, vfilter):
        # Fixme
        #d = {k: v for k, v in self.vertices.items() if v > 0}
        pass

    def find_out_edges(self, vertex):
        """
        Get all out edges for the vertex
        :param vertex:
        :return:
        """
        return vertex.v_out

    def find_in_edges(self, vertex):
        """
        Get all IN edges for the vertex
        :return:
        """
        return vertex.v_in

    def __repr__(self):
        return "WIP"  # Fixme

    def jsonify(self):
        """
        Return a JSON representation of the Graph.
        :return:
        """
        pass  # Fixme

    @staticmethod
    def make_gremlin(vertex, state):
        """
        A gremlin is a creature that travels through the graph doing our bidding.
        :param vertex:
        :param state:
        :return:
        """
        return {vertex: vertex, state: state or {}}

    def goto_vertex(self, gremlin, vertex):
        """

        :param gremlin:
        :param vertex:
        :return:
        """
        return self.make_gremlin(vertex, gremlin.state)

    def filter_edges(self, edge, ofilter):
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

        return self.object_filter(edge, ofilter)

    """
    functools.partial(func, *args, **keywords)
    Return a new partial object which when called will
    behave like func called with the positional arguments
    args and keyword arguments keywords. If more arguments
    are supplied to the call, they are appended to args.
    If additional keyword arguments are supplied,
    they extend and override keywords.
    """
    def add_pipe_type(self, name, func, *args):
        """
        Add a pipe to the query.
        :param name:
        :param func:
        :param args:
        :return:
        """

        self._pipetypes[name] = func  # This is the definitions of the different pipetypes
        self.query.add(name, func(args))  # This is the Instances of the pipetype with the args
        #self._Q[name] = func   # add the pipetype and args to the query.

    def get_pipe_type(self, name):
        """
        Get the pipetype
        :param name:
        :return:
        """
        pipetype = self.pipetypes[name]

        if not pipetype:
            raise "Unknown PipeType: " + name

        return pipetype or self.faux_pipe

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

    @classmethod
    def clean_vertex(cls, key, value):
        pass

    @classmethod
    def clean_edge(cls, key, value):
        pass

    @classmethod
    def jsonify(cls, graph):
        # Todo: This should only write valid parts.
        return '{"V":' + json.dumps(graph.vertices) + ',"E":' + json.dumps(graph.edges) + '}'

    @classmethod
    def persist(cls, graph, name):
        pass  # Todo

    @classmethod
    def depersist(cls, name):
        pass  # Todo

    @classmethod
    def error(cls, msg):
        """
        Todo: add logging.
        :param msg:
        :return:
        """
        pass

    def transform(self, program):
        return self._T.transform(program)