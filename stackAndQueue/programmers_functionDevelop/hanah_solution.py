# https://programmers.co.kr/learn/courses/30/lessons/42586 (기능개발)

# 과거 풀이 (데큐 사용)
def solution(progresses, speeds):
    answer = []
    days = [(100-p)//s if (100-p)%s==0 else (100-p)//s +1 for p, s in zip(progresses, speeds)]
    
    from collections import deque
    days = deque(days)
    
    count = 1
    d = days.popleft()
    while len(days)>0:
        if d >= days[0]:
            days.popleft()
            count +=1
        else:
            answer.append(count)
            d = days.popleft()
            count = 1
    answer.append(count)      
    
    return answer

# 1번 풀이
import math
def solution(progresses, speeds):
    answer = []
    day_list = []
    temp = 0
    
    # 큰 수 구하기?
    for idx, p, s in zip(range(len(speeds)), progresses, speeds):
        days = math.ceil((100-p)/s)
        if not day_list:
            day_list.append(days)
        if day_list and day_list[-1] < days:
            day_list.pop()
            answer.append(temp)
            day_list.append(days)
            temp = 0
        if idx == len(speeds)-1:
            answer.append(temp+1)
            
        temp +=1
    return answer

# 2. while 문으로 변경 
import math
def solution(progresses, speeds):
    answer = []
    day_list = []
    temp = 0
    idx = 0
    length = len(speeds)

    while length > idx:
        days = math.ceil((100 - progresses[idx])/speeds[idx])
        
        if not day_list:
            day_list.append(days)
        if day_list and day_list[-1] < days:
            day_list.pop()
            answer.append(temp)
            day_list.append(days)
            temp = 0
        temp += 1
        idx += 1
        
    answer.append(temp) # 마지막 배포 기능 수 추가    
    
    return answer