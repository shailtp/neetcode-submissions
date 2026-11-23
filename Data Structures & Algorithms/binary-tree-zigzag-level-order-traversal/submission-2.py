# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        
        if not root:
            return []

        queue.append(root)

        reverse = 1

        while queue:
            q = len(queue)
            level = []

            for _ in range(q):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if reverse == 1:
                result.append(level)
                reverse = -1

            else:
                result.append(level[::-1])
                reverse = 1

        return result

        