# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        def search(node):
            nonlocal lca
            if not node:
                return

            lca = node

            if root is p or root is q:
                return

            elif p.val>node.val and q.val>node.val:
                search(node.right)

            elif p.val<node.val and q.val<node.val:
                search(node.left)

            #split point is the lca
            else:
                return

        search(root)
        return lca
            
        
                



        
        