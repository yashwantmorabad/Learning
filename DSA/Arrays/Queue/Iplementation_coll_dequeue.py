'''The main difference between queue using list and 
collection.dequeue is speed i.e time complexity'''
from collections import deque

class SimpleQueue:
    def __init__(self):
        # Initializing the deque
        self.queue = deque()

    def enqueue(self, item):
        """Add an element to the rear (right side)."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front element (left side)."""
        if self.is_empty():
            return "Queue Underflow"
        # popleft() is the optimized O(1) operation
        return self.queue.popleft()

    def peek(self):
        """Look at the front element without removing it."""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", list(self.queue))

# --- Example Usage ---
q = SimpleQueue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.display()
print(f"Front element is {q.peek()}")
print(f"Dequeued: {q.dequeue()}")
q.display()
print(f"Front element is {q.peek()}")