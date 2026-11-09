class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_orange = 0 

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh_orange+=1
                elif grid[i][j]==2:
                    queue.append((i,j))


        if fresh_orange==0:
            return 0

        minute = 0

        while queue:
            q = len(queue)
            minute+=1

            for _ in range(q):
                i,j = queue.popleft()

                for r,c in [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==1:
                        grid[r][c]=2
                        fresh_orange-=1
                        queue.append((r,c))
                
            if fresh_orange==0:
                return minute

        return -1

        