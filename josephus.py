from queues import Queue
def josephus(nameList, count):
    q = Queue()
    for name in nameList:
        q.enqueue(name)
    while q.size()>1:
        for j in range(count+1):
            out = q.dequeue()
            if j != count:
                q.enqueue(out)
    return q.dequeue()

if __name__ == '__main__':
    print(josephus(["Bill","David","Susan","Jane","Kent","Brad"],7))
