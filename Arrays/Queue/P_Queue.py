import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # Helps handle elements with the same priority

    def push(self, item, priority):
        """Add an item with a priority. 
        Lower numbers = Higher priority 
        (e.g., 1 is higher than 5)."""
        # We store as (priority, index, item)
        # The index ensures that items with the same priority 
        # are handled in the order they were added.
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
        print(f"Added '{item}' with priority {priority}")

    def pop(self):
        """Remove and return the highest priority item."""
        if self.is_empty():
            return "Queue is empty"
        # heappop always returns the smallest element
        priority, index, item = heapq.heappop(self._queue)
        return item

    def is_empty(self):
        return len(self._queue) == 0

    def display(self):
        # Note: Printing a heap doesn't show it in sorted order, 
        # but the first element is always the highest priority.
        print("Current Heap:", self._queue)

# --- Example Execution ---
pq = PriorityQueue()

# Adding tasks with different priorities
pq.push("Submit Assignment", 2)
pq.push("Pay Rent", 1)         # Highest priority (lowest number)
pq.push("Watch Movie", 5)
pq.push("Fix Bug", 2)          # Same priority as assignment

print("\nProcessing Tasks:")
while not pq.is_empty():
    print(f"Processing: {pq.pop()}")