def hanoi(numOfDisc, fromPole, toPole, withPole, count):
    if numOfDisc > 0:
        hanoi(numOfDisc-1, fromPole, withPole, toPole, count)
        count[0] += 1
        move(fromPole, toPole)
        hanoi(numOfDisc-1, withPole, toPole, fromPole, count)
    return count[0]

def move(fromPole, toPole):
    print(fromPole, 'to', toPole)

if __name__ == '__main__':
    print(hanoi(4, 'A', 'B', 'C', [0]))
