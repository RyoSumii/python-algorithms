class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traversal(self):
        if self.head is None:
            print("there is no element")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There isn't any node"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return f"The value {nodeValue} does not exist in this CSLL"

    def deteleNode(self, location):
        if self.head is None:
            print("There is not any node in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    if tempNode.next is self.head:
                        print("Location is bigger than the CSLL dimension")
                        return
                nextNode = tempNode.next
                if tempNode.next == self.tail:
                    self.tail = tempNode
                tempNode.next = nextNode.next

    def deleteeEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None





csll = CircularSingleLinkedList()
csll.createCSLL(0)
csll.insertCSLL(1, 1)
csll.insertCSLL(2, 2)
csll.insertCSLL(3, -1)
csll.insertCSLL(4, -1)
print([node.value for node in csll])
csll.deteleNode(3)
print([node.value for node in csll])
print(csll.tail.value)
