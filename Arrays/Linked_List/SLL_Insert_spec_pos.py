from SLL_Creation import Node,List
from SLL_Traversal import traversal
class SLL_I:
    def __init__(self):
        self.head=None
    def insert_at(self,val,pos):
        new_node=Node(val)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr_node=self.head
            prev_node=None
            count=0
            while curr_node is not None and count<pos:
                prev_node=curr_node
                curr_node=curr_node.next
                count+=1
            if prev_node is not None:
                prev_node.next = new_node
                new_node.next = curr_node
            else:
            # This handles the case where the list was empty but pos > 0
                print("Position out of range. Inserting at head instead.")
                self.head = new_node

d=SLL_I()
d.insert_at(40,0)
d.insert_at(30,1)
d.insert_at(20,2)
d.insert_at(10,3)
d.insert_at(50,3)
print(traversal(d))