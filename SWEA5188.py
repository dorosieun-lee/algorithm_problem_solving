# SWEA 5188 최소합

T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    n = 1
    cap = 0
    while n <= (N-1)*(N-1):
        for i in range(cap, n - cap + 1):
            j = n - i
            if (i-1 >= 0) and (j-1 >= 0):
                MAP[i][j] += min(MAP[i-1][j], MAP[i][j-1])
            elif (i-1 < 0) and (j-1 >= 0):
                MAP[i][j] += MAP[i][j - 1]
            elif (i-1 >= 0) and (j-1 < 0):
                MAP[i][j] += MAP[i - 1][j]

        n += 1
        if n >= N:
            cap += 1

    print(f'#{test} {MAP[N-1][N-1]}')

