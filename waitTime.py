def waitTime(numStudents=10, pagePerMin=10):
    from random import randint
    from queues import Queue
    numOfPrints = 0
    #each student prints 1-2 times
    for student in range(numStudents):
        numOfPrints += randint(0,2)
##    print(numOfPrints)    
    pageList = []
    #1-20 pages per print
    for i in range(numOfPrints):
        pageList.append(randint(1, 20))
##    print(pageList)
    timePerPage = 1 * 60 / pagePerMin
    enterTimeList = []
    #3600 seconds in an hour, make a random list of time each print enters
    for i in range(numOfPrints):
        enterTimeList.append(randint(0,3599))
    enterTimeList.sort()
##    print(enterTimeList)
    listToQueue = zip(enterTimeList, pageList)
    printQueue = Queue()
    for item in listToQueue:
        printQueue.enqueue(item)
    lastEndTime = 0
    totalWaitTime = 0
    while printQueue.size():
        aPrint = printQueue.dequeue()
        thisEnterTime = aPrint[0]
        thisPrintDur = aPrint[1] * timePerPage
        endStartDiff = lastEndTime - thisEnterTime
        endStartDiff = endStartDiff if endStartDiff > 0 else 0
        thisStartTime = thisEnterTime + endStartDiff
        thisEndTime = thisStartTime + thisPrintDur
        totalWaitTime += (thisEndTime - thisEnterTime)
        lastEndTime = thisEndTime
##        print('thisEnterTime: {}, thisPrintDur: {}, endStartDiff: {}, thisStartTime: {}, thisEndTime: {}, totalWaitTime: {}'.format(thisEnterTime, thisPrintDur, endStartDiff, thisStartTime, thisEndTime, totalWaitTime))
    return totalWaitTime / numOfPrints

if __name__ == '__main__':
    totalTime = 0
    times = 3000
    for i in range(times):
        totalTime += waitTime(pagePerMin = 10)
    print(totalTime/times)
        
    
