from graph import Graph
from query import Query
import json


class GraphDB:

    def __init__(self):
        self.graph = {}

    @staticmethod
    def graph(v, e):
        """
        Factory for the creation of Graphs.
        :param vertices: vertices
        :param edges: edges
        :return: Graph
        """
        graph = Graph()  # Setup of Graph is in __init__

        if isinstance(v, str):
            vertices = json.loads(v)
        elif isinstance(v, list):
            vertices = v
        else:
            raise Exception("Error loading Vertices")

        graph.add_vertices(vertices)

        if isinstance(e, str):
            edges = json.loads(e)
        elif isinstance(e, list):
            edges = e
        else:
            raise Exception("Error loading Edges")

        graph.add_edges(edges)

        return graph

"""
The V method. Builds a new query, then uses our helper to populate the initial query program.
This makes use of the pipetype, which we’ll look at soon.
Note that is JS parlance for “please pass me an array of this function’s arguments”.
You would be forgiven for supposing that is already an array, since it behaves like one in many situations,
but it is lacking much of the functionality we utilize in modern JavaScript arrays.
"""
    def v(self, arguments):
        """
         Dagoba.G.v = function() {                                         # a query initializer: g.v() -> query
           var query = Dagoba.query(this)
           query.add('vertex', [].slice.call(arguments))                   # add vertex as first query pipe
           return query
         }
        """
        q = Query(g)
        q.add(arguments)
        return q

    @staticmethod
    def from_string(s):
        """
        Dagoba.fromString = function(str) {                               # another graph constructor
          var obj = JSON.parse(str)                                       # this could throw
          return Dagoba.graph(obj.V, obj.E)
        """
        pass

    # A gremlin is a creature that travels through the graph doing our bidding.
    def make_gremlin(self, vertex, state):
        """
        Dagoba.makeGremlin = function(vertex, state) {                    # gremlins are simple creatures:
          return {vertex: vertex, state: state || {} }                    # a current vertex, and some state
        }
        """
        pass

    def goto_vertex(self, gremlin, vertex):
        """
        Dagoba.gotoVertex = function(gremlin, vertex) {                   # clone the gremlin
          return Dagoba.makeGremlin(vertex, gremlin.state)                # THINK: add path tracking here?
        }
        """
        pass

    def filter_edges(self, filter):
        """
        Dagoba.filterEdges = function(filter) {
          return function(edge) {
            if(!filter)                            # if there's no filter, everything is valid
              return true

            if(typeof filter == 'string')          # if the filter is a string, the label must match
              return edge._label == filter

            if(Array.isArray(filter))                  # if the filter is an array, the label must be in it
              return !!~filter.indexOf(edge._label)

            return Dagoba.objectFilter(edge, filter)    # try the filter as an object
          }
        }
        """
        pass

    def object_filter(self, filter):
        """
        Dagoba.objectFilter = function(thing, filter) {      # thing has to match all of filter's properties
          for(var key in filter)
            if(thing[key] !== filter[key])
              return false

          return true
        }
        """
        pass

    def clean_vertex(self, key, value):
        """
        Dagoba.cleanVertex = function(key, value) {                       # for JSON.stringify
          return (key == '_in' || key == '_out') ? undefined : value
        }
        """
        pass

    def clean_edge(self, key, value):
        """
        Dagoba.cleanEdge = function(key, value) {
          return (key == '_in' || key == '_out') ? value._id : value
        }
        """
        pass

    def jsonify(self, graph):
        """
        Dagoba.jsonify = function(graph) {                                # kids, don't hand code JSON
          return '{"V":' + JSON.stringify(graph.vertices, Dagoba.cleanVertex)
               + ',"E":' + JSON.stringify(graph.edges,    Dagoba.cleanEdge)
               + '}'
        }
        """
        pass

    def persist(self, graph, name):
        """
        Dagoba.persist = function(graph, name) {
          name = name || 'graph'
          localStorage.setItem('DAGOBA::'+name, graph)
        }
        """

    def depersist(self, name):
        """
        Dagoba.depersist = function (name) {
          name = 'DAGOBA::' + (name || 'graph')
          var flatgraph = localStorage.getItem(name)
          return Dagoba.fromString(flatgraph)
        }
        """
        pass

    def error(self, msg):
        """
        Dagoba.error = function(msg) {
          console.log(msg)
          return false
        }
        """
        pass

