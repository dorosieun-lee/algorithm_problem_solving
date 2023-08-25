# SWEA 2805 농작물 수확하기

# 농장의 크기는 항상 홀수
# 수확은 마름모 형태로만 가능
T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(N)]

    if N == 1:
        benefit = sum(MAP[0])
    else:
        benefit = 0
        col_dist = list(range(0, N//2)) + list(range(N//2, -1, -1))
        for row in range(N):
            for col in range(N//2 - col_dist[row], N//2 + col_dist[row]+1):
                benefit += MAP[row][col]

    print(f'#{test} {benefit}')