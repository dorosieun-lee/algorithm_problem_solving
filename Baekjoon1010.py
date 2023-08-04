# Baekjoon 1010 다리 놓기

# 완전탐색으로 풀이 -> 원소의 개수가 많아지면 시간 초과
# T = int(input())

# for test in range(1, T+1):
#     N, M = map(int, input().split())
#     subset = [[]]
#     cnt = 0
#
#     for x in range(M):
#         size = len(subset)
#         if len(subset[-1]) >= N:
#             size = N
#         for y in range(size):
#             subset.append(subset[y] + [x])
#             if len(subset[y] + [x]) == N:
#                 cnt += 1
#
#     print(f'{cnt}')

# 원소의 개수가 M개인 집합에서 원소의 개수가 N개인 부분집합의 개수 구하기
# MCN 의 순열 -> {M * (M-1) * (M-2) * ... * (M-N)} / {N * (N-1) *...* 1}
for test in range(1, T+1):
    N, M = map(int, input().split())

    up, down = 1, 1
    for m in range(M, M-N, -1):
        up *= m
    for n in range(1, N+1):
        down *= n

    cnt = int(up / down)

    print(f'{cnt}')