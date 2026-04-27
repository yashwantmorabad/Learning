from DLL_Creation import D_Node
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None # Track the tail for optimization
        self.length=0
    def insert_at_head(self, val):
        new_node = D_Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node # First node is both head and tail
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
    def delete_node(self, key):
        current = self.head

    # 1. Find the node to delete
        while current:
            if current.data == key:
                break
            current = current.next

    # If the value wasn't found
        if not current:
            print("Value not found in list.")
            return

    # 2. If node to be deleted is the HEAD
        if current == self.head:
            self.head = current.next
            if self.head: # If there's a new head, clear its prev pointer
                self.head.prev = None
            return

    # 3. If node to be deleted is NOT the head
    # Point the PREVIOUS node's 'next' to the CURRENT node's 'next'
        if current.prev:
            current.prev.next = current.next

    # 4. If node to be deleted is NOT the tail
    # Point the NEXT node's 'prev' to the CURRENT node's 'prev'
        if current.next:
            current.next.prev = current.prev
        
    # Python's garbage collector will handle the 'current' node now that it's unlinked
    def traverse_forward(self):
        current=self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
D=DLL()
D.insert_at_head(10)
D.insert_at_head(20)
D.insert_at_head(30)
D.insert_at_head(40)
D.insert_at_head(50)
D.insert_at_head(60)
print(D.traverse_forward())
D.delete_node(60)
print(D.traverse_forward())