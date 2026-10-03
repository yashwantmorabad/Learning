from SLL_Creation import Node,List
from SLL_Traversal import traversal
ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
from SLL_Creation import Node, List
from SLL_Traversal import traversal

ll = List()
ll.append(10)
ll.append(20)
ll.append(30)

# Define the function as a standalone utility (remove 'self')
def delete_node(linked_list_obj, key):
    curr = linked_list_obj.head  # Access the head of the object

    if curr is None:
        print("List is empty.")
        return

    # Case: Deleting the Head
    # NOTE: Check if your Node class uses .data or .val! 
    # If the Node class uses self.val, change .data to .val below.
    if curr.data == key:
        linked_list_obj.head = curr.next
        return

    prev = None
    while curr is not None and curr.data != key:
        prev = curr
        curr = curr.next

    if curr is None:
        print(f"Value {key} not found.")
        return

    # Unlink
    prev.next = curr.next

# --- CORRECT EXECUTION ---
# 1. Call the function directly, passing the list object as the first argument
delete_node(ll, 20) 

# 2. Print results
# Note: Ensure traversal() expects the object or the head. 
# If it expects the head, use: traversal(ll.head)
traversal(ll)