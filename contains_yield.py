class Iters:
    def __init__(self, value):
        print('set original values')
        self.data = value
##        self.ix = 0
    def __getitem__(self, i):
        print('get[{}]: '.format(i))
        return self.data[i]
    def __iter__(self):
        print('iter=> ', end = ' ')
        for x in self.data:
            yield x
            print('next: ', end = ' ')
##        self.ix = 0
##        return self
##    def __next__(self):
##        print('next: ', end = ' ')
##        for offset in range(len(self.data)):
##            yield self.data[offset]
##        if self.ix == len(self.data):
##            raise StopIteration
##        item = self.data[self.ix]
##        self.ix += 1
##        return item
    def __contains__(self, x):
        print('contains: ', end = ' ')
        return x in self.data

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print( 3 in X)
    for i in X:
           print(i, end=' | ')
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end = ' @ ')
        except StopIteration:
            break
