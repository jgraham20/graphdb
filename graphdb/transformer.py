# Dagoba.T = []                                                     # transformers (more than meets the eye)
#
# Dagoba.addTransformer = function(fun, priority) {
#   if(typeof fun != 'function')
#     return Dagoba.error('Invalid transformer function')
#
#   for(var i = 0; i < Dagoba.T.length; i++)                        # OPT: binary search
#     if(priority > Dagoba.T[i].priority) break
#
#   Dagoba.T.splice(i, 0, {priority: priority, fun: fun})
# }
#
# Dagoba.transform = function(program) {
#   return Dagoba.T.reduce(function(acc, transformer) {
#     return transformer.fun(acc)
#   }, program)
# }
#
#
# Dagoba.addAlias = function(newname, oldname, defaults) {
#   defaults = defaults || []                                       # default arguments for the alias
#   Dagoba.addPipetype(newname, function() {})                      # because there's no method catchall in js
#   Dagoba.addTransformer(function(program) {
#     return program.map(function(step) {
#       if(step[0] != newname) return step
#       return [oldname, Dagoba.extend(step[1], defaults)]
#     })
#   }, 100)                                                         # these need to run early, so they get a high priority
# }
#
# Dagoba.extend = function(list, defaults) {
#   return Object.keys(defaults).reduce(function(acc, key) {
#     if(typeof list[key] != 'undefined') return acc
#     acc[key] = defaults[key]
#     return acc
#   }, list)
# }
