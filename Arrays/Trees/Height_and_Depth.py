import functools
from collections import deque

# --- 1. Decorator ---
def trace_operation(func):
    """A decorator that logs the execution of tree operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Format the parameters nicely for logging
        params = ", ".join([str(arg) for arg in args[1:]])
        if params:
            print(f"[TRACE] Executing '{func.__name__}' for value: {params}")
        else:
            print(f"[TRACE] Executing '{func.__name__}'...")
        return func(*args, **kwargs)
    return wrapper

# --- 2. Node Class ---
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

# --- 3. Binary Tree Class ---
class BinaryTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, value):
        """Standard level-order insertion."""
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

    # --- CALCULATE HEIGHT ---

    @trace_operation
    def get_tree_height(self):
        """Public method to get the height of the entire tree."""
        return self._height_recursive(self._root)

    def _height_recursive(self, current_node):
        """
        Recursively calculates the height of a node.
        By returning -1 for None, a single leaf node ends up with a height of 0:
        max(-1, -1) + 1 = 0.
        """
        if current_node is None:
            return -1 
        
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        
        return max(left_height, right_height) + 1

    # --- CALCULATE DEPTH ---

    @trace_operation
    def get_node_depth(self, target_value):
        """Public method to find the depth of a specific value in the tree."""
        depth = self._depth_recursive(self._root, target_value, 0)
        if depth == -1:
            print(f"[INFO] Value {target_value} not found in the tree.")
        return depth

    def _depth_recursive(self, current_node, target_value, current_depth):
        """
        Recursively searches for the target_value, keeping track of 
        how deep it has gone. Returns -1 if the value isn't found.
        """
        if current_node is None:
            return -1
            
        if current_node.value == target_value:
            return current_depth

        # Search the left subtree
        left_search = self._depth_recursive(current_node.left, target_value, current_depth + 1)
        if left_search != -1:
            return left_search
            
        # If not in the left, search the right subtree
        return self._depth_recursive(current_node.right, target_value, current_depth + 1)

# --- 4. Testing the Implementations ---
if __name__ == "__main__":
    tree = BinaryTree()

    for val in [50, 30, 70, 20, 40, 60]:
        tree.insert(val)

    tree_height = tree.get_tree_height()
    print(f"Overall Tree Height: {tree_height}")

    depth_70 = tree.get_node_depth(70)
    print(f"Depth of Node 70: {depth_70}")

    depth_40 = tree.get_node_depth(40)
    print(f"Depth of Node 40: {depth_40}")

    depth_60 = tree.get_node_depth(60)
    print(f"Depth of Node 60: {depth_60}")
    
    # Testing a non-existent node
    tree.get_node_depth(999)