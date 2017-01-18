class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('trace', attrname)
        return getattr(self.wrapped, attrname)

if __name__ == '__main__':
    a = Wrapper([1, 2, 3])
    a.append(4)
    print(a.wrapped)
    b = Wrapper({'a':1, 'b':2})
    print(list(b.keys()))
