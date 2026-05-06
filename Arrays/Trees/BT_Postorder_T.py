import functools
from collections import deque

def trace_operation(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"[TRACE] Executing '{func.__name__}'...")
        return func(*args,**kwargs)
    return wrapper

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.value)

class binary_tree:
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
    @trace_operation
    def postorder_recursive(self):
        result=[]
        self._postorder_recursive_helper(self._root,result)
        return result
    
    def _postorder_recursive_helper(self,current_node,result):
        if current_node is not None:
            self._postorder_recursive_helper(current_node.left,result)
            self._postorder_recursive_helper(current_node.right,result)
            result.append(current_node.value)
    
    @trace_operation
    def postorder_iterative(self):
        """Iterative postorder traversal using a two stack approach
        this a trick:it traverses root-right-left into the second
        stack,which reserves it into left-right-root when popped"""
        if self._root is None:
            return []
        stack1=[self.root]
        stack2=[]
        result=[]
        #Step 1:Process nodes and push them to stack2
        while stack1:
            node=stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            current=stack2.pop()
            result.append(current.value)
        return result

if __name__ == "__main__":
    tree =binary_tree()

    for val in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(val)

    print("--- Testing Traversals ---")
    
    # Run Recursive
    recursive_result = tree.postorder_recursive()
    print(f"Recursive Output: {recursive_result}\n")
    
    # Run Iterative
    iterative_result = tree.postorder_iterative()
    print(f"Iterative Output: {iterative_result}\n")
    
    # Verify they match
    assert recursive_result == iterative_result, "The traversals do not match!"
    print("Success: Both approaches yielded the exact same result.")