
class Vertex(object):

    def __init__(self, vertex_name=None, vertex_id=None):
        self.vertex_id = vertex_id
        self.name = vertex_name
        self.v_in = []
        self.v_out = []

    @property
    def vertex_id(self):
        return self._vertex_id

    @vertex_id.setter
    def vertex_id(self, value):
        self._vertex_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_out(self, edge):
        """
        :param edge:
        :return:
        """
        self.v_out.append(edge)  # Todo Make sure the edge matches

    def add_in(self, edge):
        self.v_in.append(edge)

    @property
    def v_out(self):
        return self._v_out

    @property
    def v_in(self):
        return self._v_in

    @v_out.setter
    def v_out(self, value):
        self._v_out = value

    @v_in.setter
    def v_in(self, value):
        self._v_in = value
