def selectionSort(aList):
    length = len(aList)
    if length > 1:
        for i in range(length):
            min_item = aList[i]
##            min_i = i
            for j in range(i, length):
                if aList[j] < min_item:
                    min_item = aList[j]
                    min_i = j
            if aList[i] > min_item:
                aList[i], aList[min_i] = aList[min_i], aList[i]
                
def selectionSort1(aList):
    newList = aList[:]
    aList[:] = []
    while newList:
        min_item = newList[0]
        for item in newList:
            if item < min_item:
                min_item = item
        aList.append(min_item)
        newList.remove(min_item)
        

if __name__ == '__main__':
    from random import shuffle
    from time import time
    aList = list(range(10000))
    shuffle(aList)
##    print(aList)
    t1 = time()
    selectionSort1(aList)
    print(time() - t1)
##    print(aList)
