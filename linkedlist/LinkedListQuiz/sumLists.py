from LinkedList import LinkedList


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10
    if carry > 0:
        ll.add(int(carry))

    return ll

ll1 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)

ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)
print(ll1)
print(ll2)
print(sumList(ll1, ll2))


