from graphdb.vertex import Vertex
from graphdb.edge import Edge


class Graph:

    def __init__(self):

        self.edges = []
        self.vertices = []
        self.vertexIndex = {}
        self.autoid = 1

    def add_vertex(self, vertex):
        """
         Add a vertex to the graph
        """
        vid = vertex.get_id()

        if not vid:
            vertex.set_id(self.autoid)
            self.autoid += 1
        elif self.find_vertex_by_id(vid):
            raise Exception('The vertex id is already in use')

        self.vertices.append(vertex)
        self.vertexIndex[vertex.get_id()] = vertex

        return vertex.get_id()

    def add_edge(self, edge):
        """
        # Add edge
        :param edge:
        :return:
        """
        edge_in = self.find_vertex_by_id(edge.get_in())
        edge_out = self.find_vertex_by_id(edge.get_out())

        if not edge_in and edge_out:
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
            self.add_vertex(Vertex(name=v["name"], vid=v["_id"]))

    def add_edges(self, edges):
        """
        Add edges in List
        """
        for e in edges:
            self.add_edge(Edge(label=e["_label"], _in=e["_in"], _out=e["_out"]))

    def find_vertices(self, vertices=None):
        """
        Dagoba.G.findVertices = function(args) {                          # our general vertex finding function
          if(typeof args[0] == 'object')
            return this.searchVertices(args[0])
          else if(args.length == 0)
            return this.vertices.slice()                                  # OPT: slice is costly with lots of vertices
          else
            return this.findVerticesByIds(args)
        }
        """
        # Fixme
        if not vertices:
            return list(self.vertices)

    def find_vertices_by_ids(self, ids):
        """
        Dagoba.G.findVerticesByIds = function(ids) {
          if(ids.length == 1) {
            var maybe_vertex = this.findVertexById(ids[0])                # maybe_vertex is either a vertex or undefined
            return maybe_vertex ? [maybe_vertex] : []
          }

          return ids.map( this.findVertexById.bind(this) ).filter(Boolean)
        }
        """
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

    def search_vertices(self, vertex_filter):
        """
        Dagoba.G.searchVertices = function(filter) {                      # find vertices that match obj's key-value pairs
          return this.vertices.filter(function(vertex) {
            return Dagoba.objectFilter(vertex, filter)
          })
        }
        """
        # Fixme
        #d = {k: v for k, v in self.vertices.items() if v > 0}
        pass

    def find_out_edges(self, vertex):
        """
        Get all out edges for the vertex
        :param vertex:
        :return:
        """
        return vertex.get_out_edges()


    def find_in_edges(self, vertex):
        """
        Get all IN edges for the vertex
        :return:
        """
        return vertex.get_out_edges()

    def __repr__(self):
        """
        Dagoba.G.toString = function() { return Dagoba.jsonify(this) }    # serialization
        """

        return "WIP" # Fixme

    def jsonify(self):
        """
        Return a JSON representation of the Graph.
        :return:
        """
        pass # Fixme


