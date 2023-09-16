class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])
        visited, queue = set(), deque()

        movements = [[0,1], [0,-1], [1,0], [-1,0]]
        def is_valid(i,j):
            return (0<=i<=n-1) and (0<=j<=m-1)

        for i in range(n):
            if board[i][0] == 'O':
                visited.add((i,0))
                queue.append((i,0))
                board[i][0] = "T"
            if board[i][m-1] == "O":
                visited.add((i,m-1))
                queue.append((i,m-1))
                board[i][m-1] = "T"

        for j in range(m):
            if board[0][j] == 'O':
                visited.add((0,j))
                queue.append((0,j))
                board[0][j] = "T"
            if board[n-1][j] == "O":
                visited.add((n-1,j))
                queue.append((n-1,j))
                board[n-1][j] = "T"

        
        while queue:

            i,j = queue.popleft()

            for move in movements:
                if is_valid(i+move[0],j+move[1]) and board[i+move[0]][j+move[1]] == "O":
                    board[i+move[0]][j+move[1]] = "T"
                    queue.append((i+move[0], j+move[1]))

        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

        