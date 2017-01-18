class ListInstance:
    def __attrname(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t{} =\t{}\n'.format(attr, self.__dict__[attr])
        return result
    def __str__(self):
        return '<instance of {}, address {}:\n{}>'.format(self.__class__.__name__,
                                                          id(self), self.__attrname())

if __name__ == '__main__':
    class Super:
        def __init__(self):
            self.data1 = 'spam'
        def ham(self): pass
    class Sub(Super, ListInstance):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42
        def spam(self):
            pass
    s = Sub()
    print(s)
        
