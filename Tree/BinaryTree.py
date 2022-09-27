import queueLinkedlist as queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root_node, lst):
    if not root_node:
        return
    lst.append(root_node.data)
    preorder_traversal(root_node.left, lst)
    preorder_traversal(root_node.right, lst)


def inorder_traverse(root_node, lst):
    if not root_node:
        return
    inorder_traverse(root_node.left, lst)
    lst.append(root_node.data)
    inorder_traverse(root_node.right, lst)


def postorder_traverse(root_node, lst):
    if not root_node:
        return
    postorder_traverse(root_node.left, lst)
    postorder_traverse(root_node.right, lst)
    lst.append(root_node.data)


def level_order_traverse(root_node, lst):
    if not root_node:
        return
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not(que.isEmpty()):
            root = que.dequeue()
            lst.append(root.value.data)
            if root.value.left is not None:
                que.enqueue(root.value.left)

            if root.value.right is not None:
                que.enqueue(root.value.right)


def search_bt(root_node, node_value):
    if not root_node:
        return "The BT doesn't exist"
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not que.isEmpty():
            root = que.dequeue()
            if root.value.data == node_value:
                return "Success"
            if root.value.left is not None:
                que.enqueue(root.value.left)

            if root.value.right is not None:
                que.enqueue(root.value.right)
        return "The value didn't found"


def insert_bt(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not que.isEmpty():
            root = que.dequeue()
            if root.value.left is not None:
                que.enqueue(root.value.left)
            else:
                root.value.left = new_node
                return "Success"
            if root.value.right is not None:
                que.enqueue(root.value.right)
            else:
                root.value.right = new_node
                return "Success"


def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not que.isEmpty():
            root = que.dequeue()
            if root.value.left is not None:
                que.enqueue(root.value.left)

            if root.value.right is not None:
                que.enqueue(root.value.right)
        deepest = root.value
        return deepest


def delete_deepest_node(root_node, dnode):
    if not root_node:
        return
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not que.isEmpty():
            root = que.dequeue()
            if root.value is dnode:
                root.value = None
                return
            if root.value.right:
                if root.value.right is dnode:
                    root.value.right = None
                    return
                else:
                    que.enqueue(root.value.right)
            if root.value.left:
                if root.value.left is dnode:
                    root.value.left = None
                    return
                else:
                    que.enqueue(root.value.left)


def delete_bt_node(root_node, target_node):
    if not root_node:
        return
    else:
        que = queue.Queue()
        que.enqueue(root_node)
        while not que.isEmpty():
            root = que.dequeue()
            if root.value.data == target_node:
                dnode = get_deepest_node(root_node)
                root.value.data = dnode.data
                delete_deepest_node(root_node, dnode)
                return "The mode has deleted"
            if root.value.left is not None:
                que.enqueue(root.value.left)

            if root.value.right is not None:
                que.enqueue(root.value.right)
        return "The target_node is not in the BT"


def delete_bt(root_node):
    root_node.data = None
    root_node.left = None
    root_node.right = None
    print("The binary tree has been deleted")


bt = Node("Drinks")
left_child = Node("Hot")
right_child = Node("Cold")
left_left = Node("Tea")
left_right = Node("Coffee")
right_left = Node("Fanta")
right_right = Node("Cola")
bt.left = left_child
bt.right = right_child
bt.left.left = left_left
bt.left.right = left_right
bt.right.left = right_left
bt.right.right = right_right


lst = []
# preorder_traversal(bt, l)
inorder_traverse(bt, lst)
# postorder_traverse(bt, lst)
# print(lst)
# level_order_traverse(bt)
# level_order_traverse(bt, lst)
# print(lst)
# delete_bt_node(bt, "Tea")
# lst = []
# level_order_traverse(bt, lst)
print(lst)
