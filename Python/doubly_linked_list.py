# Node class represents each book in the list
class Node:
    def __init__(self, title, author):
        self.title = title      
        self.author = author    
        self.next = None        # Pointer to the next book
        self.prev = None        # Pointer to the previous book


# Doubly Linked List to manage books
class DoublyLinkedList:
    def __init__(self):
        self.head = None  

    def add_book(self, title, author):
        # Add a new book to the end of the list
        data = Node(title, author)
        if not self.head:  # If list is empty
            self.head = data
            return
        
        first = self.head
        while first.next:  # Traverse to the last book
            first = first.next

        first.next = data
        data.prev = first

    def remove_book(self, title):
        # Remove a book by title
        if not self.head:
            print("The list is empty.")
            return
        
        book = self.head
        if book.title == title:
            # If the book to remove is the first node
            self.head = book.next
            if self.head:
                self.head.prev = None
            print(f'Book "{title}" is removed.')
            return
        
        # Traverse to find the book
        while book and book.title != title:
            book = book.next

        if not book:
            print(f'Book "{title}" not found.')
            return

        # Adjust pointers
        if book.next:
            book.next.prev = book.prev
        if book.prev:
            book.prev.next = book.next

        print(f'Book "{title}" removed.')

    def display_books_forward(self):
        # Display all books in forward order
        if not self.head:
            print("There are no books in the list.")
            return

        first = self.head
        print("Books in forward order:")
        while first:
            print(f"Title: {first.title}, \nAuthor: {first.author}\n")
            first = first.next

    def display_books_backward(self):
        # Display all books in reverse order
        if not self.head:
            print("There are no books in the list.")
            return
         
        last = self.head
        while last.next:  # Move to the last book
            last = last.next
         
        print("Books in backward order:")
        while last:
            print(f"Title: {last.title}, \nAuthor: {last.author}\n")
            last = last.prev

    def search_book(self, title):
        # Search for a book by title
        current = self.head
        while current:
            if current.title == title:
                print(f"\nBook {title} found.")
                print(f"Title: {current.title}, \nAuthor: {current.author}\n")  
                return
            current = current.next

        print(f"Book {title} not found.")


# Example Usage 
def main():
    dll = DoublyLinkedList()
    dll.add_book("Harry Potter", "J.K. Rowling")
    dll.add_book("2 States", "Chetan Bhagat")
    dll.add_book("Book 3", "Me")

    dll.display_books_forward()   
    dll.display_books_backward()

    dll.remove_book("2 States")
    dll.display_books_forward()   
    dll.search_book("Harry Potter")


if __name__ == "__main__":
    main()
