'''I have converted this display function in SLL_Creation
due to get a correct output in this code, Here traversal
and display are same'''
from SLL_Creation import Node,List 
ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
def traversal(self):
    # Start at the beginning of the list
        curr = self.head
    
    # If the list is empty, let the user know
        if not curr:
            print("List is empty.")
            return

    # Traverse until current is None
        while curr:
            # Print the data; 'end' keeps it on one line
            print(curr.data, end=" -> ")
            curr = curr.next
        
        print("None")

print(traversal(ll))