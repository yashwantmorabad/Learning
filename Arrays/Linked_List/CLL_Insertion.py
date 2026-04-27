class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the Beginning
    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        # We need the last node to update its pointer
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        
        new_node.next = self.head
        curr.next = new_node
        self.head = new_node # Move the head pointer to the new node

    # 2. Insert at the End
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        
        curr.next = new_node
        new_node.next = self.head

    # 3. Insert after a specific value
    def insert_after(self, target_data, data):
        if not self.head:
            return
        
        curr = self.head
        while True:
            if curr.data == target_data:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            if curr == self.head:
                print(f"Node {target_data} not found.")
                break

    def display(self):
        nodes = []
        if self.head:
            curr = self.head
            while True:
                nodes.append(str(curr.data))
                curr = curr.next
                if curr == self.head: break
        print(" -> ".join(nodes) + " -> (Head)")

# Testing
cll = CircularLinkedList()
cll.insert_at_end(20)
cll.insert_at_start(10)   # List: 10 -> 20
cll.insert_at_end(30)     # List: 10 -> 20 -> 30
cll.insert_after(20, 25)  # List: 10 -> 20 -> 25 -> 30
cll.display()