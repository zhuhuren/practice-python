def infixToPostfix(infixexpr):
    from stacks import Stack
    from string import digits, ascii_uppercase
    print(infixexpr)
    infixexpr=infixexpr.replace('**', '^')
    print(infixexpr)
    tokenList = ''.join([' ' + x + ' ' if not x in digits else x for x in infixexpr])
    tokenList = tokenList.split()
    print(tokenList)

    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    postfixList = []
    opStack = Stack()

    for token in tokenList:
        if token in ascii_uppercase or token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            if not opStack.isEmpty():
                topStack = opStack.pop()
            while not opStack.isEmpty() and topStack != '(':
                postfixList.append(topStack)
                topStack = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    result = ' '.join(postfixList)
    result = result.replace('^', '**')
    return result

if __name__ == '__main__':
##    print(infixToPostfix('A + B * C'))
##    print(infixToPostfix('A * B + C'))
##    print(infixToPostfix('( A + B ) * C'))
##    print(infixToPostfix('(A + B) * C - (D - E) * (F + G)'))
##    print(infixToPostfix('(A + B * C / D - (E + F * G / (H - I) / (J + K) * (L - M) * N + O) - P) / Q * (R + (S + T - U) * V / W * (X + Y * Z) + 1) * 2 / (3 + (4 - 5 * 6 )/ (7 + 8)) * 9'))
##    print(infixToPostfix('3 + 8 * 6 - 9 / 3 + 12 - 4 + 8 * 2'))
##    print(infixToPostfix('10 + 3 * 5 / (16 - 4)'))
    print(infixToPostfix('5 * 3 ** (4 - 2)'))

