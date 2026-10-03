"Display by converting into string"
def display(self):
    nodes = []
    if self.head:
        curr = self.head
        while True:
            nodes.append(str(curr.data))
            curr = curr.next
            if curr == self.head: break
    print(" -> ".join(nodes) + " -> (Head)") 
"Display without converting into string"
def display_simple(self):
    temp = self.head
    if self.head is not None:
        while True:
            print(temp.data, end=" ") # Directly print the data
            temp = temp.next
            if temp == self.head:
                break
"Display using tail"
def display_simple(self):
        if not self.tail:
            print("List is empty")
            return
        head=self.tail.next
        curr=head
        while True:
            print(curr.data, end=" -> ") # Directly print the data
            curr = curr.next
            if curr == head:
                break
        print("Head")
