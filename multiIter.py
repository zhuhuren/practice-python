class MultiIter():
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return AnotherClass(self.wrapped)
    def __getitem__(self, index):
        return self.wrapped[index]

class AnotherClass():
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = -1
    def __next__(self):
        if self.offset >= len(self.wrapped) - 1:
            raise StopIteration
        self.offset += 1
        return self.wrapped[self.offset]

if __name__ == '__main__':
    a = MultiIter(list(range(50)))
    I = iter(a)
    print(next(I))
    for x in a:
        print(x)
    print([x * 2 for x in a])
    for x in a[::3]:
        for y in a[::3]:
            x = str(x)
            y = str(y)
            for i in range(2 - len(x)): x = '0' + x
            for i in range(2 - len(y)): y = '0' + y
            print(x + y, end = ' ')
        print()
