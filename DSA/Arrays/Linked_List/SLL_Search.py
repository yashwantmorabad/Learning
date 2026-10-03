from SLL_Creation import Node, List
from SLL_Traversal import traversal

ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(traversal(ll))
def search(ll, target):
    current = ll.head
    index = 0
    
    while current is not None:
        if current.data == target:
            return f"Element found at index {index}"
        
        current = current.next
        index += 1
        
    return "Element not found"

print(search(ll,30))
print(search(ll,60))