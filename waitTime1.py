from random import randrange
from queues import Queue

class Printer:
    def __init__(self, pagesPerMin):
        self.ppm = pagesPerMin
        self.currentTask = None
        self.timeRemain = 0

    def tick(self):
        self.timeRemain -= 1
        if self.timeRemain <=0:
            self.timeRemain = 0
            
    def nextTask(self, task):
        self.currentTask = task

    def isBusy(self):
        return bool(self.currentTask)

class Task:
    def __init__(self, timeStamp):
        self.timeStamp = timeStamp
        self.pages = randrange(1, 21)

if __name__ == '__main__':
    def testWaitTime(numOfStudents, duration):
        numOfTasks = numOfStudents * 2
##        print(numOfTasks)
        printQueue = Queue()
        aPrinter = Printer(10)
        waitTimeList = []

        for currentSecond in range(duration):
            if hasTask(numOfTasks, duration):
                timeStamp = currentSecond
##                print(timeStamp)
                printQueue.enqueue(Task(timeStamp))
            if not aPrinter.isBusy() and not printQueue.isEmpty():
                currentTask = printQueue.dequeue()
                aPrinter.nextTask(currentTask)
                waitTimeList.append(currentSecond - currentTask.timeStamp)
##                print('currentSecond', currentSecond)
##                print('currentTask.timeStamp', currentTask.timeStamp)
##                print('currentSecond - currentTask.timeStamp', currentSecond - currentTask.timeStamp)
                aPrinter.timeRemain = 60 / aPrinter.ppm * currentTask.pages
##                print(aPrinter.ppm)
##                print('pages: {}, timeRemain: {}'.format(currentTask.pages,aPrinter.timeRemain))
                    
            if aPrinter.isBusy():
##                print(currentSecond)
                aPrinter.tick()
                if aPrinter.timeRemain <= 0:
                    aPrinter.currentTask = None
                    
        return sum(waitTimeList) / len(waitTimeList)
##        return waitTimeList
                    

    def hasTask(numOfTasks, duration):
        probabilityBase = int(duration / numOfTasks)
        if randrange(0, probabilityBase) == probabilityBase - 1:
            return True
        else:
            return False

##    print(testWaitTime(10, 3600))
    total = 0
    for i in range(100):
        total += testWaitTime(10, 3600)
    print(total / 100)
    
