class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for i in range(len(equations)):

            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))



        def dfs(var, target, visited):

            visited.add(var)
            for neighbor, caution in graph[var]:
                if neighbor not in visited:
                    if neighbor == target:
                        return caution
                    else:
                        div = dfs(neighbor, target, visited)
                        if div != -1.0:
                            return caution * div

            return -1.0



        output = list()
        for query in queries:

            if query[0] not in graph or query[1] not in graph:
                output.append(-1.0)
            
            elif query[0] == query[1]:
                output.append(1.0)

            else:
                output.append(dfs(query[0], query[1], set()))

        return output


