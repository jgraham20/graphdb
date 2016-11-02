class Edge(object):

    def __init__(self, label, _in, _out):
        self.label = label
        self.e_in = _in
        self.e_out = _out

    @property
    def label(self):
        return self.label

    @label.setter
    def label(self, label):
        self.label = label

    @property
    def e_out(self):
        return self.e_out

    @property
    def e_in(self):
        return self.e_in

    @e_out.setter
    def e_out(self, _out):
        self.e_out = _out

    @e_in.setter
    def e_in(self, _in):
        self.e_in = _in

    def get_in(self):
        return self.e_in

    def get_out(self):
        return self.e_out
