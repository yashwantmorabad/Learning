from SLL_Creation import Node, List
from SLL_Traversal import traversal

ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(traversal(ll))

#Brute-force sol
# temp=ll.head
# stack=[]
# while temp is not None:
#     stack.append(temp.data)
#     temp=temp.next

# temp = ll.head
# while temp is not None:
#     e = stack.pop()
#     temp.data = e
#     temp = temp.next

# print(traversal(ll))

#Optimal sol
temp=ll.head
prev=None
while temp is not None:
    front=temp.next
    temp.next=prev
    prev=temp
    temp=front
ll.head=prev
print(traversal(ll)) 