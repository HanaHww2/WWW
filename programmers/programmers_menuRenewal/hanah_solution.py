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
