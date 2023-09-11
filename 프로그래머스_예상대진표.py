# 프로그래머스 예상대진표
import math

def calc_answer(n, a, b):
    mid = n // 2
    # mid를 기준으로 a, b가 양쪽에 위치하는 경우
    if (a <= mid and b > mid) or (a > mid and b <= mid):
        return int(math.log(n, 2))
    # a, b가 mid보다 작은 영역에 속하는 경우
    elif a <= mid and b <= mid:
        return calc_answer(mid, a, b)
    # a, b가 mid보다 큰 영역에 속하는 경우
    elif a > mid and b > mid:
        return calc_answer(mid, a - mid, b - mid)


def solution(n, a, b):
    # a, b가 바로 만나는 경우
    if (a % 2 == 0 and a - 1 == b) or (b % 2 == 0 and b - 1 == a):
        answer = 1
    else:
        answer = calc_answer(n, a, b)

    return answer

print(solution(8, 2, 3))