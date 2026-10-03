class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedListOptimized:
    def __init__(self):
        self.tail = None  # We only track the tail!

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail # Point to itself
        else:
            # New node points to the current head (tail.next)
            new_node.next = self.tail.next
            # Tail now points to the new head
            self.tail.next = new_node
        print(f"Inserted {data} at start")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            # 1. New node points to head
            new_node.next = self.tail.next
            # 2. Current tail points to new node
            self.tail.next = new_node
            # 3. Move the tail pointer to the new node
            self.tail = new_node
        print(f"Inserted {data} at end")

    def insert_at_pos(self, data, pos):
        new_node = Node(data)

        # Case 0: List is empty
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail
            return

        # Case 1: Insert at the beginning (Position 0)
        if pos == 0:
            new_node.next = self.tail.next
            self.tail.next = new_node
            return

        # Case 2: Insert at Middle or End
        curr = self.tail.next  # Start at Head
        for _ in range(pos - 1):
            curr = curr.next
            # If we loop back to head before reaching pos, 
            # it means the index is out of bounds (optional check)
            if curr == self.tail.next:
                print("Position out of range, inserting at end.")
                break
        
        new_node.next = curr.next
        curr.next = new_node
        
        # If we inserted after the current tail, update the tail pointer
        if curr == self.tail:
            self.tail = new_node

    def display_simple(self):
        if not self.tail:
            print("List is empty")
            return
        head=self.tail.next
        curr=head
        while True:
            print(curr.data, end=" -> ") # Directly print the data
            curr = curr.next
            if curr == head:
                break
        print("Head")

    def traversal_length(self):
        curr = self.tail.next # Start at Head
        count=0
        while True:
            curr=curr.next
            count+=1
            if curr == self.tail.next:
                break
        print(count)

cll = CircularLinkedListOptimized()
cll.insert_at_end(10)   # 10 -> (Head)
cll.insert_at_end(20)   # 10 -> 20 -> (Head)
cll.insert_at_start(5)  # 0 -> 10 -> 20 -> (Head)
cll.insert_at_pos(1,0)
cll.display_simple()
cll.traversal_length()