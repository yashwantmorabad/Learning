class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def inorder(root):
    res=[]
    if root:
        res=inorder(root.left)
        res.append(root.val)
        res=res+inorder(root.right)
    return res

def sorted_array_to_bst(nums):
    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2          # pick middle as root
        node = Node(nums[mid])
        node.left = build(left, mid - 1)   # build left subtree from left half
        node.right = build(mid + 1, right) # build right subtree from right half
        return node

    return build(0, len(nums) - 1)


n=[-10,-3,0,5,9]
root=sorted_array_to_bst(n)
print("Tree:",inorder(root))
m=[10,20,30,50,90]
root1=sorted_array_to_bst(m)
print("Tree:",inorder(root1))
