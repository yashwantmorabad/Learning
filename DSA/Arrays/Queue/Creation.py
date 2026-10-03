class SimpleQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            return "Queue Underflow: The queue is empty."
        return self.queue.pop(0)

    def peek(self):
        """View the front element without removing it."""
        if self.is_empty():
            return "Queue is empty."
        return self.queue[0]

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)

    def display(self):
        """Print the current state of the queue."""
        print("Queue:", " -> ".join(map(str, self.queue)))


# --- Example Execution ---
q = SimpleQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print(f"Front element is: {q.peek()}")
print(f"Dequeued element: {q.dequeue()}")

q.display()
print(f"Queue size: {q.size()}")