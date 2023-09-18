# SWEA 1486 장훈이의 높은 선반

from itertools import combinations as comb

T = int(input())

for test in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    result = float("inf")
    for i in range(1, N+1):
        my_lst = list(map(sum, comb(heights, i)))
        if max(my_lst) > B:
            for l in my_lst:
                if l > B:
                    result = min(result, l)

    print(f'#{test} {result - B}')