import sys
min_move = sys.maxsize

def solution(name):
    cnt = 0
    index = []
    length = len(name)
    global min_move
    
    # 아스키 코드 65 ~ 90
    def count_up_down(a):
        ascii_num = ord(a)
        return min(ascii_num-65, 90-ascii_num+1)
    
    for i, a in enumerate(name):
        if a == 'A': continue
        cnt += count_up_down(a) # 위아래 카운트
        index.append(i) # A 외 알파벳의 인덱스값 리스트
    
    # 좌우 이동 카운트
		# dfs를 이용해 완전 탐색 수행
		# min_move 전역 변수를 활용해 가능하다면 백트랙킹 수행
    def dfs(index, current, current_move):
        global min_move
        if min_move <= current_move:
            return
        if not index:
            min_move = current_move
            return
				
				# 개선이 가능할 거 같지만 일단 패스
        left_d = abs(index[-1] - length) + current if index[-1] > current else current - index[-1]  
        right_d = index[0] - current if index[0] >= current else abs(current - length) + index[0]
        
        dfs(index[1:], index[0], current_move + right_d)
        dfs(index[:-1], index[-1], current_move + left_d)
        
    dfs(index, 0, 0)
    
    return cnt + min_move