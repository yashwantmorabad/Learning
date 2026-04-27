class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.next=node2
node2.next=node3
node3.next=node4
print(node1.val) #It gives the value stored in it
print(node1)#It gives the address 
print(node1.next)#It gives the address
print(node1.next.val)#It gives the value stored in the next node
print(node2.val)
print(node2)
print(node3.val)
print(node3)
print(node4.val)
print(node4)