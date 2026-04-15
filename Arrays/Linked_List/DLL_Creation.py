class D_Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head = None
    def insert_at_head(self,val):
        new_node=D_Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def traverse_forward(self):
        current=self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    def traverse_backward(self):
    # 1. Move to the end of the list
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        # 2. Traverse backward using 'prev'
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
D=DLL()
D.insert_at_head(10)
D.insert_at_head(20)
D.insert_at_head(30)
D.traverse_forward()
D.traverse_backward()
