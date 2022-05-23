def solution(m, n, board):
    disappear_block = [[0 for _ in range(n)]
                       for _ in range(m)]  # [[0]*n]*m 얕은복사 현상
    board = [list(arr) for arr in board]

    # 2*2 윈도우??
    def checkIf(r, c):
        the_character = board[r][c]
        if board[r][c] == 0 or c + 1 >= n or r - 1 < 0:
            return False
        if board[r][c+1] != the_character or board[r-1][c] != the_character or board[r-1][c+1] != the_character:
            return False
        return True

    def recordIt(r, c):
        disappear_block[r][c] = 1
        disappear_block[r][c+1] = 1
        disappear_block[r-1][c] = 1
        disappear_block[r-1][c+1] = 1

    def count():
        cnt = 0
        for r in range(m):
            cnt += sum(disappear_block[r])
        return cnt

    def remove_block():
        for r in range(m):
            for c in range(n):
                if disappear_block[r][c] == 1:
                    board[r][c] = 0

    def rearrange_board():
        for c in range(n):
            empty_bottom = 0
            r = m
            # 아래 로직 while 문으로 변경하기
            while r > 0:
                r -= 1
                if empty_bottom == -1:
                    break
                if board[r][c] == 0:
                    empty_bottom = max(empty_bottom, r)
                if empty_bottom > 0 and board[r][c] != 0:
                    board[empty_bottom][c] = board[r][c]
                    board[r][c] = 0
                    empty_bottom -= 1

    cnt = 0
    while True:
        # 보드 아래에서부터 확인한다.
        for r in range(m-1, 0, -1):
            for c in range(n-1):
                if checkIf(r, c):
                    recordIt(r, c)
        chk = count()
        if chk == 0:
            return cnt
        cnt += chk
        remove_block()
        rearrange_board()
        disappear_block = [[0 for _ in range(n)] for _ in range(m)]

    return cnt
