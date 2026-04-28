class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        # Full if the next step of rear meets the front
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow: The queue is full.")
            return

        # If queue is empty, initialize front and rear to 0
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            # Wrap around using modulo
            self.rear = (self.rear + 1) % self.size
            
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow: The queue is empty.")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None # Clear the slot visually

        # If it was the last element, reset the queue
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Wrap around using modulo
            self.front = (self.front + 1) % self.size
            
        return data

    def display(self):
        print(f"Queue State: {self.queue} | Front: {self.front}, Rear: {self.rear}")

# --- Example Execution ---
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()

print(f"Dequeued: {cq.dequeue()}")
print(f"Dequeued: {cq.dequeue()}")
cq.display()

# Because it's circular, we can now add to the front indices!
cq.enqueue(60)
cq.enqueue(70)
cq.enqueue(80)
cq.display()
print(f"Dequeued: {cq.dequeue()}")
cq.display()