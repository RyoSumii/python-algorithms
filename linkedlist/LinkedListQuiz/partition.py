from LinkedList import LinkedList


def partition(ll, x):
    cur_node = ll.head
    ll.tail = ll.head

    while cur_node:
        next_node = cur_node.next
        cur_node.next = None

        if cur_node.value < 10:
            cur_node.next = ll.head
            ll.head = cur_node
        else:
            ll.tail.next = cur_node
            ll.tail = cur_node
        cur_node = next_node

    if ll.tail.next is not None:
        ll.tail.next = None


cll = LinkedList()
cll.generate(10, 0, 20)
print(cll)
partition(cll, 10)
print(cll)






