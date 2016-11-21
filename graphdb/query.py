from collections import namedtuple
from functools import wraps


class GenerativeBase(object):
    def _generate(self):
        s = self.__class__.__new__(self.__class__)
        s.__dict__ = self.__dict__.copy()
        return s


def _generative(func):
    @wraps(func)
    def decorator(self, *args, **kw):
        new_self = self._generate()
        func(new_self, *args, **kw)
        return new_self
    return decorator

Step = namedtuple('Step', 'pipe_type, args')


class Query:

    def __init__(self, graph):
        self.graph = graph      # the graph itself
        self.state = []         # state for each step
        self.program = []       # list of steps to take
        self.gremlins = []      # gremlins for each step
        self.pipetypes = {}

    def __getattr__(self, name):
        print(name)
        return self.pipetypes[name]

    def add(self, pipe_type, args):
        step = Step(pipe_type=pipe_type, args=args)
        print("Add Step: " + str(step))
        self.program.append(step)
        self.pipetypes[pipe_type] = args
        return self

    def run(self):
        self.program = self.graph.transform(self.program)
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
            pipetype = self.graph.get_pipe_type(step[0])  # Pipetype is a function # TODO: should this call back to graph
            maybe_gremlin = pipetype(self.graph, step[1], maybe_gremlin, state)

            if maybe_gremlin == 'pull':  # 'pull' tells us the pipe wants further input
                maybe_gremlin = False
                if pc-1 > done:
                    pc -= 1  # try the previous pipe
                    continue
                else:
                    done = pc  # previous pipe is finished, so we are too

            if maybe_gremlin == 'done':  # 'done' tells us the pipe is finished
                maybe_gremlin = False
                done = pc

            pc += 1

            if pc > max:
                if maybe_gremlin:
                    results.append(maybe_gremlin)  # a gremlin popped out the end of the pipeline
                    maybe_gremlin = False
                    pc -= 1  # take a step back

            results = [gremlin.result if gremlin.result else gremlin.vertex for gremlin in results]

            return results

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