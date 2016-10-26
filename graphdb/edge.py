class Edge:

    def __init__(self, label, _in, _out):
        self._label = label
        self._in = _in
        self._out = _out

    def get_label(self):
        return self._label

    def get_out(self):
        return  self._out

    def get_in(self):
        return self._in

    def set_out(self, _out):
        self._out = _out

    def set_in(self, _in):
        self._in = _in
