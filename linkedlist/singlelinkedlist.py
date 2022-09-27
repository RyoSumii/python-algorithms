class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
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

    def traverseSLL(self):
        if self.head is None:
            print("The SLL doesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def serchSLL(self, nodeValue):
        if self.head is None:
            return "The SLL doesn't exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value is not in this list"

    def deleteNode(self, location):
        if self.head is None:
            print("No SSL exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSSL(self):
        if self.head is None:
            print("No SSL exists")
        else:
            self.head = None
            self.tail = None




singleLinkedList = SLinkedList()
singleLinkedList.insertSLL(0, 0)
singleLinkedList.insertSLL(1, 1)
singleLinkedList.insertSLL(2, 2)
singleLinkedList.insertSLL(3, 3)
singleLinkedList.insertSLL(4, 4)
singleLinkedList.insertSLL(5, 5)

print([node.value for node in singleLinkedList])
# singleLinkedList.traverseSLL()
# print(singleLinkedList.serchSLL(9))
singleLinkedList.deleteNode(4)
print([node.value for node in singleLinkedList])
