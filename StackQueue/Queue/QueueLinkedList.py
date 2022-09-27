class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            temp_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return f"{temp_node} is deleted"

    def peek(self):
        if self.isEmpty():
            return "there is no element in the queue"
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que)
print(que.dequeue())
print(que)




