class A:
    def method(self):
        print('I\'m in class: A')

class B(A):
    def method4(self):
        print('I\'m in class: B')

class C(A):
    def method5(self):
        print('I\'m in class: C')

class D(C):
    def method3(self):
        print('I\'m in class: D')

class E(B, D):
    def method2(self):
        print('I\'m in class: E')

if __name__ == '__main__':
    e = E()
    e.method()
