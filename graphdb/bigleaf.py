from graph import Graph

import json


class BigLeaf:

    def __init__(self):
        self.graph = {}

    @staticmethod
    def graph(v, e):
        """
        Factory for the creation of Graphs.
        :param v: vertices
        :param e: edges
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

    @staticmethod
    def from_string(s):
        """
        Dagoba.fromString = function(str) {                               # another graph constructor
          var obj = JSON.parse(str)                                       # this could throw
          return Dagoba.graph(obj.V, obj.E)
        """
        obj = json.loads(s)
        return BigLeaf.graph(obj.V, obj.E)

    # A gremlin is a creature that travels through the graph doing our bidding.
    @staticmethod
    def make_gremlin(vertex, state):
        """
        Dagoba.makeGremlin = function(vertex, state) {                    # gremlins are simple creatures:
          return {vertex: vertex, state: state || {} }                    # a current vertex, and some state
        }
        """
        pass

    @staticmethod
    def goto_vertex(gremlin, vertex):
        """
        Dagoba.gotoVertex = function(gremlin, vertex) {                   # clone the gremlin
          return Dagoba.makeGremlin(vertex, gremlin.state)                # THINK: add path tracking here?
        }
        """
        pass

    @staticmethod
    def filter_edges(edge, ofilter):
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
        if not ofilter:
            return True
        if type(ofilter) is str:
            return edge.get_label() == ofilter
        if type(ofilter) is list:
            return any(item == edge.get_label() for item in ofilter)

        return BigLeaf.object_filter(edge, ofilter)

    """
    Dagoba.addPipetype = function(name, fun) {                        # adds a new method to our query object
      Dagoba.Pipetypes[name] = fun
      Dagoba.Q[name] = function() {
        return this.add(name, [].slice.apply(arguments)) }            # capture the pipetype and args
    }
    """

    """
    Dagoba.getPipetype = function(name) {
      var pipetype = Dagoba.Pipetypes[name]                           # a pipe type is just a function

      if(!pipetype)
        Dagoba.error('Unrecognized pipe type: ' + name)

      return pipetype || Dagoba.fauxPipetype
    }
    """

    """
    If we can’t ﬁnd a pipetype, we generate an error and return the default pipetype,
    which acts like an empty conduit: if a message comes in one side, it gets passed out the other.
    """

    """
    Dagoba.fauxPipetype = function(graph, args, maybe_gremlin) {      # if you can't find a pipe type
      return maybe_gremlin || 'pull'                                  # just keep things flowing along
    }

    """

    @staticmethod
    def object_filter(thing, ofilter):
        """
        Dagoba.objectFilter = function(thing, filter) {      # thing has to match all of filter's properties
          for(var key in filter)
            if(thing[key] !== filter[key])
              return false

          return true
        }
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
        pass

    @staticmethod
    def persist(graph, name):
        """
        Dagoba.persist = function(graph, name) {
          name = name || 'graph'
          localStorage.setItem('DAGOBA::'+name, graph)
        }
        """

    @staticmethod
    def depersist( name):
        """
        Dagoba.depersist = function (name) {
          name = 'DAGOBA::' + (name || 'graph')
          var flatgraph = localStorage.getItem(name)
          return Dagoba.fromString(flatgraph)
        }
        """
        pass

    @staticmethod
    def error( msg):
        """
        Dagoba.error = function(msg) {
          console.log(msg)
          return false
        }
        """
        pass

