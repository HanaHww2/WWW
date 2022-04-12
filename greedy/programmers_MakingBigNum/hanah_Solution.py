def solution(number, k):
    answer = ''
    LEN = len(number) - k

    # 스택을 이용해서 앞 뒤의 값을 비교한다.
    # 앞의 값이 뒤의 값보다 작으면 삭제, 아니면 그대로 둔다.
    def check_fb(number):
        # while문 사용
        # cnt 더하기
        i = 0
        cnt = 0
        num_list = list(number)
        stack = []
        while i < len(num_list):
            while cnt < k and stack and stack[-1] < num_list[i]:
                stack.pop()
                cnt += 1
            stack.append(num_list[i])
            i += 1
        return stack[:LEN]

    answer = ''.join(check_fb(number))
    return answer