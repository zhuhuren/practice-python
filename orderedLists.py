class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __ge__(self, other):
        return self.data >= other.data
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, nextItem):
        self.next = nextItem
    def __str__(self):
        return 'Node: {}'.format(self.data)

class OrderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.getNext()
        return count
        
    def add(self, data):
        currentNode = self.head
        newNode = Node(data)
        stop = False
        previousNode = None
        while currentNode and not stop:
            if currentNode >= newNode:
                stop = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()
        addItem(self, previousNode, newNode, currentNode)

    def remove(self, data):
        currentNode = self.head
        stop = False
        previousNode = None
        while currentNode and not stop:
            if currentNode.getData() == data:
                stop = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()
        if currentNode:
            removeItem(self, previousNode, currentNode)
        else:
            print('{} not found. Nothing\'s removed'.format(data))
            

    def search(self, searchData):
        currentNode = self.head
        found = False
        while currentNode and not found:
            if currentNode.getData() == searchData:
                found = True
            currentNode = currentNode.getNext()
        return found

    def index(self, data):
        i = 0
        listSize = self.size()
        currentNode = self.head
        found = False
        while currentNode and not found:
            if currentNode.getData() == data:
                found = True
            else:
                i += 1
            currentNode = currentNode.getNext()
##        print(i)
        if i >=0 and i < listSize:
##            print('i: ', i)
            return i
        else:
            return -1
    def popPos(self, pos):
        listSize = self.size()
        if pos >= 0 and pos < listSize:
            currentNode = self.head
            previousNode = None
            for i in range(pos):
                previousNode = currentNode
                currentNode = currentNode.getNext()
            removeItem(self, previousNode, currentNode)

    def pop(self):
        currentNode = self.head
        previousNode = None
        if not self.isEmpty():
            while currentNode.getNext():
                previousNode = currentNode
                currentNode = currentNode.getNext()
            removeItem(self, previousNode, currentNode)
        
    def __str__(self):
        result = []
        currentNode = self.head
        while currentNode:
            result.append(currentNode.getData())
            currentNode = currentNode.getNext()
        return 'OrderedList({})'.format(result)

def addItem(obj, previous, newItem, current):
    if obj.isEmpty():
        obj.head = newItem
    elif previous == None:
        newItem.setNext(current)
        obj.head = newItem
    elif current == None:
        previous.setNext(newItem)
    else:
        newItem.setNext(current)
        previous.setNext(newItem)

def removeItem(obj, previous, current):
    if previous == None:
        obj.head = current.getNext()
    elif current.getNext() == None:
        previous.setNext(None)
    else:
        previous.setNext(current.getNext())

if __name__ == '__main__':
    olist = OrderedList()
    print(olist)
    olist.add(9)
    print(olist)
    olist.add(3)
    print(olist)
    olist.add(8)
    print(olist)
    olist.add(2)
    print(olist)
    olist.add(12)
    print(olist)
    olist.remove(8)
    print(olist)
    olist.remove(12)
    print(olist)
    olist.popPos(9)
    print(olist)
    olist.pop()
    print(olist)
    olist.pop()
    print(olist)
    olist.pop()
    print(olist)
    olist.pop()
    print(olist)
    olist.pop()
    print(olist)
    olist.add(3)
    print(olist)

