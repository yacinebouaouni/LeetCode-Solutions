class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(i, visited):
            
            if len(visited) == len(rooms):
                return True

            for room in rooms[i]:
                if room not in visited:
                    visited.add(room)
                    if dfs(room, visited):
                        return True

            return False


        visited = set()
        visited.add(0)
        return dfs(0, visited)