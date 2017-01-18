class ListInstance:
    def __attrname(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t{}=\t{}\n'.format(attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<instance of {}: address {}:\n{}>'.format(self.__class__.__name__,
                                                         id(self), self.__attrname())

if __name__ =='__main__':
    from employees import PizzaRobot
    class Sub(PizzaRobot, ListInstance):
        pass
    s = Sub('Bob')
    print(s)
