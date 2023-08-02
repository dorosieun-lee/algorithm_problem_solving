# SWEA 2001 파리퇴치
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.

T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N):
        for j in range(N):
            fly_sum = 0
            for di in range(M):
                for dj in range(M):
                    ni = i + di
                    nj = j + dj
                    if (0 <= ni < N) and (0 <= nj < N):
                        fly_sum += arr[ni][nj]

            if max_val < fly_sum:
                max_val = fly_sum

    print(f'#{test} {max_val}')
