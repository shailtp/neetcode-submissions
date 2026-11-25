# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        lca = root

        def search(node):
            nonlocal lca
            lca = node

            if node is p or node is q:
                return

            elif p.val<node.val and q.val<node.val:
                find_lca = search(node.left)

            elif p.val>node.val and q.val>node.val:
                find_lca = search(node.right)
            
            #no valid paths
            else:
                return

        search(root)
        return lca


            


        