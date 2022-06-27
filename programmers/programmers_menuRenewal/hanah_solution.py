# 집합을 활용해보고 싶어서 도전 중
# 테스트 통과를 못하고 있다... 수정이 필요함
from collections import Counter, defaultdict


def solution(orders, course):
    answer = []
    # 내림차순 정렬
    asc_orders = sorted(orders, key=len, reverse=True)
    temp = set()
    comb_list = []
    comb_set = set()

    for idx in range(len(asc_orders)):
        item = set(asc_orders[idx])
        for order in asc_orders[idx+1:]:
            temp = set(order) & item
            if len(temp) in course:
                comb_list.append(temp)
                #print(order, item, temp)
                comb_set.add(''.join(sorted(temp)))

    return sorted(list(comb_set))


# 최초 풀이
# dfs를 이용해서 combination 생성


def solution(orders, course):
    answer = []
    comb_dict = {n: defaultdict(int) for n in course}

    def mk_comb(prefix, remainder):
        length = len(prefix)
        if length in course:
            print(sorted(prefix))
            prefix = ''.join(sorted(prefix))
            comb_dict[length][prefix] += 1

        if not remainder:
            return
        for i, one in enumerate(remainder):
            mk_comb(prefix+one, remainder[i+1:])

    s_orders = sorted(orders, key=len)  # 길이함수를 이용해 정렬

    for order in s_orders:
        # 조합 만들기
        mk_comb('', order)
    print(comb_dict)

    for n in course:
        temp = []
        prev = 2
        for key in comb_dict[n].keys():
            val = comb_dict[n][key]
            if val > prev:
                prev = val
                temp = [key]
            elif val == prev:
                temp.append(key)
        answer += temp

    return sorted(answer)
