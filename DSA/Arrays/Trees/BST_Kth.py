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
    
    def kth_smallest(self,root, k):
    # Use a list as a mutable container so inner function can modify it
        count = [0]
        result = [None]

        def inorder(node):
            if node is None or result[0] is not None:
                return                            # short-circuit once found
            inorder(node.left)
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            inorder(node.right)

        inorder(root)
        return result[0]


    def kth_largest(self,root, k):
    # Reverse inorder: right → node → left visits in descending order
        count = [0]
        result = [None]

        def reverse_inorder(node):
            if node is None or result[0] is not None:
                return
            reverse_inorder(node.right)
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            reverse_inorder(node.left)

        reverse_inorder(root)
        return result[0]
bst = BST()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)
bst.insert(root, 40)
print(bst.inorder(root))
print(bst.kth_smallest(root,2))
print(bst.kth_largest(root,2))