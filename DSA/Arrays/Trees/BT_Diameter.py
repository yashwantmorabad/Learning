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
    def get_diameter(self):
        """Public method to find the diameter of the binary tree.
        The diameter is the longest path (number of edges) between any two nodes."""
        # We use a list to hold our maximum diameter to act as a mutable reference
        # that can be updated inside our recursive helper function.
        max_diameter = [0]
        
        self._diameter_recursive(self._root, max_diameter)
        
        return max_diameter[0]

    def _diameter_recursive(self, current_node, max_diameter):
        """
        Returns the height of the current node, but sneaks in a 
        calculation to update the global max_diameter along the way.
        """
        if current_node is None:
            return -1  # Keeping consistent with our previous height definition
            
        # Get the height of the left and right subtrees
        left_height = self._diameter_recursive(current_node.left, max_diameter)
        right_height = self._diameter_recursive(current_node.right, max_diameter)
        
        # The diameter passing THROUGH this specific node is the height 
        # of the left subtree + height of the right subtree + 2 edges connecting them.
        current_node_diameter = left_height + right_height + 2
        
        # Update the maximum diameter if this node's diameter is the biggest we've seen
        max_diameter[0] = max(max_diameter[0], current_node_diameter)
        
        # Return the height of this node for its parent to use
        return max(left_height, right_height) + 1

if __name__ == "__main__":
    # We will build a tree where the longest path is completely in the left subtree.
    #
    #          1 (Root)
    #         / 
    #        2
    #       / \
    #      3   4
    #     /     \
    #    5       6
    #   /         \
    #  7           8
    # 
    # The longest path here is 7 -> 5 -> 3 -> 2 -> 4 -> 6 -> 8. 
    # That is 6 edges. Notice it never touches the root (1).

    # To build this specific custom shape, we'll manually link nodes 
    # instead of using our level-order insert method.
    tree = Binary_Tree()
    tree._root = Node(1)
    tree._root.left = Node(2)
    
    # Left branch of 2
    tree._root.left.left = Node(3)
    tree._root.left.left.left = Node(5)
    tree._root.left.left.left.left = Node(7)
    
    # Right branch of 2
    tree._root.left.right = Node(4)
    tree._root.left.right.right = Node(6)
    tree._root.left.right.right.right = Node(8)

    print("--- Calculating Diameter ---")
    diameter = tree.get_diameter()
    print(f"\nThe maximum diameter of the tree is: {diameter} edges")
    "Diameter is the number of edges between the longest path"