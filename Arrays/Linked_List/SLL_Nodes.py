from SLL_Creation import Node, List
from SLL_Traversal import traversal

ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(traversal(ll))
def get_length(ll):
    count = 0
    current = ll.head
    
    while current is not None:
        count += 1
        current = current.next
        
    return count
print(get_length(ll))

def get_length_recursive(node):
    if not node:
        return 0
    return 1 + get_length_recursive(node.next)
curr=ll.head
print(get_length_recursive(curr))