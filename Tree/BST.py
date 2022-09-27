import queueLinkedlist as queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left is None:
            root_node.left = Node(node_value)
        else:
            insert(root_node.left, node_value)
    else:
        if root_node.right is None:
            root_node.right = Node(node_value)
        else:
            insert(root_node.right, node_value)


def preorder_traversal(root_node):
    if not root_node:
        return
    print(root_node.data, end=" -> ")
    preorder_traversal(root_node.left)
    preorder_traversal(root_node.right)


def inorder_traversal(root_node):
    if not root_node:
        return
    inorder_traversal(root_node.left)
    print(root_node.data, end=" -> ")
    inorder_traversal(root_node.right)


def postorder_traversal(root_node):
    if not root_node:
        return
    postorder_traversal(root_node.left)
    postorder_traversal(root_node.right)
    print(root_node.data, end=" -> ")


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not que.isEmpty():
            root = que.dequeue()
            print(root.value.data, end=" -> ")
            if root.value.left is not None:
                que.enqueue(root.value.left)
            if root.value.right is not None:
                que.enqueue(root.value.right)


def search(root_node, value):
    if not root_node:
        return "Not Found"

    if root_node.data == value:
        return "Found"
    elif value < root_node.data:
        return search(root_node.left, value)
    else:
        return search(root_node.right, value)


def return_min_node(bst_node):
    current = bst_node
    while current.left is not None:
        current = current.left
    return current


def delete(root_node, value):
    if root_node is None:
        return root_node
    if value < root_node.data:
        root_node.left = delete(root_node.left, value)
    elif value > root_node.data:
        root_node.right = delete(root_node.right, value)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp
        if root_node.right is None:
            temp = root_node.right
            root_node = None
            return temp

        temp = return_min_node(root_node.right)
        root_node.data = temp.data
        root_node.right = delete(root_node.right, temp.data)
    return root_node


def delete_bst(root_node):
    root_node.data = None
    root_node.left = None
    root_node.right = None
    return "The BST has been deleted"


bst = Node(None)
insert(bst, 70)
insert(bst, 50)
insert(bst, 90)
insert(bst, 30)
insert(bst, 60)
insert(bst, 80)
insert(bst, 100)
insert(bst, 20)
insert(bst, 40)
# preorder_traversal(bst)
# print()
# inorder_traversal(bst)
# print()
# postorder_traversal(bst)
# print()
level_order_traversal(bst)
print()
delete(bst, 50)
level_order_traversal(bst)
# print(search(bst, 20))
# print(search(bst, 30))
# print(search(bst, 40))
# print(search(bst, 50))
# print(search(bst, 60))
# print(search(bst, 70))
# print(search(bst, 80))
# print(search(bst, 90))
# print(search(bst, 100))
# print(search(bst, 89))
