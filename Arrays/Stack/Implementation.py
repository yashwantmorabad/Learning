class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack underflow:Empty"
        return self._items[-1]
    
    def length(self):
        return len(self._items)

    def __str__(self):
        return f"Stack:{self._items}"

S=Stack()
S.push(10)
S.push(20)
S.push(30)
print(S.__str__())
print(S.length())
print(S.peek())
print(S.pop())
print(S.peek())
print(S.__str__())
print(S.length())