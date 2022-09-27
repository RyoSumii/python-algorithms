class Queue:
    def __init__(self, maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self):
        if self.isEmpty():
            return "there is no element in the queue"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxsize * [None]
        self.start = -1
        self.top = -1


que = Queue(3)
que.enqueue(0)
que.enqueue(1)
que.enqueue(2)
print(que.peek())
que.dequeue()
print(que.peek())
que.dequeue()
print(que.peek())
que.dequeue()
print(que.peek())
