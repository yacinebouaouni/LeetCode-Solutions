class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])


        def bfs(i,j):

            q = deque()
            visited = set()
            q.append([i,j])
            grid[i][j] = 'x'
            count = 1

            while q:

                i,j = q.popleft()
                
                if i+1 < ROWS and grid[i+1][j] == 1:
                    q.append([i+1,j])
                    grid[i+1][j] = 'x'
                    count += 1
                if i-1 >= 0 and grid[i-1][j] == 1:
                    q.append([i-1,j])
                    grid[i-1][j] = 'x'
                    count += 1
                if j+1 < COLS and grid[i][j+1] == 1:
                    q.append([i,j+1])
                    grid[i][j+1] = 'x'
                    count += 1
                if j-1 >= 0 and grid[i][j-1] == 1:
                    q.append([i, j-1])
                    grid[i][j-1] = 'x'
                    count += 1

            return count
                



        max_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count = bfs(i,j)
                    if count > max_count:
                        max_count = count

        return max_count