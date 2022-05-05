def solution(priorities, location):
    cnt = 0
    index_bound = len(priorities)-1

    # 남아있는 최대값을 확인하기 위해 정렬한 리스트를 만들어둔다.
    sorted_p = sorted(priorities)
    printed = []

    idx = 0  # 인덱스, 포인터 초기화
    while priorities:  # 주어진 배열을 조작하지 않기 때문에 항상 True나 다름없다.
        if idx > index_bound:
            idx = 0  # index out of range 방지

        if priorities[idx] == sorted_p[-1]:  # 최대값과 같다면
            sorted_p.pop()
            printed.append(idx)  # 프린트되는 순서를 저장한다.

            if idx == location:  # 내가 알고자 하는 위치의 자료가 프린트되었다면
                return len(printed)  # 프린트된 내역의 길이를 반환해서 몇 번째에 출력했는지 확인한다.

        idx += 1

    return cnt


# 과거 풀이
# (현재 과거에 비해 여러모로 개선 혹은 좀 변화가 있는 것 같다. 변수명이 너무 짧고 의미불명인 건 이제 싫다. 손가락 아파도 길게 쓴다.)
def solution(pr, l):
    answer = 0
    c = 0
    while pr:
        # max값과 비교
        # 아래처럼 항상 max 연산이 수행되지 않게 변수로 값을 선언하고,
        # 최댓값을 갖는 프린터를 출력한 이후에 새로운 최댓값을 재할당해줄 필요가 있다.
        if max(pr) > pr[0]:
            # 리스트를 조작해준다.
            # 퍽 불필요한 작업을 수행했던 것 같다.
            # 포인터를 활용한다는 개념이 없었나보다. 푸는데 급급했다거나ㅎㅎ
            pr.append(pr[0])
            del pr[0]  # 시간복잡도??

            # 내가 찾는 위치 인덱스도 조작을 해준다.
            if l != 0:
                l -= 1
            else:
                l = len(pr)-1

        # 최댓값과 같은 경우
        else:
            del pr[0]
            c += 1  # 출력된 자료 갯수를 카운트

            if l == 0:  # 내 자료가 출력되었다면
                break
            else:
                # 내가 찾는 위치 인덱스도 조작 (코드가 중복되어 있다. 메서드로 따로 만들어줄 수 있다.)
                if l != 0:
                    l -= 1
                else:
                    l = len(pr) - 1
    answer = c
    return answer
