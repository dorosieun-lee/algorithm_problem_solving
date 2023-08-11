# Baekjoon 9095 1,2,3 더하기
# Dynamic Programming 문제는 규칙 찾기가 관건!
# N: 1, 2, 3, 4, 5, 6, 7 인 경우 손으로 써보고 규칙 찾아냄
# 3, 4, 7 은 문제에서 주어진거 참고

T = int(input())

for test in range(1, T+1):
    N = int(input())
    lst = [0, 1, 2, 4]
    if N >= 4:
        for i in range(4, N+1):
            lst.append(lst[i-3] + lst[i-2] + lst[i-1]) # 규칙!

    print(lst[N])

