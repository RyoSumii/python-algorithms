from LinkedList import LinkedList


def nthToLast(ll, n):
    p1 = ll.head
    p2 = ll.head

    for i in range(n):
        if p2 is None:
            return None
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1


cll = LinkedList()
cll.generate(10, 0, 99)
print(cll)
print(nthToLast(cll, 0))
