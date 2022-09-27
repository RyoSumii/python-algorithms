class Stack:
    def __init__(self, maxsize):
        self.list = []
        self.maxsize = maxsize

    def __str__(self):
        value = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The stack is Full"

        else:
            self.list.append(value)
            return "The element has been inserted successfully"

    def pop(self):
        if self.isEmpty():
            return "There is no elements in the stack"
        else:
            return self.list.pop()

    def peak(self):
        if self.isEmpty():
            return "There is no elements in the stack"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None
        








stack = Stack(4)
print(stack.isEmpty())
print(stack.isFull())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peak())



