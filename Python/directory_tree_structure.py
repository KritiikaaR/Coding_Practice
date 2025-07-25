# Node class to represent files or folders in the directory tree
class Node:
    def __init__(self, name, is_file=False):
        self.name = name            # Name of the file or folder
        self.is_file = is_file      # True if it's a file, False if folder
        self.children = []          # List of child nodes (subfolders/files)

# Class representing the entire directory structure
class DirectoryTree:
    def __init__(self):
        self.root = Node("Root")    # Root folder of the directory tree

    #Helper Method 
    def _find(self, current, name):
        """
        Recursively search for a node with the given name.
        Returns the Node object if found, otherwise None.
        """
        if current.name == name:
            return current
        for child in current.children:
            found = self._find(child, name)
            if found:
                return found
        return None

    #Add File or Folder
    def add(self, parent_name, name, is_file=False):
        """
        Add a file or folder under a given parent folder.
        parent_name: Name of the folder where the new node will be added.
        name: Name of the new file/folder.
        is_file: Boolean indicating whether it's a file.
        """
        parent = self._find(self.root, parent_name)
        if parent:
            parent.children.append(Node(name, is_file))
        else:
            # If the parent folder doesn't exist, do nothing
            pass

    # Delete File or Folder
    def delete(self, name):
        """
        Delete a file or folder with the given name.
        Cannot delete the root folder.
        """
        if self.root.name == name:
            print("Cannot delete the root folder.")
            return
        
        # Recursive helper function to delete a node
        def _delete_recursive(parent, name):
            for i, child in enumerate(parent.children):
                if child.name == name:
                    del parent.children[i]
                    return True
                if _delete_recursive(child, name):
                    return True
            return False
        
        if not _delete_recursive(self.root, name):
            print(f"Folder/File '{name}' not found.")

    # Search File or Folder
    def search(self, name):
        """
        Check if a file or folder with the given name exists.
        Returns True if found, False otherwise.
        """
        return self._find(self.root, name) is not None

    #Displaying the Tree
    def display(self, node=None, level=0):
        """
        Display the directory tree structure in a hierarchical format.
        """
        if node is None:
            node = self.root
        print("  " * level + ("[File] " if node.is_file else "[Folder] ") + node.name)
        for child in node.children:
            self.display(child, level + 1)


# Example Usage 
dt = DirectoryTree()
dt.add("Root", "Kritika")
dt.add("Kritika", "Photos")
dt.add("kritika", "Notes.txt", is_file=True)  # This will fail (case-sensitive parent name)
dt.add("Photos", "Vacation.jpg", is_file=True)

dt.display()
print("Searching for 'Notes.txt':", dt.search("Notes.txt"))
dt.delete("Photos")
dt.display()
