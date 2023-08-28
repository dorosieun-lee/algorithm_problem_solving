# SWEA 12712 파리퇴치3
# 십자 또는 X자로 분사
# 잡을 수 있는 최대 파리 수

d1 = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 십자
d2 = [-1, -1], [-1, 1], [1, 1], [1, -1] # 엑스자
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0

    for row in range(N):
        for col in range(N):
            total1 = MAP[row][col]
            total2 = MAP[row][col]
            for m in range(1, M):
                for i in range(4):
                    r1 = row + d1[i][0] * m
                    c1 = col + d1[i][1] * m
                    if (0 <= r1 < N) and (0 <= c1 < N):
                        total1 += MAP[r1][c1]
                for j in range(4):
                    r2 = row + d2[j][0] * m
                    c2 = col + d2[j][1] * m
                    if (0 <= r2 < N) and (0 <= c2 < N):
                        total2 += MAP[r2][c2]

            MAX = max([MAX, total1, total2])

    print(f'#{test} {MAX}')
