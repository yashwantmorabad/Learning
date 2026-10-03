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