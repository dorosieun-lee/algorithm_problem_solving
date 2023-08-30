# SWEA 5189 전자카트
# 최소배터리 사용량
# 각 행과 열 한번만 방문인데 모두 방문해야함

def DFS(row, col_list, total):
    global MIN
    if len(col_list) == N-1:
        total += MAP[row][0]
        MIN = min(total, MIN)
        return

    for col in range(N):
        if col != row and col != 0 and not visited[col]:
            visited[col] = True
            DFS(col, col_list+[col], total + MAP[row][col])
            visited[col] = False


T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    MIN = 100*N
    visited = [False] * N
    DFS(0, [], 0)

    print(f'#{test} {MIN}')