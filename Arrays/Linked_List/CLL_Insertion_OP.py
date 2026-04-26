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
cll = CircularLinkedListOptimized()
cll.insert_at_end(10)   # 10 -> (Head)
cll.insert_at_end(20)   # 10 -> 20 -> (Head)
cll.insert_at_start(0)  # 0 -> 10 -> 20 -> (Head)
cll.display_simple()
# Assuming 'cll' is your Circular Linked List object
head_node = cll.tail.next
tail_node = cll.tail

print(f"Head ID: {id(head_node)}")
print(f"Tail points to: {id(tail_node.next)}")

if id(head_node) == id(tail_node.next):
    print("Proof: The Tail's 'next' is exactly the same object as the Head!")