# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #In BFS we explore the tree level by level.
        #If we look at each level from left to right, 
        #the last node we encounter at that level is 
        #the one visible from the right side.
    
        if not root:
            return []

        queue = deque() #BFS level by level traversal

        queue.append(root)
        result = []


        while queue:
            q = len(queue)

            for i in range(q):
                node = queue.popleft()

                if i == q - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
        #time: O(n), space: O(n)





        


        