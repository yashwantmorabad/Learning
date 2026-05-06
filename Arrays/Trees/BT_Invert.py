import functools
from collections import deque

def trace_operation(func):
    "A decorator that logs the execution of tree operations"
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        params=", ".join([str(arg) for arg in args[1:]])
        print(f"[TRACE] Executing '{func.__name__}' with value(s):{params}")
        result=func(*args,**kwargs)
        return result
    return wrapper

"Node:Creating a node"
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.data)

"Binary tree"
class Binary_Tree:
    def __init__(self):
        self._root=None

    #Using a built-in decorator to create a getter for root
    @property
    def root(self):
        return self._root

    @trace_operation
    def insert(self,value):
        new_node=Node(value)
        if self._root is None:
            self._root=new_node
            return
        "Use a queue to find the first available spot"
        queue=deque([self.root])
        while queue:
            current_node=queue.popleft()
            if current_node.left is None:
                current_node.left=new_node
                break
            else:
                queue.append(current_node.left)
            if current_node.right is None:
                current_node.right=new_node
                break
            else:
                queue.append(current_node.right)

    @trace_operation
    def level_order_traversal(self):
        if self.root is None:
            return []
        elements=[]
        queue=deque([self._root])
        while queue:
            current_node=queue.popleft()
            elements.append(current_node.data)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return elements

    # ... (Keep all your previous __init__, insert, and traversal methods) ...

    # --- INVERT TREE ---

    @trace_operation
    def invert(self):
        """Public method to invert the binary tree."""
        self._invert_recursive(self._root)

    def _invert_recursive(self, current_node):
        """
        Recursively swaps the left and right children of every node.
        """
        # Base Case: We've hit the bottom of a branch
        if current_node is None:
            return
            
        # Step 1: Swap the left and right children
        # In Python, we can do this elegantly in a single line without a temp variable
        current_node.left, current_node.right = current_node.right, current_node.left
        
        # Step 2: Recursively invert the left subtree (which was just swapped)
        self._invert_recursive(current_node.left)
        
        # Step 3: Recursively invert the right subtree (which was just swapped)
        self._invert_recursive(current_node.right)

if __name__ == "__main__":
    # Let's build this tree:
    #        1
    #      /   \
    #     2     3
    #    / \   / 
    #   4   5 6   
    #
    # Notice node 3 has a left child (6) but no right child.
    
    tree = Binary_Tree()
    for val in [1,2,3,4,5,6,7]:
        tree.insert(val)

    print("--- Before Inversion ---")
    # Using the level_order_traversal method we built earlier
    print(f"Level Order: {tree.level_order_traversal()}")
    
    # Let's invert it!
    print("\n--- Inverting ---")
    tree.invert()
    
    # The new tree should look like this:
    #        1
    #      /   \
    #     3     2
    #      \   / \
    #       6 5   4
    
    print("\n--- After Inversion ---")
    print(f"Level Order: {tree.level_order_traversal()}")