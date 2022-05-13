def solution(citations):
    sorted_c = sorted(citations, reverse=True)

    for idx, cnt in enumerate(sorted_c):
        if idx + 1 <= cnt:
            # 논문당 인용 횟수보다 인용된 논문 갯수가 작다면,
            # 계속 진행
            continue
        return idx
    # 모든 논문당 인용 횟수가 인용된 논문 갯수보다 크다면
    # 전체 길이 반환
    return len(citations)
