# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        def dfs(node):
            nonlocal lca

            lca = node

            if node is p or node is q:
                return

            elif node.val>p.val and node.val>q.val:
                dfs(node.left)

            elif node.val<p.val and node.val<q.val:
                dfs(node.right)


            #split point, both on different side
            else:
                return 

        dfs(root)
        return lca


        