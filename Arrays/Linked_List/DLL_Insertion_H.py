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