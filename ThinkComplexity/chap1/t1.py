class Edge(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __str__(self):
        sVal = ''
        for x in self:
            sVal += str(x)
        return sVal

x = Edge(1,2,44444)
print(x)
