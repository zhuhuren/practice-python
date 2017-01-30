def insertSort(aList, start, step):
    length = len(aList)
    for i in range(start, length, step):
        cVal = aList[i]
        position = i
        while position >= step and aList[position-step] > cVal:
            aList[position] = aList[position - step]
            position = position - step
        aList[position]=cVal

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


def shellSort(aList):
    sublistcount = len(aList) // 2
    while sublistcount>=1:
        for i in range(sublistcount):
            insertSort(aList, i, sublistcount)
        sublistcount //= 2

def shellSort1(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

##      print("After increments of size",sublistcount,
##                                   "The list is",alist)

      sublistcount = sublistcount // 2

if __name__ == '__main__':
    from random import shuffle
    from time import time
    aList = list(range(100000))
    shuffle(aList)
##    print(aList)
##    t1 = time()
##    insertSort(aList,0,1)
##    print(time()-t1)
##    print(aList)
    
    shuffle(aList)
##    print(aList)
    t1 = time()
    shellSort(aList)
    print(time()-t1)
##    print(aList)

##    shuffle(aList)
##    t1 = time()
##    gapInsertionSort(aList,0,1)
##    print(time()-t1)

    shuffle(aList)
##    print(aList)
    t1 = time()
    shellSort1(aList)
    print(time()-t1)
##    print(aList)

    shuffle(aList)
    t1 = time()
    aList.sort()
    print(time()-t1)
