class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self, value):
        self.data.insert(0, value)
    def dequeue(self):
        return self.data.pop()
    def isEmpty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)
    def _repr__(self):
        return 'Queue({})'.format(self.data)
    def __str__(self):
        return 'Queue({})'.format(self.data)

if __name__ == '__main__':
    from stacks import Stack
    q = Queue()
    print(q)
    q.enqueue('abc')
    print(q)
    q.enqueue(123)
    print(q)
    q.enqueue([1,2])
    print(q)
    q.enqueue(Stack())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.isEmpty())
    q.dequeue()
