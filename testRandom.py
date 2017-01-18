def testRandom(testTimes, num):
    from random import randint
    L = [0 for x in range(num)]

    for i in range(testTimes):
        L[randint(0, num-1)] += 1
    return L

if __name__ == '__main__':
    L = testRandom(1000000, 4)
    total = sum(L)
    print([x/total for x in L])
    
