class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class List:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def display(self):
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

ll = List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()