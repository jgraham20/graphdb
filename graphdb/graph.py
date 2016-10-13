class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = []
        self.vertexIndex = {}
        self.autoid = 1

    def addVertices(self, V):
        # Dagoba.G.addVertices = function(vertices) { vertices.forEach(this.addVertex.bind(this)) }
        pass

    def addEdges(self, E):
        # Dagoba.G.addEdges    = function(edges)    { edges   .forEach(this.addEdge  .bind(this)) }
        pass

        # Dagoba.G.findVertices = function(args) {                          # our general vertex finding function
        #   if(typeof args[0] == 'object')
        #     return this.searchVertices(args[0])
        #   else if(args.length == 0)
        #     return this.vertices.slice()                                  # OPT: slice is costly with lots of vertices
        #   else
        #     return this.findVerticesByIds(args)
        # }

        # Dagoba.G.findVerticesByIds = function(ids) {
        #   if(ids.length == 1) {
        #     var maybe_vertex = this.findVertexById(ids[0])                # maybe_vertex is either a vertex or undefined
        #     return maybe_vertex ? [maybe_vertex] : []
        #   }
        #
        #   return ids.map( this.findVertexById.bind(this) ).filter(Boolean)
        # }

        # Dagoba.G.findVertexById = function(vertex_id) {
        #   return this.vertexIndex[vertex_id]
        # }
        #
        # Dagoba.G.searchVertices = function(filter) {                      # find vertices that match obj's key-value pairs
        #   return this.vertices.filter(function(vertex) {
        #     return Dagoba.objectFilter(vertex, filter)
        #   })
        # }

        # Dagoba.G.findOutEdges = function(vertex) { return vertex._out; }
        # Dagoba.G.findInEdges  = function(vertex) { return vertex._in;  }
        #
        # Dagoba.G.toString = function() { return Dagoba.jsonify(this) }    # serialization
        #
        # Dagoba.fromString = function(str) {                               # another graph constructor
        #   var obj = JSON.parse(str)                                       # this could throw
        #   return Dagoba.graph(obj.V, obj.E)


