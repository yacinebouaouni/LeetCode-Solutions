class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, True)) # True if u -> v (Reverse)
            graph[v].append((u, False)) # Don't reverse (Example 1 -> 0)

        def dfs(city, visited):

            visited.add(city)
            count = 0
            for neighbor, reverse in graph[city]:
                if neighbor not in visited:
                    count += reverse 
                    count += dfs(neighbor, visited)

            return count

        return dfs(0, set())