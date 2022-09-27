class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, nodeValue):
        newnode = Node(nodeValue)
        self.head = newnode
        self.tail = newnode
        newnode.prev = newnode
        newnode.next = newnode
        return "CDLL is created"

    def insert(self, value, location):
        if self.head is None:
            return "create CDLL first"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    if tempNode is self.head:
                        print("Location is bigger than the CDLL dimension")
                        return
                if tempNode == self.tail:
                    newNode.next = self.head
                    newNode.prev = self.tail
                    self.head.prev = newNode
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    newNode.next = tempNode.next
                    newNode.prev = tempNode
                    newNode.next.prev = newNode
                    tempNode.next = newNode

    def traverse(self):
        if self.head is None:
            print("create CDLL first")
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next

    def reverse(self):
        if self.head is None:
            print("create CDLL first")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    def search(self, nodeValue):
        if self.head is None:
            return "create CDLL first"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value isn't in CDLL"
                tempNode = tempNode.next

    def delete(self, location):
        if self.head is None:
            print("create CDLL first")
        else:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None

            elif location == 0:
                # if self.head == self.tail:
                #     self.head.prev = None
                #     self.head.next = None
                #     self.head = None
                #     self.tail = None

                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head

            elif location == -1:
                # if self.head == self.tail:
                #     self.head.prev = None
                #     self.head.next = None
                #     self.head = None
                #     self.tail = None
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail

            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                    if curNode == self.head:
                        print("The location is greater than length of CDLL")
                if curNode == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    curNode.next = curNode.next.next
                    curNode.next.prev = curNode
            print("The node is deleted")

    def deleteCDLL(self):
        if self.head == self.tail:
            print("create CDLL first")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been deleted")



cdll = CircularDoubleLinkedList()
cdll.create(0)
cdll.insert(1, -1)
cdll.insert(2, -1)
print([node.value for node in cdll])
# cdll.traverse()
# cdll.reverse()

cdll.deleteCDLL()
print([node.value for node in cdll])

