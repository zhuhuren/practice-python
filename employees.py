class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
    def work(self):
        print(self.name, 'does stuff')
    def giveraise(self, percent):
        self.salary *= (1 + percent)
    def __repr__(self):
        return '<{}: name: {}, salary: {}>'.format(self.__class__.__name__, self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, 'makes food.')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, 'interfaces customers.')

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, 'makes pizza.')

if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)
    print(bob.name)
    print(bob.salary)
    bob.work()
    bob.giveraise(0.2)
    print(bob)
    bob
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
