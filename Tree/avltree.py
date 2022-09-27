import queueLinkedlist as queue


class AVL:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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


def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height


def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left) - get_height(root_node.right)


def right_rotate(unbalance_node):
    new_root = unbalance_node.left
    unbalance_node.left = unbalance_node.left.right
    new_root.right = unbalance_node
    unbalance_node.height = 1 + max(get_height(unbalance_node.left), get_height(unbalance_node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root


def left_rotate(unbalance_node):
    new_root = unbalance_node.right
    unbalance_node.right = unbalance_node.right.left
    new_root.left = unbalance_node
    unbalance_node.height = 1 + max(get_height(unbalance_node.left), get_height(unbalance_node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root


def insert(root, value):
    if not root:
        return AVL(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and value < root.left.data:
        return right_rotate(root)
    if balance > 1 and value > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and value > root.right.data:
        return left_rotate(root)
    if balance < -1 and value < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root


def get_min_value(root):
    if root is None or root.left is None:
        return root
    return get_min_value(root.left)


def delete(root, value):
    if not root:
        return root
    elif value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = get_min_value(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def delete_avl(root):
    root.data = None
    root.left = None
    root.right = None
    return "The AVL has been deleted"

avl = AVL(5)
avl = insert(avl, 10)
avl = insert(avl, 15)
avl = insert(avl, 20)
avl = delete(avl, 15)
delete_avl(avl)
level_order_traversal(avl)

