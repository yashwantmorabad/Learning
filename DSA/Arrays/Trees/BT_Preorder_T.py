import functools
from collections import deque

# --- 1. Decorators ---

def trace_operation(func):
    """A decorator that logs the execution of tree operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE] Executing '{func.__name__}'...")
        return func(*args, **kwargs)
    return wrapper


# --- 2. Node Class ---

class Node:
    """Represents a single node in the Binary Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


# --- 3. Binary Tree Class ---

class BinaryTree:
    """The main Binary Tree class managing the nodes."""
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, value):
        """Inserts a new value using level-order traversal."""
        new_node = Node(value)
        if self._root is None:
            self._root = new_node
            return

        queue = deque([self._root])
        
        while queue:
            current_node = queue.popleft()

            if current_node.left is None:
                current_node.left = new_node
                break
            else:
                queue.append(current_node.left)

            if current_node.right is None:
                current_node.right = new_node
                break
            else:
                queue.append(current_node.right)

    # --- PREORDER TRAVERSAL: APPROACH 1 (RECURSIVE) ---
    
    @trace_operation
    def preorder_recursive(self):
        """Public method for recursive preorder traversal."""
        result = []
        self._preorder_recursive_helper(self._root, result)
        return result

    def _preorder_recursive_helper(self, current_node, result):
        if current_node is not None:
            # 1. Visit Root
            result.append(current_node.value)
            # 2. Traverse Left
            self._preorder_recursive_helper(current_node.left, result)
            # 3. Traverse Right
            self._preorder_recursive_helper(current_node.right, result)

    # --- PREORDER TRAVERSAL: APPROACH 2 (ITERATIVE) ---

    @trace_operation
    def preorder_iterative(self):
        """
        Iterative preorder traversal using a single stack.
        Notice that we push the right child first, so the left child 
        is processed first when popped (LIFO order).
        """
        if self._root is None:
            return []

        stack = [self._root]
        result = []

        while stack:
            # Pop the top item and add it to results (Root)
            current = stack.pop()
            result.append(current.value)

            # Push right child FIRST
            if current.right is not None:
                stack.append(current.right)
            
            # Push left child SECOND (so it sits on top and gets popped next)
            if current.left is not None:
                stack.append(current.left)

        return result


# --- 4. Testing the Implementations ---

if __name__ == "__main__":
    tree = BinaryTree()

    for val in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(val)

    print("--- Testing Preorder Traversals ---")
    
    # Run Recursive
    recursive_result = tree.preorder_recursive()
    print(f"Recursive Output: {recursive_result}\n")
    
    # Run Iterative
    iterative_result = tree.preorder_iterative()
    print(f"Iterative Output: {iterative_result}\n")
    
    # Verify they match
    assert recursive_result == iterative_result, "The traversals do not match!"
    print("Success: Both approaches yielded the exact same result.")