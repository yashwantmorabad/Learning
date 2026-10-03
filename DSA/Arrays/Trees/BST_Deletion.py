class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.val)
            res = res + self.inorder(root.right)
        return res

    def find_min(self, node):
        """Helper function to find the smallest value node in a tree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        # Base case: empty tree / key not found
        if root is None:
            return None

        # 1. Search for the node to delete — use `root`, NOT `self.root`
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)

        # 2. Found the node
        else:
            # Cases 1 & 2: 0 or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: 2 children — replace with inorder successor
            successor = self.find_min(root.right)
            root.val = successor.val
            root.right = self.delete(root.right, successor.val)

        return root


bst = BST()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)
bst.insert(root, 40)
print(bst.inorder(root))           # [20, 30, 40, 50, 70]

root = bst.delete(root, 50)   
print(bst.inorder(root))           
# root = bst.delete(root, 70)   
# print(bst.inorder(root))           
