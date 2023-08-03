# SWEA16268 풍선팡2

T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_val = 0

    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < N) and (0 <= nj < M):
                    total += arr[ni][nj]

            if max_val < total:
                max_val = total

    print(f"#{test} {max_val}")