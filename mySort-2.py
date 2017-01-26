def mySort(aList):
    dividedBy = 1000
    subLen = len(aList) // dividedBy
    listContainer = []
    while aList:
        subList = []
        for i in range(subLen):
            subList.append(aList.pop())
        insertionSort(subList)
        listContainer.append(subList)
    mergeContainer(listContainer)
    return listContainer[0]

def mergeSort(aList):
    if len(aList) > 1:
        listContainer = [[x] for x in aList]
        aList[:] = []
        mergeContainer(listContainer)
        aList[:] = listContainer[0][:]

def mergeSortedLists(list1, list2):
    newlist = []
    if list1 and list2:
        len1 = len(list1)
        len2 = len(list2)
        index1 = 0
        index2 = 0
        while index1 < len1 and index2< len2:
            if list1[index1] < list2[index2]:
                newlist.append(list1[index1])
                index1 += 1
            else:
                newlist.append(list2[index2])
                index2 += 1
    return newlist + list1[index1:] + list2[index2:]

def mergeContainer(listContainer):
    if len(listContainer) > 1:
        newContainer = listContainer[:]
        listContainer[:] = []
        while newContainer:
            if len(newContainer) == 1:
                listContainer.append(newContainer.pop())
            else:
                listContainer.append(mergeSortedLists(newContainer.pop(), newContainer.pop()))
        mergeContainer(listContainer)

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
    aList = list(range(1000000))
    shuffle(aList)
##    print(aList)
    t1 = time()
    mySort(aList)
##    print(mySort(aList))
    print(time() - t1)
