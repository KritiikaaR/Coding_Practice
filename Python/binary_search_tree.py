# Node class to represent each node in the binary tree
class Node:
    def __init__(self, value):
        self.value = value      # Value of the node
        self.left = None        # Pointer to the left child
        self.right = None       # Pointer to the right child


# Binary Search Tree (BST) implementation
class BinaryTree:
    def __init__(self):
        self.root = None  # Initially, the tree is empty

    # Insert a new value into the tree
    def insert(self, root, value):
        if not root:  # If tree (or subtree) is empty, create a new node
            return Node(value)
        
        if value < root.value:
            # Insert in the left subtree if value is smaller
            root.left = self.insert(root.left, value)
        
        else:
            # Insert in the right subtree if value is larger or equal
            root.right = self.insert(root.right, value)
        
        return root

    # Search for a key in the tree
    def search(self, root, key):
        if not root:  # Reached a leaf without finding the key
            return False
        
        if root.value == key:  # Key found
            return True
        
        if key < root.value:  # Search in left subtree
            return self.search(root.left, key)
        
        return self.search(root.right, key)  # Search in right subtree

    # In-order traversal (Left -> Root -> Right)
    def in_order(self, root):
        if not root:
            return []
        return self.in_order(root.left) + [root.value] + self.in_order(root.right)

    # Find the minimum value (leftmost node)
    def find_min(self, root):
        while root.left:
            root = root.left
        return root.value

    # Find the maximum value (rightmost node)
    def find_max(self, root):
        while root.right:
            root = root.right
        return root.value

    # Calculate the height of the tree
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))



tree = BinaryTree()
numbers = [50, 30, 70, 20, 40, 60, 80]  # Values to insert in BST

# Inserting values into the tree
for num in numbers:
    tree.root = tree.insert(tree.root, num)

# Performing operations
print("Search 40:", "Found" if tree.search(tree.root, 40) else "Not Found")
print("Minimum:", tree.find_min(tree.root))
print("Maximum:", tree.find_max(tree.root))
print("In-order Traversal:", tree.in_order(tree.root))
print("Tree Height:", tree.height(tree.root))
