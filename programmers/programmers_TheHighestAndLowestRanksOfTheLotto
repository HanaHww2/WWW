def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for pick_num in lottos:
        if pick_num in win_nums:
            answer.append(pick_num)
        if pick_num == 0:
            cnt += 1
            
    rank_list = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1} # 일치하는 개수:순위
    rank = rank_list[len(answer)]
    # print(len(answer))
    max_rank = rank_list[len(answer)+cnt]
    return max_rank, rank

# for x in win_nums:    로 최저 결과 추론
# lottos의 0 갯수 더한다
# 둘이 더하면 최고 결과.

# 그 두 결과로 몇 등인지 return
