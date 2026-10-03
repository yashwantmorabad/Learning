def traverse_forward(self):
    current=self.head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")