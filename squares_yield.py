class Squares():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for x in range(self.start, self.stop + 1):
            yield x ** 2
    def __getitem__(self, index):
        if isinstance(index, int):
            return list(self)[index]
        else:
            return (x for x in list(self)[index])

if __name__ == '__main__':
    s = Squares(3, 17)
    print(type(s).__name__)
    for x in s:
        print(x, end = ' ')
    print()
    print(9 in s)
    print([ x for x in s])
    print(s[2])
    b = s[2:5]
    print(type(b).__name__)
    print(list(b))
