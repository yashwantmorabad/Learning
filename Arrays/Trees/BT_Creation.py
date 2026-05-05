from ast import arg
import functools
from collections import deque
from hmac import new
from unittest import result

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

if __name__ == "__main__":
    # Initialize the tree
    tree =Binary_Tree()

    # Insert nodes
    tree.insert(50)  
    tree.insert(30)   
    tree.insert(70)  
    tree.insert(20)  
    tree.insert(40)  
    # For a generic Binary tree, level-order traversal shows exactly 
    # the order we inserted them if the tree is complete.
    level_order_data = tree.level_order_traversal()
    
    print(f"\nFinal Level-order Output: {level_order_data}")
    print(f"Root Node Value (@property): {tree.root.data}")
    print(f"Root's Left Child: {tree.root.left.data}")
    print(f"Root's Right Child: {tree.root.right.data}")
            