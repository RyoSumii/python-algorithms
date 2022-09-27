class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "DLL created successfully"

    def insert(self, nodeValue, location):
        if self.head is None:
            print("Create DLL first")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                if tempNode == self.tail:
                    newNode.next = None
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.tail = newNode

                else:
                    newNode.next = tempNode.next
                    newNode.prev = tempNode
                    newNode.next.prev = newNode
                    tempNode.next = newNode

    def traverse(self):
        if self.head is None:
            print("No element in DLL")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverse(self):
        if self.head is None:
            print("No element in DLL")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def search(self, nodeValue):
        if self.head is None:
            return "create DLL first"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return nodeValue
                tempNode = tempNode.next
            return "The nodeValue is not in the DLL"

    def deletenode(self, location):
        if self.head is None:
            print("create DLL first")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been deleted successfully")

    def deleteDLL(self):
        if self.head is None:
            print("There is no nodes")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("DLL has been deleted")


doublyLL = DoubleLinkedList()
doublyLL.create(0)
doublyLL.insert(1, -1)
doublyLL.insert(2, -1)
doublyLL.insert(3, -1)
doublyLL.insert(4, -1)
doublyLL.insert(5, -1)
print([node.value for node in doublyLL])
# doublyLL.traverse()
# doublyLL.reverse()
doublyLL.deletenode(0)
print([node.value for node in doublyLL])
doublyLL.deletenode(1)
print([node.value for node in doublyLL])
doublyLL.deletenode(-1)
print([node.value for node in doublyLL])
doublyLL.deleteDLL()
print([node.value for node in doublyLL])