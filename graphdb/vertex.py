
class Vertex(object):

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.v_in = []
        self.v_out = []

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

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
        return self.v_out

    @property
    def v_in(self):
        return self.v_in

    @v_out.setter
    def v_out(self, _out):
        self.v_out = _out

    @v_in.setter
    def v_in(self, _in):
        self.v_in = _in
