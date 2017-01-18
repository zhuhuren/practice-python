class Stack:
    def __init__(self, data = []):
        try:
            data = list(data)
            if isinstance(data, list):
                self.data = data
        except TypeError:
            print('Argument should be a sequence, no Stack instance is created.')
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data) == 0
    def __str__(self):
        return 'Stack({})'.format(self.data)
    def __repr__(self):
        return 'Stack({})'.format(self.data)

def revstring(mystr):
    a = Stack()
    for s in mystr:
        a.push(s)
    result = ''
    while a.size():
        result += a.pop()
    return result

def isParenBalanced(paren):
    result = True
    paren = [s for s in paren if s == '(' or s == ')']
    p = Stack()
    for s in paren:
        if s == '(':
            p.push(s)
        else:
            if p.isEmpty():
                result = False
                break
            else:
                p.pop()
    if not p.isEmpty():
        result = False             
    return result

def symbolBalance(symbolStr):
    def isReversed(opener, closer):
        openers = '([{'
        closers = ')]}'
        return opener in openers and closer in closers and openers.index(opener) == closers.index(closer)
    balanced = True
    p = Stack()
    index = 0
    while index < len(symbolStr) and balanced:
        s = symbolStr[index]
        if s in '([{':
            p.push(s)
        else:
            if p.isEmpty():
                balanced = False
            else:
                s_pop = p.pop()
                if not isReversed(s_pop, s):
                    balanced = False
        index += 1
    if balanced and p.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    s = Stack([1,3,['a','b','c'],{1,3,6}])
    s.push(2)
    s.push('abc')
    s.push([1,2,3])
    s.push({2,5,8})
    s.push((3,4,5))
    s.push({'a':1, 'b':2})
##    print(s)
##    print(s.pop())
##    print(s)
##    print(s.peek())
##    print(s.size())
##    print(s.isEmpty())
##    print(revstring('abcdefg'))
##    print(isParenBalanced('((()))'))
##    print(isParenBalanced('(()'))
    print(symbolBalance('((()))'))
    print(symbolBalance('()[]{}'))
    print(symbolBalance('{}{()}{()}'))
    
