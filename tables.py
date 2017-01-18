class Table():
    count = 0
    def __init__(self, name):
        self.name = name
        Table.count += 1 # if a table is deleted by Del, how can this number decrease?

    def setsize(self, width, length):
        self.width = width
        self.length = length
    def setcolor(self, color):
        self.color = color
    def showtable(self):
        print('name = {}'.format(self.name))
        print('width = {}, length = {}'.format(self.width, self.length))
        print('color = {}'.format(self.color))
    def area(self):
        print('Area = ', end = '')
        return self.width * self.length
