# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #pass lowest, highest values along with node in dfs. recursively change low limit to node.vak for right
        #and high limit to node.val for letf
        if not root:
            return True

        def dfs(node, low, high):
            if not node:
                return True

            #in case node value not within limits, we can return Flase
            if node.val>=high or node.val<=low:
                return False

            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float('-inf'), float('inf'))


            


        