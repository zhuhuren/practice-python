def classtree(C):
    if C.__bases__[0].__name__ == 'object':
        return C.__name__
    else:
        List = [C.__name__, [sub for sub in C.__bases__]]
        for i in range(len(List[1])):
            List[1][i] = classtree(List[1][i])
        return List


if __name__ == '__main__':
    class A: pass
    class B: pass
    class C (A): pass
    class D (B): pass
    class E (C, D): pass
    class F (E): pass
    print(classtree(F))
            
