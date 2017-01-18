from queues import Queue

class Printer:
    def __init__(self, speed = 10, printQueue = Queue(), printPeriod = 3600):
        #unit of speed: pages/minute
        self.printQueue = printQueue
        self.speed = speed
        self.printPeriod = printPeriod
    def isBusy(self):
        if self.printQueue.isEmpty():
            return False
        else:
            return True
        
class Task:
    def __init__(self, enterTime, pages, lastEndTime, printSpeed):
        self.enterTime = enterTime
        self.pages = pages
        self.lastEndTime = lastEndTime
        self.printSpeed = printSpeed
    def waitPeriod(self):
        wait =self.lastEndTime - self.enterTime
        return wait if wait > 0 else 0
    def startTime(self):
        return self.enterTime + self.waitPeriod()
    def endTime(self):
        return self.startTime() + self.printSpeed * self.pages
    def taskLastTime(self):
        return self.endTime() - self.startTime() + self.waitPeriod()
    def __str__(self):
        return ('Time entered: {}\nPages: {}\nTime last task ends: {}\n' + 
    'Time started: {}\nTime ended: {}\nTime Lasted: {}').format(self.enterTime,
                                                               self.pages, self.lastEndTime,
                                                               self.startTime(), self.endTime(),
                                                               self.taskLastTime())
if __name__ == '__main__':
    def test():
        from random import randint
        students = 10
        taskPerStuUpTo = 2
        pagesUpTo = 20
        printPeriod = 1 * 60 * 60
        aPrintQueue = Queue()
        aPrinter = Printer(speed = 12, printQueue = aPrintQueue, printPeriod = 3600)
        numOfTasks = 0
        for i in range(students):
            numOfTasks += randint(0, taskPerStuUpTo)
        enterTimeList = []
        for i in range(numOfTasks):
            enterTimeList.append(randint(0, printPeriod -1))
        enterTimeList.sort()
        lastEndTime = 0
        for enterTime in enterTimeList:
            aTask = Task(enterTime, randint(1,pagesUpTo), lastEndTime, aPrinter.speed)
            aPrintQueue.enqueue(aTask)
            lastEndTime = aTask.endTime()
##        print(aPrintQueue.size())
        totalWaitTime = 0
##        print(aPrinter.printQueue.size())
##        print('isEmpty',aPrinter.printQueue.isEmpty())
##        print(aPrinter.isBusy())
        while aPrinter.isBusy():
##            print(aPrinter.isBusy())
##            print(totalWaitTime)
            totalWaitTime += aPrinter.printQueue.dequeue().taskLastTime()
        return totalWaitTime / numOfTasks

    totalTime = 0
    numOfTests = 10000
    for i in range(numOfTests):
        totalTime += test()
    print(totalTime / numOfTests)
    

        
    
