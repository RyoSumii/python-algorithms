class BinaryTree:
    def __init__(self, size):
        self.tree_list = size * [None]
        self.last_used_index = 0
        self.maxsize = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.maxsize:
            print("The Binary Tree is full")
            return
        self.tree_list[self.last_used_index+1] = value
        self.last_used_index += 1
        return "The value has been inserted"

    def search_node(self, node_value):
        for i in range(len(self.tree_list)):
            if self.tree_list[i] == node_value:
                print("Success")
                return
        print("Not found")

    def preorder_traversal(self, index=1):
        if index > self.last_used_index:
            return
        print(self.tree_list[index])
        self.preorder_traversal(index*2)
        self.preorder_traversal(index*2 + 1)

    def inorder_traversal(self, index=1):
        if index > self.last_used_index:
            return
        self.inorder_traversal(index*2)
        print(self.tree_list[index])
        self.inorder_traversal(index*2 + 1)

    def postorder_traversal(self, index=1):
        if index > self.last_used_index:
            return
        self.postorder_traversal(index*2)
        self.postorder_traversal(index*2 + 1)
        print(self.tree_list[index])

    def level_order_traversal(self, index=1):
        for i in range(index, self.last_used_index+1):
            print(self.tree_list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return
        for i in range(1, self.last_used_index+1):
            if self.tree_list[i] == value:
                self.tree_list[i] = self.tree_list[self.last_used_index]
                self.tree_list[self.last_used_index] = None
                self.last_used_index -= 1
        print(f"'{value}' is not in the BT")

    def delete_bt(self):
        self.tree_list = None
        print("The binary tree has been deleted")


bt = BinaryTree(8)
bt.insert_node("Drink")
bt.insert_node("Hot")
bt.insert_node("Cold")
bt.insert_node("Tea")
bt.insert_node("Coffee")
bt.insert_node("Fanta")
bt.insert_node("Cola")
bt.delete_node("Drin")
# bt.preorder_traversal()
# bt.inorder_traversal()
# bt.postorder_traversal()
# print(bt.tree_list)
bt.level_order_traversal()




