from DLL_Creation import D_Node
class Add:
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
    def traverse_forward(self):
        current=self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

A=Add()
A.append(10)
A.append(20)
A.append(30)
A.traverse_backward()
A.traverse_forward()