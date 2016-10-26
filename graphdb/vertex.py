
class Vertex:

    def __init__(self, name, vid=None):
        self._id = vid
        self._name = name
        self._in = []
        self._out = []

    def get_id(self):
        return self._id

    def set_id(self, vid):
        self._id = vid

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def add_out(self, edge):
        """
        :param edge:
        :return:
        """
        self._out.append(edge)  # Todo Make sure the edge matches

    def add_in(self, edge):
        self._in.append(edge)

    def get_out_edges(self):
        return self._out

    def get_in_edges(self):
        return self._in
