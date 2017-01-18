class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext
    def __str__(self):
        return 'Node: {}'.format(self.data)

class UnorderedList:
    def __init__(self):
        self.head = None
    def add(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
##        print(self.head.data)
    def search(self, searchData):
        currentNode = self.head
        found = false
        while currentNode and not found:
            if currentNode.data == searchData:
                found = True
            else:
                currentNode = currentNode.next
        return found
    def remove(self, data):
        previousNode = None
        currentNode = self.head
        found = False
        while currentNode and not found:
            if currentNode.data == data:
                found = True
                if previousNode == None:
                    self.head = currentNode.next
                else:
                    previousNode.next = currentNode.next
            else:
                previousNode = currentNode
                currentNode = currentNode.next
        if not found:
            print(data, 'isn\'t in the list.')
        
    def index(self, item):
        i = 0
        currentNode = self.head
        found = False
        while currentNode and not found:
            if currentNode.data == item:
                found = True
            else:
                currentNode = currentNode.next
                i += 1
        if found:
            return i
        else:
            return -1
    def size(self):
        currentNode = self.head
        result = 0
        while currentNode:
            currentNode = currentNode.next
            result += 1
        return result
    def isEmpty(self):
        return self.head == None

    def insert(self, index, data):
        listSize = self.size()
        if index >= listSize: index = listSize
        previousNode = None
        currentNode = self.head
        if index == 0:
            self.add(data)
        else:
            for i in range(index):
                previousNode = currentNode
                currentNode = currentNode.next
            if currentNode == None:
                previousNode.next = Node(data)
            else:
                tempNode = Node(data)
                tempNode.next = currentNode
                previousNode.next = tempNode
                
    def pop(self):
        listSize = self.size()
        result = None
        if listSize > 0:
            if listSize == 1:
                result = self.head
                self.head = None
            else:
                currentNode = self.head
                for i in range(listSize - 1):
                    previousNode = currentNode
                    currentNode = currentNode.next
                result = currentNode
                previousNode.next = None
        return result
                
    def popPos(self, pos):
        result = None
        listSize = self.size()
        if pos >= 0 and pos < listSize:
            if pos == 0:
                result = self.head
                self.head = result.next
            elif pos == listSize - 1:
                result = self.pop()
            else:
                currentNode = self.head
                previousNode = None
                for i in range(pos):
                    previousNode = currentNode
                    currentNode = currentNode.next
                previousNode.next = currentNode.next
                result = currentNode
        return result

    def __str__(self):
        currentNode = self.head
        result = []
        while currentNode:
            result.append(currentNode.data)
            currentNode = currentNode.next
        return 'UnorderedList({})'.format(result)
        

if __name__ == '__main__':
    ulist = UnorderedList()
    ulist.add(3)
    ulist.add(5)
    ulist.add('abc')
    ulist.add('657')
    ulist.add(6)
    print(ulist)
    print(ulist.index(9))
    ulist.remove(6)
    ulist.remove(3)
    ulist.remove('abc')
    ulist.remove(5)
    ulist.remove('657')
    ulist.insert(0, 5)
    ulist.insert(7, 6)
    ulist.insert(0, 7)
    ulist.insert(1,8)
    print(ulist)
    print('popPos, 3', ulist.popPos(3))
    print(ulist)
    print(ulist.pop())
    print(ulist)
    print(ulist.pop())
    print(ulist)
    print(ulist.pop())
    print(ulist)
    print(ulist.pop())
    print(ulist.pop())
    print(ulist.pop())
    print(ulist.pop())
    print(ulist)
    print(ulist.size())
    print(ulist.isEmpty())
