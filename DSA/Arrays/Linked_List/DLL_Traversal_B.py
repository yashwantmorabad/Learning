def traverse_backward(self):
    # 1. Move to the end of the list
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        # 2. Traverse backward using 'prev'
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")