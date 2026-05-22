class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force is O(n**2), to check all elements

        #we need modified binary search, since rows are sorted

        rows=len(matrix)
        cols=len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==target:
                    return True

        return False