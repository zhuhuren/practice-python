def numberSort(numList):
    newList = [None for i in range(maxNum(numList)+1)]
    for num in numList:
        newList[num] = num
    numList[:] = [x for x in newList if x][:]
##    return newList

def maxNum(numList):
    maxNum = None
    if numList:
        max_num = numList.pop()
        for num in numList:
            if num > max_num:
                max_num = num
    return max_num

if __name__ == '__main__':
    from random import shuffle, randint
    from time import time
    num = 1000000
    numList = list(range(num))
    shuffle(numList)
    for i in range(num//10):
        numList.pop(randint(1, num//2))
    t1 = time()
##    print(numList)
    numberSort(numList)
##    print(numList)
    print(time() - t1)
    shuffle(numList)
##    print(numList)
    t1 = time()
    numList.sort()
##    print(numList)
    print(time() - t1)
