# Dagoba.Pipetypes = {}                                             # every pipe has a type
#
# Dagoba.addPipetype = function(name, fun) {                        # adds a new method to our query object
#   Dagoba.Pipetypes[name] = fun
#   Dagoba.Q[name] = function() {
#     return this.add(name, [].slice.apply(arguments)) }            # capture the pipetype and args
# }
#
# Dagoba.getPipetype = function(name) {
#   var pipetype = Dagoba.Pipetypes[name]                           # a pipe type is just a function
#
#   if(!pipetype)
#     Dagoba.error('Unrecognized pipe type: ' + name)
#
#   return pipetype || Dagoba.fauxPipetype
# }
#
# Dagoba.fauxPipetype = function(graph, args, maybe_gremlin) {      # if you can't find a pipe type
#   return maybe_gremlin || 'pull'                                  # just keep things flowing along
# }
#

# # BUILT-IN PIPE TYPES
#
# Dagoba.addPipetype('vertex', function(graph, args, gremlin, state) {
#   if(!state.vertices)
#     state.vertices = graph.findVertices(args)                     # state initialization
#
#   if(!state.vertices.length)                                      # all done
#     return 'done'
#
#   var vertex = state.vertices.pop()                               # OPT: this relies on cloning the vertices
#   return Dagoba.makeGremlin(vertex, gremlin.state)                # we can have incoming gremlins from as/back queries
# })
#
# Dagoba.simpleTraversal = function(dir) {                          # handles basic in and out pipetypes
#   var find_method = dir == 'out' ? 'findOutEdges' : 'findInEdges'
#   var edge_list   = dir == 'out' ? '_in' : '_out'
#
#   return function(graph, args, gremlin, state) {
#     if(!gremlin && (!state.edges || !state.edges.length))         # query initialization
#       return 'pull'
#
#     if(!state.edges || !state.edges.length) {                     # state initialization
#       state.gremlin = gremlin
#       state.edges = graph[find_method](gremlin.vertex)            # get edges that match our query
#                          .filter(Dagoba.filterEdges(args[0]))
#     }
#
#     if(!state.edges.length)                                       # all done
#       return 'pull'
#
#     var vertex = state.edges.pop()[edge_list]                     # use up an edge
#     return Dagoba.gotoVertex(state.gremlin, vertex)
#   }
# }
#
# Dagoba.addPipetype('in',  Dagoba.simpleTraversal('in'))
# Dagoba.addPipetype('out', Dagoba.simpleTraversal('out'))
#
#
# Dagoba.addPipetype('property', function(graph, args, gremlin, state) {
#   if(!gremlin) return 'pull'                                      # query initialization
#   gremlin.result = gremlin.vertex[args[0]]
#   return gremlin.result == null ? false : gremlin                 # undefined or null properties kill the gremlin
# })
#
# Dagoba.addPipetype('unique', function(graph, args, gremlin, state) {
#   if(!gremlin) return 'pull'                                      # query initialization
#   if(state[gremlin.vertex._id]) return 'pull'                     # we've seen this gremlin, so get another instead
#   state[gremlin.vertex._id] = true
#   return gremlin
# })
#
# Dagoba.addPipetype('filter', function(graph, args, gremlin, state) {
#   if(!gremlin) return 'pull'                                      # query initialization
#
#   if(typeof args[0] == 'object')                                  # filter by object
#     return Dagoba.objectFilter(gremlin.vertex, args[0])
#          ? gremlin : 'pull'
#
#   if(typeof args[0] != 'function') {
#     Dagoba.error('Filter arg is not a function: ' + args[0])
#     return gremlin                                                # keep things moving
#   }
#
#   if(!args[0](gremlin.vertex, gremlin)) return 'pull'             # gremlin fails filter function
#   return gremlin
# })
#
# Dagoba.addPipetype('take', function(graph, args, gremlin, state) {
#   state.taken = state.taken || 0                                  # state initialization
#
#   if(state.taken == args[0]) {
#     state.taken = 0
#     return 'done'                                                 # all done
#   }
#
#   if(!gremlin) return 'pull'                                      # query initialization
#   state.taken++                                                   # THINK: if this didn't mutate state, we could be more
#   return gremlin                                                  # cavalier about state management (but run the GC hotter)
# })
#
# Dagoba.addPipetype('as', function(graph, args, gremlin, state) {
#   if(!gremlin) return 'pull'                                      # query initialization
#   gremlin.state.as = gremlin.state.as || {}                       # initialize gremlin's 'as' state
#   gremlin.state.as[args[0]] = gremlin.vertex                      # set label to the current vertex
#   return gremlin
# })
#
# Dagoba.addPipetype('back', function(graph, args, gremlin, state) {
#   if(!gremlin) return 'pull'                                      # query initialization
#   return Dagoba.gotoVertex(gremlin, gremlin.state.as[args[0]])    # TODO: check for nulls
# })
#
# Dagoba.addPipetype('except', function(graph, args, gremlin, state) {
#   if(!gremlin) return 'pull'                                      # query initialization
#   if(gremlin.vertex == gremlin.state.as[args[0]]) return 'pull'   # TODO: check for nulls
#   return gremlin
# })
#
# Dagoba.addPipetype('merge', function(graph, args, gremlin, state) {
#   if(!state.vertices && !gremlin) return 'pull'                   # query initialization
#
#   if(!state.vertices || !state.vertices.length) {                 # state initialization
#     var obj = (gremlin.state||{}).as || {}
#     state.vertices = args.map(function(id) {return obj[id]}).filter(Boolean)
#   }
#
#   if(!state.vertices.length) return 'pull'                        # done with this batch
#
#   var vertex = state.vertices.pop()
#   return Dagoba.makeGremlin(vertex, gremlin.state)
# })