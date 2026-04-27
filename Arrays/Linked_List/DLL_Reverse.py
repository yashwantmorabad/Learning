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
    def reverse(self):
        if not self.head:
            return  # List is empty

        current = self.head
        temp = None

    # Traverse the list and swap next and prev pointers
        while current:
        # 1. Swap the pointers
            temp = current.prev
            current.prev = current.next
            current.next = temp
        
        # 2. Move to the next node 
        # (Using current.prev because we just swapped it!)
            current = current.prev

    # 3. Update the head 
    # After the loop, 'temp' is at the old second node, 
    # and temp.prev is the old tail (the new head).
        if temp:
            self.head = temp.prev
        return self.head
    #This is too slow for large data    
    def reverse_dll_data(self):
        if not self.head: return None
    
    # Step 1: Move 'right' pointer to the end
        left = self.head
        right = self.head
        while right.next:
            right = right.next
        
    # Step 2: Swap data and move pointers toward middle
    # Loop continues until pointers meet or cross
        while left != right and left.prev != right:
            left.data, right.data = right.data, left.data
            left = left.next
            right = right.prev
        
        return self.head
D=DLL()
D.insert_at_head(10)
D.insert_at_head(20)
D.insert_at_head(30)
D.insert_at_head(40)
D.insert_at_head(50)
D.insert_at_head(60)
print(D.traverse_forward())
Rev=D.reverse()
print(D.traverse_forward())
REV=D.reverse_dll_data()
print(D.traverse_forward())
