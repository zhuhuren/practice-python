def convertBase(num, base = 2):
    from stacks import Stack
    s = Stack()
    while num!=0:
        remainder = str(num % base)
        numList = ['10', '11', '12', '13', '14', '15']
        if remainder in numList:
            remainder = 'ABCDEF'[numList.index(remainder)]
        s.push(remainder)
        num //= base
    convertedNum = ''
    while not s.isEmpty():
        convertedNum += s.pop()
    return convertedNum

if __name__ == '__main__':
    print(convertBase(4576459,2))
    print(convertBase(25,8))
    print(convertBase(4576459,10))
    print(convertBase(256,16))
