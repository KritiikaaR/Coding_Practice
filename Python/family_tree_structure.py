class Node:
    def __init__(self, name):
        self.name = name          # Name of the family member
        self.left = None          # Left child 
        self.right = None         # Right child 


class FamilyTree:
    def __init__(self, root_name):
        self.root = Node(root_name)  # Root of the tree

    def find_node(self, root, name):
        # Recursively search for a node by name
        if not root:
            return None
        if root.name == name:
            return root
        left = self.find_node(root.left, name)
        if left:
            return left
        return self.find_node(root.right, name)

    def insert(self, parent_name, child_name, position):
        # Insert a child under the given parent node (left or right)
        parent = self.find_node(self.root, parent_name)
        if parent:
            if position == 'left' and not parent.left:
                parent.left = Node(child_name)
            elif position == 'right' and not parent.right:
                parent.right = Node(child_name)

    def pre_order(self, root):
        # Pre-order traversal: Root -> Left -> Right
        if not root:
            return []
        return [root.name] + self.pre_order(root.left) + self.pre_order(root.right)

    def in_order(self, root):
        # In-order traversal: Left -> Root -> Right
        if not root:
            return []
        return self.in_order(root.left) + [root.name] + self.in_order(root.right)

    def post_order(self, root):
        # Post-order traversal: Left -> Right -> Root
        if not root:
            return []
        return self.post_order(root.left) + self.post_order(root.right) + [root.name]

    def level_order(self):
        # Level-order traversal (BFS)
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.name)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def search(self, root, name):
        # Search for a member by name
        if not root:
            return False
        if root.name == name:
            return True
        return self.search(root.left, name) or self.search(root.right, name)

    def count_members(self, root):
        # Count all members in the tree
        if not root:
            return 0
        return 1 + self.count_members(root.left) + self.count_members(root.right)

    def height(self, root):
        # Find the height of the tree
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def delete_subtree(self, root, name):
        # Delete an entire subtree rooted at the given name
        if not root:
            return None
        if root.left and root.left.name == name:
            root.left = None
        elif root.right and root.right.name == name:
            root.right = None
        else:
            self.delete_subtree(root.left, name)
            self.delete_subtree(root.right, name)

    def move_child(self, from_parent, to_parent, child_name, position):
        # Move a child from one parent to another
        child = self.detach_child(self.root, from_parent, child_name)
        if child:
            new_parent = self.find_node(self.root, to_parent)
            if new_parent:
                if position == 'left' and not new_parent.left:
                    new_parent.left = child
                elif position == 'right' and not new_parent.right:
                    new_parent.right = child

    def detach_child(self, root, parent_name, child_name):
        # Detach a child node from its current parent
        if not root:
            return None
        if root.name == parent_name:
            if root.left and root.left.name == child_name:
                temp = root.left
                root.left = None
                return temp
            if root.right and root.right.name == child_name:
                temp = root.right
                root.right = None
                return temp
        left = self.detach_child(root.left, parent_name, child_name)
        if left:
            return left
        return self.detach_child(root.right, parent_name, child_name)


# Example Usage
tree = FamilyTree("Parent-0")
tree.insert("Parent-0", "Parent-1", "left")
tree.insert("Parent-0", "Parent-2", "right")
tree.insert("Parent-1", "Child-1A", "left")
tree.insert("Parent-1", "Child-1B", "right")
tree.insert("Parent-2", "Child-2A", "left")
tree.insert("Parent-2", "Child-2B", "right")
tree.insert("Parent-2", "Child-2C", "left")  # This won't insert (left already filled)

print("Pre-order:", tree.pre_order(tree.root))
print("In-order:", tree.in_order(tree.root))
print("Post-order:", tree.post_order(tree.root))
print("Level-order:", tree.level_order())
print("Search Child-1A:", tree.search(tree.root, "Child-1A"))
print("Total Members:", tree.count_members(tree.root))
print("Tree Height:", tree.height(tree.root))
tree.delete_subtree(tree.root, "Parent-1")
tree.move_child("Parent-1", "Parent-2", "Child-1A", "right")
