from LinkedList import LinkedList, Node


def intersect(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode


def addsome(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(3, 0, 5)

llB = LinkedList()
llB.generate(4, 0, 5)

addsome(llA, llB, 7)
addsome(llA, llB, 11)

print(llA)
print(llB)

print(intersect(llA, llB))
