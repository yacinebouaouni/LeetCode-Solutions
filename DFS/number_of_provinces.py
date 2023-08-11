class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = [False] * len(isConnected)

        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)

        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                count += 1

        return count