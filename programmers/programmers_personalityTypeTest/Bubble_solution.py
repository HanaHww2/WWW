# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def makeResult(personal, a, b):
    if personal[a] >= personal[b]:
        return a
    else:
        return b

def solution(survey, choices):
    # 사전순
    personal = {"A":0, "N":0, "C":0, "F":0, "J":0, "M":0, "R":0, "T":0}
    scores = {1:3, 7:3, 2:2, 6:2, 3:1, 5:1, 4:0}
    answer = ''
    
    for i in range(len(survey)): # survey[i] = "AN"
        if choices[i] > 4:  # 2번째 문자에 해당되는 유형에 점수를 더한다
            personal[survey[i][1]] += scores[choices[i]]
        else:               # 1번째 문자에 해당되는 유형에 점수를 더한다
            personal[survey[i][0]] += scores[choices[i]]

    # 지표별로 성격 유형을 판단한다        
    answer += makeResult(personal, "R", "T")
    answer += makeResult(personal, "C", "F")
    answer += makeResult(personal, "J", "M")
    answer += makeResult(personal, "A", "N")

#     # R-T
#     if personal["R"] >= personal["T"]:
#         answer += 'R'
#     else:
#         answer += 'T'
        
#     # C-F
#     if personal["C"] >= personal["F"]:
#         answer += 'C'
#     else:
#         answer += 'F'

#     # J-M
#     if personal["J"] >= personal["M"]:
#         answer += 'J'
#     else:
#         answer += 'M'
        
#     # A-N
#     if personal["A"] >= personal["N"]:
#         answer += 'A'
#     else:
#         answer += 'N'
    
    
    return answer

# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"

# 1	매우 비동의
# 2	비동의
# 3	약간 비동의
# 4	모르겠음
# 5	약간 동의
# 6	동의
# 7	매우 동의