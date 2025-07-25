import heapq  

# Class to implement a Min Heap data structure
class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to store heap elements

    # Insert a new key into the heap
    def insert(self, key):
        self.heap.append(key)  # Add the key at the end
        self.heapify_up(len(self.heap) - 1)  # Re-arrange the heap to maintain min-heap property

    # Get the minimum element (root of the heap)
    def get_min(self):
        if not self.heap:  # If heap is empty
            return None
        return self.heap[0]  # The smallest element is always at index 0

    # Remove and return the minimum element
    def extract_min(self):
        if not self.heap:  # If heap is empty
            return None
        
        if len(self.heap) == 1:  # If there is only one element
            return self.heap.pop()
        
        # Swap the first element with the last, then pop the smallest element
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)  # Re-arrange to maintain min-heap property
        return min_value

    # Re-arrange heap from bottom to top
    def heapify_up(self, index):
        parent = (index - 1) // 2  # Parent index
        # Swap with parent while current node is smaller than parent
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    # Re-arrange heap from top to bottom
    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1  # Left child index
        right = 2 * index + 2 # Right child index

        # Find the smallest among current node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # Swap and continue heapifying if needed
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

# Test the MinHeap class
def main():
    heap = MinHeap()
    # Insert elements into the heap
    for num in [10, 5, 3, 2, 7]:
        heap.insert(num)

    # Display operations
    print("Min element:", heap.get_min())         # Should be 2
    print("Extracted min:", heap.extract_min())   # Should return 2
    print("Heap after extraction:", heap.heap)    # Updated heap
    print("New min element:", heap.get_min())     # Should be 3

if __name__ == "__main__":
    main()
