def insertionSort(aList):
    newList = aList[:]
    aList[:] = []
    for item in newList:
        insertSortedList(item, aList)

def insertSortedList(item, sortedList):
    length = len(sortedList)
    if length == 0:
        sortedList.append(item)
    else:
        start = 0
        end = length - 1
        mid = (start + end) // 2
        while end > start + 1:
            if item > sortedList[mid]:
                start = mid
            else:
                end = mid
            mid = (start + end) // 2
        if item <= sortedList[start]:
            sortedList.insert(start, item)
        elif item > sortedList[start] and item < sortedList[end]:
            sortedList.insert(end, item)
        else:
            sortedList.insert(end+1, item)

if __name__ == '__main__':
    from random import shuffle
    from time import time
    aList = list(range(10000))
    shuffle(aList)
##    print(aList)
    t1 = time()
    insertionSort(aList)
    print(time() - t1)
##    print(aList)
