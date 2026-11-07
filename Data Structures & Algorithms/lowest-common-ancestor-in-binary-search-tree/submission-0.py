# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_lca(node):
            if not node or node is q or node is p:
                return node 

            left = find_lca(node.left)
            right = find_lca(node.right)

            #basically means we are the split point and the current node is the lca
            if left and right:
                return node

            if left:
                return left

            if right:
                return right

            return None

        return find_lca(root)

        #time: O(n), O(h) space since we need to only visit all nodes and recursive call stack.


        