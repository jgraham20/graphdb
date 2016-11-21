class Edge(object):

    def __init__(self, label, _in, _out):
        self.label = label
        self.e_in = _in
        self.e_out = _out

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def e_out(self):
        return self._e_out

    @property
    def e_in(self):
        return self._e_in

    @e_out.setter
    def e_out(self, value):
        self._e_out = value

    @e_in.setter
    def e_in(self, value):
        self._e_in = value

    def get_in(self):
        return self.e_in

    def get_out(self):
        return self.e_out
