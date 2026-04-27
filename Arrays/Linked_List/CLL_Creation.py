class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Points to itself
            return

        temp = self.head
        # Traverse until we find the node that points back to head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        nodes = []
        temp = self.head
        while True:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        
        print(" -> ".join(nodes) + " -> (Head)")
        
    def display_simple(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=" -> ") # Directly print the data
                temp = temp.next
                if temp == self.head:
                    break
        

cll=CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)

print("Circular Linked List:")
cll.display()
cll.display_simple()