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

    def lca_bst(self,root, p, q):
        """Recursive LCA in a BST. p and q are values."""
        if root is None:
            return None
    # Both on the left
        if p < root.val and q < root.val:
            return self.lca_bst(root.left, p, q)
    # Both on the right
        if p > root.val and q > root.val:
            return self.lca_bst(root.right, p, q)
    # Split point (or one of them equals root.val) → this is the LCA
        return root


    def lca_bst_iter(root, p, q):
        """Iterative version — no recursion stack needed."""
        while root:
            if p < root.val and q < root.val:
                root = root.left
            elif p > root.val and q > root.val:
                root = root.right
            else:
                return root
        return None
    
bst = BST()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 20)
bst.insert(root, 40)
bst.insert(root, 70)
bst.insert(root, 60)
bst.insert(root, 80)
print(bst.inorder(root))
print(bst.lca_bst(root,20,40).val)
print(bst.lca_bst(root,20,60).val)
print(bst.lca_bst(root,30,40).val)
print(bst.lca_bst(root,60,80).val)