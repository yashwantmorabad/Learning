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
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.value)

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

    @trace_operation
    def is_identical(self, other_tree):
        """
        Public method to check if this tree is identical to another tree.
        Expects another BinaryTree instance as the argument.
        """
        # Safety check: Make sure we are actually comparing to a BinaryTree
        if not isinstance(other_tree, Binary_Tree):
            print("[ERROR] You can only compare a BinaryTree to another BinaryTree.")
            return False
            
        # Start the recursive comparison from the roots of both trees
        return self._is_identical_recursive(self._root, other_tree.root)

    def _is_identical_recursive(self, node1, node2):
        """
        Recursively compares two nodes and their subtrees.
        """
        # Base Case 1: Both nodes are None. 
        # We've hit the bottom of both branches at the same time. This is a match!
        if node1 is None and node2 is None:
            return True
            
        # Base Case 2: Both nodes exist.
        # Check if their values match, AND if their left branches match, AND right branches match.
        if node1 is not None and node2 is not None:
            return (node1.value == node2.value and self._is_identical_recursive(node1.left, node2.left) and self._is_identical_recursive(node1.right, node2.right))
                    
        # Base Case 3: One node exists, but the other is None.
        # The structure is broken. They are not identical.
        return False

if __name__ == "__main__":
    
    tree1 = Binary_Tree()
    for val in [10, 20, 30, 40, 50]:
        tree1.insert(val)

    tree2 = Binary_Tree()
    for val in [10, 20, 30, 40, 50]:
        tree2.insert(val)

    tree3 = Binary_Tree()
    for val in [10, 20, 30, 40, 99]:
        tree3.insert(val)

    # Compare Tree 1 and Tree 2
    match_1_and_2 = tree1.is_identical(tree2)
    print(f"\nAre Tree 1 and Tree 2 identical? {match_1_and_2}")
    
    # Compare Tree 1 and Tree 3
    match_1_and_3 = tree1.is_identical(tree3)
    print(f"\nAre Tree 1 and Tree 3 identical? {match_1_and_3}")