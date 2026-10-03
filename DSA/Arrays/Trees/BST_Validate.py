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
    
    def is_valid_bst(self,root):
        def validate(node, low, high):
        # Empty subtree is valid
            if node is None:
                return True
        # Current node must fall strictly within (low, high)
            if node.val <= low or node.val >= high:
                return False
        # Left subtree: upper bound becomes current value
        # Right subtree: lower bound becomes current value
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))

bst = BST()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)
bst.insert(root, 40)
print(bst.inorder(root))
print(bst.is_valid_bst(root))

root2=bst.insert(None,10)
bst.insert(root2, 5)
bst.insert(root2, 45)
bst.insert(root2, 60)
bst.insert(root2, 20)
print(bst.inorder(root2))
print(bst.is_valid_bst(root2))
root2.left.val = 100 
print(bst.inorder(root2))
print(bst.is_valid_bst(root2))

bad_root = Node(10,Node(5),Node(15, Node(6), Node(20)))
print(bst.inorder(bad_root))
print(bst.is_valid_bst(bad_root))   # False