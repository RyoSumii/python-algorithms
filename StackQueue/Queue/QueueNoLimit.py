class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is no item in the queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


queue = Queue()
print(queue.isEmpty())
queue.delete()
print(queue.isEmpty())

