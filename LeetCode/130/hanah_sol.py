class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        cols = len(board[0])
        rows = len(board)

        def dfs(x, y):
            nonlocal isolated

            # 이전 값이 경계값인 경우
            if (x < 0 or x > rows-1) or (y < 0 or y > cols - 1):
                return False

            # 방문했는지 확인
            if checked[x][y] == 1:
                return True
            checked[x][y] = 1
            visited[x][y] = 0

            if board[x][y] == 'X':
                return True

            if board[x][y] == 'O':
                isolated.add((x, y))

                # 동서남북으로 이동
                if dfs(x+1, y) and dfs(x, y+1) and dfs(x-1, y) and dfs(x, y-1):
                    return True
                else:
                    return False

        # 고립된 블록 좌표 집합을 담는다.
        isolated = set()
        visited = [[1]*cols for _ in range(rows)]

        for i in range(cols):
            for j in range(rows):
                # 한 번 방문한 곳은 두 번 방문하지 않는다.
                # O가 아닌 곳도 탐색할 필요가 없다.
                if visited[j][i] == 0 or board[j][i] == 'X':
                    continue

                # 매번 블록 검증을 위해 새로 만들어준다.
                checked = [[0]*cols for _ in range(rows)]

                if dfs(j, i):
                    while isolated:
                        x, y = isolated.pop()
                        board[x][y] = 'X'
                else:
                    isolated = set()
