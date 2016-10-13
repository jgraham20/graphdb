# Dagoba.Q = {}                                                     # prototype
#
# Dagoba.query = function(graph) {                                  # factory (only called by a graph's query initializers)
#   var query = Object.create( Dagoba.Q )
#
#   query.   graph = graph                                          # the graph itself
#   query.   state = []                                             # state for each step
#   query. program = []                                             # list of steps to take
#   query.gremlins = []                                             # gremlins for each step
#
#   return query
# }
#
# Dagoba.Q.run = function() {                                       # our virtual machine for query processing
#   this.program = Dagoba.transform(this.program)                   # activate the transformers
#
#   var max = this.program.length - 1                               # last step in the program
#   var maybe_gremlin = false                                       # a gremlin, a signal string, or false
#   var results = []                                                # results for this particular run
#   var done = -1                                                   # behindwhich things have finished
#   var pc = max                                                    # our program counter -- we start from the end
#
#   var step, state, pipetype
#
#   # driver loop
#   while(done < max) {
#
#     step = this.program[pc]                                       # step is an array: first the pipe type, then its args
#     state = (this.state[pc] = this.state[pc] || {})               # the state for this step: ensure it's always an object
#     pipetype = Dagoba.getPipetype(step[0])                        # a pipetype is just a function
#
#     maybe_gremlin = pipetype(this.graph, step[1], maybe_gremlin, state)
#
#     if(maybe_gremlin == 'pull') {                                 # 'pull' tells us the pipe wants further input
#       maybe_gremlin = false
#       if(pc-1 > done) {
#         pc--                                                      # try the previous pipe
#         continue
#       } else {
#         done = pc                                                 # previous pipe is finished, so we are too
#       }
#     }
#
#     if(maybe_gremlin == 'done') {                                 # 'done' tells us the pipe is finished
#       maybe_gremlin = false
#       done = pc
#     }
#
#     pc++                                                          # move on to the next pipe
#
#     if(pc > max) {
#       if(maybe_gremlin)
#         results.push(maybe_gremlin)                               # a gremlin popped out the end of the pipeline
#       maybe_gremlin = false
#       pc--                                                        # take a step back
#     }
#   }
#
#   results = results.map(function(gremlin) {                       # return either results (like property('name')) or vertices
#     return gremlin.result != null
#          ? gremlin.result : gremlin.vertex } )
#
#   return results
# }
#
#
# Dagoba.Q.add = function(pipetype, args) {                         # add a new step to the query
#   var step = [pipetype, args]
#   this.program.push(step)                                         # step is an array: first the pipe type, then its args
#   return this
# }
#
