# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #for each node, a node is balanced if left subtree and right subtrees are balanced and height difference<=1

        #height of a node = 1 + max(leftsubtreeheight, rightsubtreeheight)

        balanced = True

        def height(root):
            nonlocal balanced
            if not root:
                return 0 

            left = height(root.left)
            right = height(root.right)

            if abs(left-right)>1:
                balanced = False

            return 1+max(left, right)

        height(root)
        return balanced

            

            



            


        