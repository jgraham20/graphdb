from collections import namedtuple
from graphdb.graphdb import GraphDB

Step = namedtuple('Step', 'pipe_type, args')


class Query:

    def __init__(self, graph):
        self.graph = graph      # the graph itself
        self.state = []         # state for each step
        self.program = []       # list of steps to take
        self.gremlins = []      # gremlins for each step

    def add(self, pipe_type, args):
        step = Step(pipe_type=pipe_type, args=args)
        print("Add Step: " + str(step))
        self.program.append(step)
        return self  # Todo: Not sure about this

    def run(self):
        self.program = GraphDB.transform(self.program)
        prog_len = len(self.program) - 1
        maybe_gremlin = False
        pc = prog_len
        results = []
        done = -1

        step = state = pipetype = None

        # Driver Loop
        while done < prog_len:

            step = self.program[pc]
            state = self.state[pc] or []
            pipetype = GraphDB.get_pipe_type()




"""
Dagoba.Q.run = function() {                                       # our virtual machine for query processing
  this.program = Dagoba.transform(this.program)                   # activate the transformers

  var max = this.program.length - 1                               # last step in the program
  var maybe_gremlin = false                                       # a gremlin, a signal string, or false
  var results = []                                                # results for this particular run
  var done = -1                                                   # behindwhich things have finished
  var pc = max                                                    # our program counter -- we start from the end

  var step, state, pipetype

  # driver loop
  while(done < max) {

    step = this.program[pc]                                   # step is an array: first the pipe type, then its args
    state = (this.state[pc] = this.state[pc] || {})          # the state for this step: ensure it's always an object
    pipetype = Dagoba.getPipetype(step[0])                   # a pipetype is just a function

    maybe_gremlin = pipetype(this.graph, step[1], maybe_gremlin, state)

    if(maybe_gremlin == 'pull') {                                 # 'pull' tells us the pipe wants further input
      maybe_gremlin = false
      if(pc-1 > done) {
        pc--                                                      # try the previous pipe
        continue
      } else {
        done = pc                                                 # previous pipe is finished, so we are too
      }
    }

    if(maybe_gremlin == 'done') {                                 # 'done' tells us the pipe is finished
      maybe_gremlin = false
      done = pc
    }

    pc++                                                          # move on to the next pipe

    if(pc > max) {
      if(maybe_gremlin)
        results.push(maybe_gremlin)                               # a gremlin popped out the end of the pipeline
      maybe_gremlin = false
      pc--                                                        # take a step back
    }
  }

  results = results.map(function(gremlin) {   # return either results (like property('name')) or vertices
    return gremlin.result != null
         ? gremlin.result : gremlin.vertex } )

  return results
}

"""