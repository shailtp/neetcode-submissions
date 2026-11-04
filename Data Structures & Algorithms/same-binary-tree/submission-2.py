# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        #structure needs to be identical, and so does the root and child values
        if p and q and p.val==q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        else:
            return False

    
        