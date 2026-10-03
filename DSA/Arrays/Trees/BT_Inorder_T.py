import functools
from collections import deque
from hmac import new
from unittest import result

def trace_operation(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"[TRACE] Executing '{func.__name__}'...")
        result=func(*args,**kwargs)
        return result
    return wrapper

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.value)

class Binary_Tree:
    def __init__(self):
        self._root=None
    
    @property
    def root(self):
        return self._root
    
    def insert(self,value):
        new_node=Node(value)
        if self._root is None:
            self._root=new_node
            return

        queue=deque([self._root])
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
            
    "Recursive approach"
    @trace_operation
    def inorder_recursive(self):
        result=[]
        self._inorder_recursive_helper(self._root,result)
        return result

    def _inorder_recursive_helper(self,current_node,result):
        if current_node is not None:
            self._inorder_recursive_helper(current_node.left,result)
            result.append(current_node.value)
            self._inorder_recursive_helper(current_node.right,result)
    "Iterative approach"
    @trace_operation
    def inorder_iterative(self):
        result=[]
        stack=[]
        current=self._root

        while current is not None or len(stack)>0:
            if current is not None:
                stack.append(current)
                current=current.left
            else:
                current=stack.pop()
                result.append(current.value)
                current=current.right
        return result

if __name__=="__main__":
    tree=Binary_Tree()

    for val in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(val)

    print("--- Testing Traversals ---")
    
    # Run Recursive
    recursive_result = tree.inorder_recursive()
    print(f"Recursive Output: {recursive_result}\n")
    
    # Run Iterative
    iterative_result = tree.inorder_iterative()
    print(f"Iterative Output: {iterative_result}\n")
    
    # Verify they match
    assert recursive_result == iterative_result, "The traversals do not match!"
    print("Success: Both approaches yielded the exact same result.")