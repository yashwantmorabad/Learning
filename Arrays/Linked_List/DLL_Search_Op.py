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

    def search_optimized(self, target):
        if not self.head:
            return "List is empty"

        left = self.head
        right = self.tail
        left_pos=0
        right_pos=self.length-1
        # Search from both ends towards the middle
        while left and right and left_pos <= right_pos:
            if left.data == target:
                return f"Found {target} at {left_pos}"
            if right.data == target:
                return f"Found {target} at {right_pos}"
            left=left.next
            right=right.prev

            left_pos+=1
            right_pos-=1
        return "Value not found"
D=DLL()
D.insert_at_head(10)
D.insert_at_head(20)
D.insert_at_head(30)
D.insert_at_head(40)
D.insert_at_head(50)
print(D.search_optimized(20))