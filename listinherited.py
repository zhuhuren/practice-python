class ListInherited:
    def __inheritedattr(self, indent = ' ' * 4):
        result = 'Unders{}\n{}{{}}\nOthers{}\n'.format('-' * 77, indent, '-' * 77)
        unders = []
        for attr in dir(self):
            if attr.startswith('__') and attr.endswith('__'):
                unders.append('{}'.format(attr))
            else:
                display = str(getattr(self, attr))[:82 - (len(indent) + len(attr))]
                result += '{}{} ={}\n'.format(indent, attr, display)
        return result.format(', '.join(unders))
    
    def __str__(self):
        return '<instance of {}, address {}:\n{}>'.format(self.__class__.__name__,
                                                          id(self), self.__inheritedattr())
    
if __name__ == '__main__':
    class A:
        def __init__(self):
            self.data1 = 'spam'
        def ham(self):
            self.data1 = 'spam1'

    class B(A, ListInherited):
        def __init__(self):
            self.data2 = 'eggs'
            self.data3 = 42
        def spam(self):
            A.__init__(self)

    b = B()
    b.ham()
    b.spam()
    b.ham()
    print(b)
