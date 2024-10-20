# Простое двоичное дерево можно реализовать с помощью узлов,
# где каждый узел хранит свои значения и ссылки на левое и правое поддеревья.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = current_node.right
            current_node.right = new_node

# Пример использования
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)