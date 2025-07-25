class Song:
    def __init__(self, title):
        self.title = title  # Song title
        self.next = None    # Pointer to the next song in the playlist


class Playlist:
    def __init__(self):
        self.head = None  # Start of the playlist (head of linked list)

    def add_beginning(self, title):
        # Add a new song at the beginning of the playlist
        new_song = Song(title)
        new_song.next = self.head
        self.head = new_song

    def add_end(self, title):
        # Add a new song at the end of the playlist
        new_song = Song(title)
        if not self.head:  # If playlist is empty
            self.head = new_song
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_song

    def search_song(self, title):
        # Search for a song by title
        current = self.head
        while current:
            if current.title == title:
                return True
            current = current.next
        return False

    def delete_song(self, title):
        # Delete a song from the playlist
        current = self.head
        prev = None
        while current:
            if current.title == title:
                if prev:  # If it's not the first song
                    prev.next = current.next
                else:     # If it's the first song
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def display_songs(self):
        # Display all songs in the playlist
        current = self.head
        while current:
            print(current.title)
            current = current.next

    def reverse_playlist(self):
        # Reverse the playlist order
        prev = None
        current = self.head
        while current:
            next_song = current.next
            current.next = prev
            prev = current
            current = next_song
        self.head = prev

    def sort_playlist(self):
        # Sort playlist alphabetically by title
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current:
            next_song = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_song
        self.head = sorted_list

    def sorted_insert(self, head, new_node):
        # Helper function to insert a song into sorted order
        if not head or new_node.title < head.title:
            new_node.next = head
            return new_node
        current = head
        while current.next and current.next.title < new_node.title:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head


# Example usage
playlist = Playlist()
playlist.add_end("Song C")
playlist.add_end("Song A")
playlist.add_end("Song B")

print("Playlist before sorting:")
playlist.display_songs()

playlist.sort_playlist()
print("\nPlaylist after sorting:")
playlist.display_songs()

playlist.reverse_playlist()
print("\nPlaylist after reversing:")
playlist.display_songs()
