import itertools

# 해볼 것
# itertools 사용한 풀이


def solution(relation):
    answer = []
    store = []
    data_size = len(relation)
    num_cols = len(relation[0])

    for i, cols in enumerate(zip(*relation)):
        store.append(cols)  # 행렬 Transpose

    def check_if_subset(new):
        print(answer, new)
        temp = []
        for i, item in enumerate(answer):
            if set(new) <= set(item):
                temp.append(i)
            elif set(item) <= set(new):
                return answer

        while temp:
            del answer[temp.pop()]
        else:
            answer.append(new[:])

        return answer

    def make_tuple_set(prefix):
        temp = set()
        for x in zip(*prefix):
            temp.add(x)
        return temp

    def make_combi(prefix, idx_arr, store, idx):

        for i, data in enumerate(store):

            prefix.append(data)
            idx_arr.append(i+idx)

            result = make_tuple_set(prefix)

            if len(result) != data_size:
                make_combi(prefix, idx_arr, store[i+1:], i+idx+1)
            else:
                answer = check_if_subset(idx_arr)
                idx_arr.pop()
                prefix.pop()  # 마지막 데이터 제거하고 다시 순회
                continue
            idx_arr.pop()
            prefix.pop()  # 마지막 데이터 제거하고 다시 순회

    make_combi([], [], store, 0)
    return len(answer)
