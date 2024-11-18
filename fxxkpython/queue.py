class Queue:
    def __init__(self):
        self.items = []
        self.count = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.count += 1

    def dequeue(self):
        data = self.items.pop()
        self.count -= 1
        return data


queue = Queue()
queue.enqueue('f')
queue.enqueue('u')
queue.enqueue('c')
queue.enqueue('k')
print(queue.items)
print(queue.dequeue())
