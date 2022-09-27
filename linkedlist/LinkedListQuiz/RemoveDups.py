from LinkedList import LinkedList


def removeDups(llist):
    if ll.head is None:
        return
    else:
        curNode = llist.head
        visited = {curNode.value}
        while curNode.next:
            if curNode.next.value in visited:
                curNode.next = curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode = curNode.next
        return llist


def removeDups1(llist):
    if ll.head is None:
        return

    curNode = llist.head
    while curNode:
        runner = curNode
        while runner.next:
            if runner.next.value == curNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curNode = curNode.next
    return llist


ll = LinkedList()
ll.generate(10, 0, 10)
print(ll)
removeDups1(ll)
print(ll)
