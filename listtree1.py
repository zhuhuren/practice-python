class ListTree:
    def __attrname(self, obj, indent):
        result = ''
        spaces = ' ' * (indent + 1)
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(
                    attr,
                    getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<class {1}, address {2}:(see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            here = self.__attrname(aClass, indent)
            above = ''
            
            self.__visited[aClass] = True
            #classes can be keys in dictinaries
            
            for supercls in aClass.__bases__:
                above += self.__listclass(supercls, indent + 4)
            return '\n{0}<class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                here,
                above,
                dots)

    def __str__(self):
        self.__visited = {}
        here = self.__attrname(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<instance of {0}, address {1}:\n{2}{3}'.format(
            self.__class__.__name__,
            id(self),
            here,
            above
            )

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)
    
    
