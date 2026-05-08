class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class BST:
    def __init__(self):
        self.root=None

    def insert(self,root,val):
        if not root :
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left,val)
        else:
            root.right = self.insert(root.right,val)
        return root
    
    def search(self,root,key):
        if root is None or root.val == key:
            return root

    # Key is greater than root's val, search in right subtree
        if root.val < key:
            return self.search(root.right, key)

    # Key is smaller than root's val, search in left subtree
        return self.search(root.left, key)

    def search_iterative(self,root, key):
        current = root
        while current is not None:
            if key == current.val:
                return current  # Found it
            elif key < current.val:
                current = current.left # Move left
            else:
                current = current.right # Move right
        return None  # Not found
    def inorder(self,root):
        res=[]
        if root:
            res=self.inorder(root.left)
            res.append(root.val)
            res=res+self.inorder(root.right)
        return res
bst = BST()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)
bst.insert(root, 40)
print(bst.inorder(root))
print((bst.search(root,70)).val)
print((bst.search_iterative(root,70)).val)
a=bst.search(root,30)
print(a.val)
print(a.left.val)
print(a.right.val)
''' You need to check if the result is None
    before you ask for its .val. bcz it may cause error
    if value is not there'''
# 1. Do the search and save the whole Node object
result = bst.search(bst.root, 99)

# 2. Check if the search actually found something
if result is not None:
    # Safe to use .val
    print("Found it:", result.val) 
else:
    # No error! Just a nice message.
    print("That number is not in the tree.")