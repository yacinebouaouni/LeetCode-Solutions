class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        ROWS, COLS = len(maze), len(maze[0])
        q = list()
        q.append(entrance)
        maze[entrance[0]][entrance[1]] = 'v'
        count = 0

        while q:

            tmp = q.copy()
            q.clear()

            for i,j in tmp:

                if (i == 0 or i == ROWS-1 or j == 0 or j == COLS-1) and [i,j]!=entrance:
                    return count

                if i+1 < ROWS and maze[i+1][j] == '.':
                    q.append([i+1,j])
                    maze[i+1][j] = 'v'
                if i-1 >= 0 and maze[i-1][j] == '.':
                    q.append([i-1,j])
                    maze[i-1][j] = 'v'
                if j+1 < COLS and maze[i][j+1] == '.':
                    q.append([i,j+1])
                    maze[i][j+1] = 'v'
                if j-1 >= 0 and maze[i][j-1] == '.':
                    q.append([i,j-1])
                    maze[i][j-1] = 'v'

            count += 1

        return -1

        