class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        degrees = [0] * numCourses
        order = []

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            degrees[prereq[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            order.append(current)

            for nextCourse in graph[current]:
                degrees[nextCourse] -= 1
                if degrees[nextCourse] == 0:
                    queue.append(nextCourse)

        return order if len(order) == numCourses else []
     