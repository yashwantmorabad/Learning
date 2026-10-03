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

    @trace_operation
    def count_nodes(self):
        """Public method to get the total number of nodes in the tree."""
        return self._count_nodes_recursive(self._root)

    def _count_nodes_recursive(self, current_node):
        """
        Recursively counts nodes. 
        Returns 0 for an empty branch, otherwise 1 + left_count + right_count.
        """
        if current_node is None:
            return 0
            
        # 1 (Current Node) + Nodes in Left Subtree + Nodes in Right Subtree
        return (1 + 
                self._count_nodes_recursive(current_node.left) + 
                self._count_nodes_recursive(current_node.right))

    @trace_operation
    def count_leaves(self):
        """Public method to get the number of leaf nodes (nodes with no children)."""
        return self._count_leaves_recursive(self._root)

    def _count_leaves_recursive(self, current_node):
        """
        Recursively counts leaf nodes.
        Returns 1 if it's a leaf, otherwise sum of leaves in left and right subtrees.
        """
        if current_node is None:
            return 0
            
        # Is this a leaf? (No left child AND no right child)
        if current_node.left is None and current_node.right is None:
            return 1
            
        # If not a leaf, gather the leaf counts from the children
        return (self._count_leaves_recursive(current_node.left) + 
                self._count_leaves_recursive(current_node.right))

if __name__ == "__main__":
    # Let's build a tree:
    #        10
    #      /    \
    #    20      30
    #   /  \    /
    # 40   50  60 
    #
    # Total Nodes: 6
    # Leaf Nodes: 3 (Nodes 40, 50, and 60)

    tree = Binary_Tree()
    for val in [10, 20, 30, 40, 50, 60]:
        tree.insert(val)

    print("--- Calculating Nodes ---")
    total_nodes = tree.count_nodes()
    print(f"Total number of nodes: {total_nodes}")

    print("\n--- Calculating Leaves ---")
    total_leaves = tree.count_leaves()
    print(f"Total number of leaves: {total_leaves}")