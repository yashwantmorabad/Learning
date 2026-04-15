from DLL_Creation import D_Node
class Insertion:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, val, pos):
        new_node = D_Node(val)

        # Case 1: Insert at the beginning
        if pos == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        count = 0

        # Traverse to find the node at the current position
        while current and count < pos:
            prev_node = current
            current = current.next
            count += 1

        # Case 2: Insert at the end (current is None)
        if not current:
            prev_node.next = new_node
            new_node.prev = prev_node
        # Case 3: Insert in the middle
        else:
            new_node.next = current
            new_node.prev = current.prev
            
            # Linking the neighbor back to the new node
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

I=Insertion()
I.insert_at_pos(10,0)
I.insert_at_pos(20,1)
I.insert_at_pos(30,2)
I.insert_at_pos(40,3)
I.insert_at_pos(50,2)
I.traverse()