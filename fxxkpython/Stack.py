class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return None
        return self.items.pop()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.items)
print(stack.items.pop())