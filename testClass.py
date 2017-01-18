class FirstClass():
    def __init__(self, data, name):
        self.data = data
        self.name = name
    def __add__(self, other):
        self.data += other
    def __str__(self):
        return ('name = {}\ndata = {}\ncolor = {}'.format(self.name, self.data, self.color))
    def __mul__(self, other):
        self.data *= other
    
    def setcolor(self, color):
        self.color = color
    def setdata(self, data):
        self.data = data

class SecondClass(FirstClass):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def setsize(self, width, length):
        self.width = width
        self.length = length

class ThirdClass(SecondClass):
    def __init__(self):
        pass
    def setweight(self, weight):
        self.weight = weight

