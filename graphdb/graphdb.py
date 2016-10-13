
class GraphDB:

    class Query:

        def __init__(self):
            pass

        def add(self, args):
            pass

    def __init__(self):
        self.graph = {}

    def graph(self, V, E):
        graph = Graph()  # Setup of Graph is in __init__

        if isinstance(V, []):
            graph.addVertices(V)

        if isinstance(E, []):
            graph.addEdges(E)

        return graph

    def query(self, arguments):
        """
         Dagoba.G.v = function() {                                         # a query initializer: g.v() -> query
           var query = Dagoba.query(this)
           query.add('vertex', [].slice.call(arguments))                   # add vertex as first query pipe
           return query
         }
        """
        q = self.Query()
        q.add(arguments)
        return q

    def add_vertex(self):
        """
         Dagoba.G.addVertex = function(vertex) {                           # accepts a vertex-like object, with properties
           if(!vertex._id)
             vertex._id = this.autoid++
           else if(this.findVertexById(vertex._id))
             return Dagoba.error('A vertex with id ' + vertex._id + ' already exists')

           this.vertices.push(vertex)
           this.vertexIndex[vertex._id] = vertex
           vertex._out = []; vertex._in = []                               # placeholders for edge pointers
            return vertex._id
         }
        """
        pass

    def add_edge(self):
        """
         Dagoba.G.addEdge = function(edge) {                               # accepts an edge-like object, with properties
           edge._in  = this.findVertexById(edge._in)
           edge._out = this.findVertexById(edge._out)

          if(!(edge._in && edge._out))
             return Dagoba.error("That edge's " + (edge._in ? 'out' : 'in') + " vertex wasn't found")

           edge._out._out.push(edge)                                       # add edge to the edge's out vertex's out edges
           edge._in._in.push(edge)                                         # vice versa
           this.edges.push(edge)
         }
        """
        pass


#
# # HELPER FUNCTIONS
#
# Dagoba.makeGremlin = function(vertex, state) {                    # gremlins are simple creatures:
#   return {vertex: vertex, state: state || {} }                    # a current vertex, and some state
# }
#
# Dagoba.gotoVertex = function(gremlin, vertex) {                   # clone the gremlin
#   return Dagoba.makeGremlin(vertex, gremlin.state)                # THINK: add path tracking here?
# }
#
# Dagoba.filterEdges = function(filter) {
#   return function(edge) {
#     if(!filter)                                                   # if there's no filter, everything is valid
#       return true
#
#     if(typeof filter == 'string')                                 # if the filter is a string, the label must match
#       return edge._label == filter
#
#     if(Array.isArray(filter))                                     # if the filter is an array, the label must be in it
#       return !!~filter.indexOf(edge._label)
#
#     return Dagoba.objectFilter(edge, filter)                      # try the filter as an object
#   }
# }
#
# Dagoba.objectFilter = function(thing, filter) {                   # thing has to match all of filter's properties
#   for(var key in filter)
#     if(thing[key] !== filter[key])
#       return false
#
#   return true
# }
#
# Dagoba.cleanVertex = function(key, value) {                       # for JSON.stringify
#   return (key == '_in' || key == '_out') ? undefined : value
# }
#
# Dagoba.cleanEdge = function(key, value) {
#   return (key == '_in' || key == '_out') ? value._id : value
# }
#
# Dagoba.jsonify = function(graph) {                                # kids, don't hand code JSON
#   return '{"V":' + JSON.stringify(graph.vertices, Dagoba.cleanVertex)
#        + ',"E":' + JSON.stringify(graph.edges,    Dagoba.cleanEdge)
#        + '}'
# }
#
# Dagoba.persist = function(graph, name) {
#   name = name || 'graph'
#   localStorage.setItem('DAGOBA::'+name, graph)
# }
#
# Dagoba.depersist = function (name) {
#   name = 'DAGOBA::' + (name || 'graph')
#   var flatgraph = localStorage.getItem(name)
#   return Dagoba.fromString(flatgraph)
# }
#
# Dagoba.error = function(msg) {
#   console.log(msg)
#   return false
# }
#
#
