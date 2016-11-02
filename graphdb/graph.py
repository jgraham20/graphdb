from graphdb.edge import Edge
from graphdb.vertex import Vertex
from graphdb.query import Query


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
            self.add_vertex(Vertex(name=v.name, id=v.id))

    def add_edges(self, edges):
        """
        Add edges in List
        """
        for e in edges:
            self.add_edge(Edge(label=e.label, _in=e.e_in, _out=e.e_out))

    def v(self, *args):
        query = Query(self)
        query.add('vertex', args)
        return query

    def find_vertices(self, vertices=None, *args):
        # Fixme
        if not vertices:
            return list(self.vertices)

    def find_vertices_by_ids(self, ids):
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

    @staticmethod
    def search_vertices(vertex, vfilter):
        # Fixme
        #d = {k: v for k, v in self.vertices.items() if v > 0}
        pass

    def find_out_edges(self, vertex):
        """
        Get all out edges for the vertex
        :param vertex:
        :return:
        """
        return vertex.v_out

    def find_in_edges(self, vertex):
        """
        Get all IN edges for the vertex
        :return:
        """
        return vertex.v_in

    def __repr__(self):
        return "WIP"  # Fixme

    def jsonify(self):
        """
        Return a JSON representation of the Graph.
        :return:
        """
        pass  # Fixme


