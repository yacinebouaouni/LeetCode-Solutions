class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]

        if n == 1 and any(obstacleGrid[0]):
            return 0
        elif n == 1 and not any(obstacleGrid[0]):
            return 1
        
        elif m == 1 and any([obstacleGrid[i][0] for i in range(n)]):
            return 0

        elif m == 1 and not any([obstacleGrid[i][0] for i in range(n)]):
            return 1



        for i in range(n-1, -1, -1):
            if obstacleGrid[i][m-1] == 1:
                break
            else:
                dp[i][m-1] = 1
        
        for j in range(m-1, -1, -1):
            if obstacleGrid[n-1][j] == 1:
                break
            else:
                dp[n-1][j] = 1

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
