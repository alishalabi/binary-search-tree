"""
Step 1: Build a binary search tree, with add, remove and in methods.

Step 2: Perform DFS's and BFS
"""


class BinaryTreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = True


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, node, current_node):
        # Item already exists, return nothing
        if node.data == current_node.data:
            print("Node data already in Binary Search Tree")
            return self
        # Base case: empty binary tree, add as root
        if self.root == None:
            self.root = node
            return self
        # Begin traversal at root node
        # See if data belongs on left or right of current node
        # Left:
        if node.data < current_node.data:
            # No left value, add node
            if current_node.left_child == None:
                current_node.left_child = node
            # Left value exists, recursively call add
            # with left child as current
            else:
                return self.add(node, current_node.left_child)
        # Right:
        elif node.data > current_node.data:
            # No right value, add node
            if current_node.right_child == None:
                current_node.right_child = node
            # Right value exists, recursively call add
            # with right child as current
            else:
                return self.add(node, current_node.right_child)


nodeA = BinaryTreeNode("A")
nodeB = BinaryTreeNode("B")
nodeB = BinaryTreeNode("B")
test_tree = BinarySearchTree()

# print(f"Node A: {nodeA.data}")
# print(f"Node B: {nodeB.data}")
