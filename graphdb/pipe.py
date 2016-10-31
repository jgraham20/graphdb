class Pipe(object):

    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def exec(self):
        return 'done'

    def __str__(self):
        return self.name