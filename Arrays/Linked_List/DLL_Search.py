from DLL_Creation import D_Node
class DLL:
    def __init__(self):
        self.head = None
    def append(self,val):
        new_node=D_Node(val)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current
    def search_basic(self, target):
        current = self.head
        position = 0
        
        while current:
            if current.data == target:
                return f"Value {target} found at index {position}"
            current = current.next
            position += 1
            
        return "Value not found"

D=DLL()
D.append(10)
D.append(20)
D.append(30)
print(D.search_basic(30))