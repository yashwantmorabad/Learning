# 1. Define the Node and List structures correctly
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class List:
    def __init__(self):
        self.head = None

    # We need append to actually put data in the list!
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_kth_from_last_brute(self, k):
        # Pass 1: find length
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next

        if k > length or k <= 0:
            return 

        target = length - k

        # Edge case: delete head
        if target == 0:
            self.head = self.head.next
            return

        # Pass 2: reach node just before target
        curr = self.head
        for _ in range(target - 1):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

# 2. Standalone traversal function (takes 'll' as an argument)
def traversal(ll_obj):
    curr = ll_obj.head
    if not curr:
        print("List is empty.")
        return
    
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# 3. Execution Logic
ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Before Deletion:")
traversal(ll)

# Perform deletion (k=1 is the tail, which is 50)
ll.delete_kth_from_last_brute(2)

print("After Deleting 1st from last:")
traversal(ll)


#Optimal sol
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class List:
    def __init__(self):
        self.head = None

    # We need append to actually put data in the list!
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    def delete_kth_from_last_optimised(self, k):
        dummy = Node(0)
        dummy.next = self.head

        fast = dummy
        slow = dummy

    # Move fast k steps ahead
        for _ in range(k):
            fast = fast.next

    # Move both until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

    # slow.next is the target — unlink it
        slow.next = slow.next.next

        self.head = dummy.next  # update head in case it was deleted
    

ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Before Deletion:")
traversal(ll)

# Perform deletion (k=1 is the tail, which is 50)
ll.delete_kth_from_last_optimised(2)

print("After Deleting 1st from last:")
traversal(ll)
