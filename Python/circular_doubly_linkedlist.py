# Node class used for both Circular and Doubly Linked Lists
class Node:
    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node (used in Doubly Linked List)


# Class for Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Add a new node to the circular linked list
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.head.next = self.head  # Point to itself to make it circular
        else:
            first = self.head
            # Traverse until we reach the last node (which points back to head)
            while first.next != self.head:
                first = first.next
            first.next = new_node
            new_node.next = self.head  # Complete the circle

    # Remove a node with the given data
    def remove_node(self, data):
        if not self.head:  # If the list is empty, nothing to remove
            return
        temp = self.head
        prev = None
        while True:
            if temp.data == data:
                # Case 1: Only one node in the list
                if temp == self.head and temp.next == self.head:
                    self.head = None
                # Case 2: Removing the head node
                elif temp == self.head:
                    prev = self.head
                    while prev.next != self.head:  # Go to the last node
                        prev = prev.next
                    self.head = temp.next  # Move head
                    prev.next = self.head  # Maintain circular structure
                # Case 3: Removing a middle node
                else:
                    prev.next = temp.next
                return
            prev = temp
            temp = temp.next
            if temp == self.head:  # Stop when we have traversed full circle
                break

    # View all nodes in the circular linked list
    def view_node(self):
        if not self.head:
            print("The list is empty.")
            return

        first = self.head
        while True:
            print(first.data, end=' -> ')
            first = first.next
            if first == self.head:  # Stop when we reach the starting node again
                break
        print("(Back to Head)")


# Class for Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially empty list

    # Add a new node at the end
    def add_node(self, data):
        new_data = Node(data)
        if not self.head:  # If list is empty
            self.head = new_data
            return
        
        first = self.head
        while first.next:  # Traverse to the last node
            first = first.next
        first.next = new_data
        new_data.prev = first  # Set previous pointer

    # Remove a node by data
    def remove_node(self, data):
        if not self.head:
            print("The doubly linked list is empty.")
            return
        
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:  # If not head, adjust previous node's next
                    temp.prev.next = temp.next
                if temp.next:  # If not last, adjust next node's prev
                    temp.next.prev = temp.prev
                if temp == self.head:  # If head, move head forward
                    self.head = temp.next
                return
            temp = temp.next

    # Display nodes from head to end
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display nodes from end to head
    def display_backward(self):
        temp = self.head
        if not temp:
            print("The doubly linked list is empty.")
            return
        while temp.next:  # Move to the last node
            temp = temp.next
        while temp:  # Traverse backward
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")



circular_list = CircularLinkedList()
doubly_list = DoublyLinkedList()

# Circular Linked List Test
for name in ["Alice", "Bob", "Charlie", "Daisy", "Ethan"]:
    circular_list.add_node(name)
print("Circular Linked List:")
circular_list.view_node()

circular_list.remove_node("Charlie")
print("After removing 'Charlie':")
circular_list.view_node()

# Doubly Linked List Test
for name in ["Liam", "Mia", "Noah", "Olivia", "Sophia"]:
    doubly_list.add_node(name)
print("\nDoubly Linked List (Forward):")
doubly_list.display_forward()
print("Doubly Linked List (Backward):")
doubly_list.display_backward()

doubly_list.remove_node("Mia")
print("After removing 'Mia' (Forward):")
doubly_list.display_forward()
print("After removing 'Mia' (Backward):")
doubly_list.display_backward()
