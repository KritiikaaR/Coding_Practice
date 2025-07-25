class Node:
    def __init__(self, name):
        self.name = name         
        self.children = []        # List of child nodes

    def add_child(self, child):
        # Add a child node to the current node
        self.children.append(child)


class FamilyTree:
    def __init__(self, root_name):
        # Initialize the family tree with the root member
        self.root = Node(root_name)

    def find_node(self, root, name):
        # Recursively search for a node with the given name
        if root is None:
            return None
        if root.name == name:
            return root
        for child in root.children:
            result = self.find_node(child, name)
            if result:
                return result
        return None

    def display_children(self, name):
        # Display the children of a given family member
        root_node = self.find_node(self.root, name)
        if root_node:
            children_names = [child.name for child in root_node.children]
            print(f"Children of {name}: {', '.join(children_names)}")

    def pre_order_traversal(self, root):
        # Pre-order traversal: Root -> Children
        if root is None:
            return []
        names = [root.name]
        for child in root.children:
            names.extend(self.pre_order_traversal(child))
        return names

    def height(self, root):
        # Calculate the height of the family tree
        if root is None:
            return -1
        if not root.children:
            return 0
        return 1 + max(self.height(child) for child in root.children)

    def delete(self, name):
        # Delete a node (and its subtree) from the tree
        root_node = self.find_node(self.root, name)
        if root_node:
            root_node.children = []  # Remove its children
            parent_node = self.find_parent(self.root, name)
            if parent_node:
                # Remove the node from parent's children list
                parent_node.children = [child for child in parent_node.children if child.name != name]

    def find_parent(self, root, name):
        # Find the parent of a node with the given name
        if root is None:
            return None
        for child in root.children:
            if child.name == name:
                return root
            parent = self.find_parent(child, name)
            if parent:
                return parent
        return None


# Example Usage 
family_tree = FamilyTree("Harry Potter")

# Add children of Harry Potter
harry_potter_node = family_tree.root
harry_potter_node.add_child(Node("James Potter"))
harry_potter_node.add_child(Node("Lily Potter"))
harry_potter_node.add_child(Node("Ginny Weasley"))

# Add children of Ginny Weasley
ginny_node = family_tree.find_node(family_tree.root, "Ginny Weasley")
ginny_node.add_child(Node("Albus Potter"))
ginny_node.add_child(Node("James Sirius Potter"))
ginny_node.add_child(Node("Lily Luna Potter"))

# Display the children of Harry Potter
family_tree.display_children("Harry Potter")

# Pre-order traversal before deletion
pre_order_before = family_tree.pre_order_traversal(family_tree.root)
print('Pre-order traversal (Before deletion):')
print(" ".join(pre_order_before))

# Print height of the tree
print(f"\nHeight of Tree: {family_tree.height(family_tree.root)}")

# Delete Ginny Weasley subtree
family_tree.delete("Ginny Weasley")

# Pre-order traversal after deletion
pre_order_after = family_tree.pre_order_traversal(family_tree.root)
print('Pre-order traversal (After deleting "Ginny Weasley"):')
print(" ".join(pre_order_after))
