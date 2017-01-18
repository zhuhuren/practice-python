from string import ascii_uppercase, digits
def postfixToInfix(postfixexpr):
    postfixList = ''.join([' ' + x + ' ' if not x in digits else x for x in postfixexpr])
    postfixList = postfixList.split()
    index = 0
    while len(postfixList) >= 3:
        if index < len(postfixList) and postfixList[index] in '*/+-':
            combineItems(postfixList, index)
            index -= 2
        index += 1
    return postfixList[0]


def combineItems(aList, itemIndex):
    if itemIndex >1 and len(aList) > itemIndex:
        aList[itemIndex - 2: itemIndex + 1] = ['(' + aList[itemIndex -2] + ' ' \
                                              + aList[itemIndex] + ' ' + aList[itemIndex - 1] + ')']

def postfixEval(postfixexpr):
    from stacks import Stack
    opStack = Stack()
    postfixList = ''.join([' ' + x + ' ' if not x in digits else x for x in postfixexpr])
    postfixList = postfixList.split()
    for x in postfixList:
        if not x in '*/+-':
            opStack.push(x)
        else:
            num1 = opStack.pop()
            num2 = opStack.pop()
##            print(str(eval(num2 + x + num1)))
            opStack.push(str(eval(num2 + x + num1)))
    return opStack.pop()

if __name__ == '__main__':
    print(postfixToInfix('A B C * +'))
    print(postfixToInfix('A B * C +'))
    print(postfixToInfix('A B + C *'))
    print(postfixToInfix('A B + C * D E - F G + * -'))
    print(postfixToInfix('A B C * D / + E F G * H I - / J K + / L M - * N * + O + - P - Q / R S T + U - V * W / X Y Z * + * + 1 + * 2 * 3 4 5 6 * - 7 8 + / + / 9 *'))
    print('1 3 / 5 + 2 6 7 * - + = ', postfixEval('1 3 / 5 + 2 6 7 * - +'))
    print('3 8 6 * + 9 3 / - 12 + 4 - 8 2 * + = ', postfixEval('3 8 6 * + 9 3 / - 12 + 4 - 8 2 * +'))
    print( postfixEval('17 10 + 3 * 9 / '))
